class Account:
    def __init__(self, bal, acc):
        self.balance = float(bal)
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Debit: Rs.", amount, "was debited.")
        print("Total balance: Rs.", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Credit: Rs.", amount, "was credited.")
        print("Total balance: Rs.", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account("10000", 12345)
print("Your Current balance is:",acc1.balance,"& your account no is: ",acc1.account_no)
acc1.debit(1000)
acc1.credit(3000)