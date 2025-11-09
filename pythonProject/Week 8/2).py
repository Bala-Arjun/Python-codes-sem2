

class ATM:
    def __init__(self):
        self.pwd = 1234
        self.balance = 10000

    def pwd_check(self, pwd):
        if self.pwd == pwd:
            while True:
                print("." * 30)
                print("1.Balance ", "2.Deposit", "3.Withdrawal", "4.Exit", sep="\n")
                choice = int(input("Enter your choice : "))
                print("." * 30)
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    amount = int(input("Enter your amount : "))
                    self.deposit(amount)
                elif choice == 3:
                    amount = int(input("Enter your amount : "))
                    self.withdrawal(amount)
                else:
                    print("Thanks for visiting our ATM")
                    break
        else:
            print("Incorrect password..")

    def check_balance(self):
        print("Account balance :", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} has been credited to your account..")
        print("Account balance :", self.balance)

    def withdrawal(self, amount):
        self.amount = amount
        if (self.balance >= self.amount):
            if (self.amount % 100 == 0):
                self.balance = self.balance - amount
                print(f"{amount} has been debited from your account..")
                print("Account balance :", self.balance)
            else:

                self.amount = int(input("Enter valid amount.."))
                self.withdrawal(self.amount)
        else:
            print("Insufficient funds..")


if __name__ == '__main__':
    print("Welcome to SBI bank")
    a = ATM()
    pin = int(input("Enter your PIN"))
    a.pwd_check(pin)



