class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdraw_list = []

    def withdraw(self, request):
        print("Bank Name is:", self.bank_name)
        print("balance is ", self.balance)

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdraw_list.append(request)
            self.balance = self.balance - request
            notes = [100, 50, 10, 5]
            for note in notes:
                while request >= note:
                    request = request - note
                    print("give ", str(note))

            while request < 5 and request > 0:
                print("give " + str(request))
                request = 0
                break

        return self.balance

    def show_withdraw_list(self):
        for i in self.withdraw_list:
            print(i)


atm1 = ATM(1000, 'Faisal Bank')
atm2 = ATM(700, 'HSBC Bank')

atm1.withdraw(355)
atm1.withdraw(800)
atm1.show_withdraw_list()


atm2.withdraw(500)
atm2.withdraw(50)
atm2.show_withdraw_list()