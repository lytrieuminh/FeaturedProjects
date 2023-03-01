# Using Object-Orientated Programming (OOP), we'll create a virtual vending machine with the same functionality and properties as a real-life soda machine.

class Soda_Machine:
    paid = False
    balance = 0

    def eject_soda(self):
        if paid == False:
            print('Please insert money')
        else:
            print('Enjoy the soda!')

    def pay(self, amount):
        self.balance += amount

    def select_soda(self):
        if balance >= 1:
            self.paid = True
            self.balance -= 1
        else:
            self.paid = False
