import threading, random, time


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            num_deposit = random.randint(50, 500)
            self.balance += num_deposit
            print(f'Пополнение: {num_deposit}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            num_take = random.randint(50, 500)
            print(f'Запрос на {num_take}')
            if num_take <= self.balance:
                self.balance -= num_take
                print(f'Снятие: {num_take}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

    def run(self):
        self.deposit()
        self.take()
        self.lock.locked()


bk = Bank()
t1 = threading.Thread(target=Bank.deposit, args=(bk,))
t2 = threading.Thread(target=Bank.take, args=(bk,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'Итоговый баланс: {bk.balance}')
