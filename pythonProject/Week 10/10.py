class LowBalanceError(Exception):
    def idk2(self):
        print('...low balance cannot withdraw given amount...')
class ATM:
    def idk(self):
        self.withdraw=int(input('enter the withdrawal amount: '))
        self.balance = 10000
        try:
            if self.balance<self.withdraw:
                raise LowBalanceError()
            else:
                self.balance=self.balance-self.withdraw
                print(self.balance)
        except LowBalanceError as e:
            print(e.idk2())
s=ATM()
s.idk()