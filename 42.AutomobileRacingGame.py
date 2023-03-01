# Let's create code that will be a part of a racing game. Each player can choose a different automobile to race in.

class Automobile:
    def go(self):
        print('Racing forward')

    def stop(self):
        print('Stopping')


class Motorcycle(Automobile):
    def wheelie(self):
        print('Popping a wheelie')


class Racecar(Automobile):
    def reverse(self):
        print('Reversing')

    def goTo100(self):
        print('Increasing to 100 mph')


motorcycle = Motorcycle()
motorcycle.go()
motorcycle.wheelie()
racecar = Racecar()
racecar.goTo100()
