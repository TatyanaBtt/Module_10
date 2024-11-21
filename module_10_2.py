import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.warriors = None
        self.name = name
        self.power = power
        self.warriors = 100
        self.day = 0

    def timer(self, name, power):
        while self.warriors > 0:
            time.sleep(1)
            self.warriors -= self.power
            self.day += 1
            print(f'{self.name} сражается {self.day} день, осталось {self.warriors} воинов.')

    def run(self):
        print(f'{self.name} на нас напали!')
        self.timer(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
