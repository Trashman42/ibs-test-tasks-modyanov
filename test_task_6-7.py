class Animal:
    cnt = 0

    def __init__(self):
        Animal.cnt += 1

    def voice(self):
        pass


def num_inst():
    return f'Number of instance: {Animal.cnt}'


class Dog(Animal):
    def voice(self):
        return 'Dog goes woof'


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


class FoxSay(Fox):
    def voice(self):
        print('''\t\tRing-ding-ding-ding-dingeringeding!
        Wa-pa-pa-pa-pa-pa-pow!
        Hatee-hatee-hatee-ho!
        Joff-tchoff-tchoff-tchoffo-tchoffo-tchoff!''')


print(num_inst(), '\n')
a = Dog().voice()
print(a)
Cat().voice()
Bird().voice()
Mouse().voice()
Fox().voice()
fox = FoxSay()
fox.voice()
print('\n', num_inst())
