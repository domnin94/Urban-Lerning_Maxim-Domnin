import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Депозит {amount}. Баланс после пополнения: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Снятие {amount}. Баланс после снятия: {self.balance}')
            else:
                print("Недостаточно средств на счете")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount(1000)
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 200))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()