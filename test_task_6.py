class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        print('Dog goes woof')


class Cat(Animal):
    def voice(self):
        print('cat goes meow')


class Bird(Animal):
    def voice(self):
        print('Bird goes tweet')


class Mouse(Animal):
    def voice(self):
        print('and mouse goes squeak')


class Fox(Animal):
    def voice(self):
        print('What does the fox say?')


Dog().voice()
Cat().voice()
Bird().voice()
Mouse().voice()
Fox().voice()
