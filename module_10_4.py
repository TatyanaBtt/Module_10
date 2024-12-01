from queue import Queue
import threading
import time
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
        self.lock = threading.Lock()


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eating_time = random.randint(3, 10)
        time.sleep(eating_time)


class Cafe:
    def __init__(self, *tables):
        self.guest = None
        self.queue = Queue()
        self.tables = tables
        self.lock = threading.Lock()

    def guest_arrival(self, *guests):
        for guest in guests:
            assigned_table = None
            with self.lock:
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        assigned_table = table
                        break
                if assigned_table:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                else:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()