class Account:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def withdrawal(self):
        if balance > owner:
            print ("Insufficient Funds")
        else:
            print(owner - balance)

owner, balance = map(int, input().split())
p1 = Account(owner, balance)
p1.withdrawal()
