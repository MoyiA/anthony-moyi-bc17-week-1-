class Animal():
    def __init__(self, walk, sound):
        ''' class takes attributes walk and sound
        '''
        
        self.walk = walk
        self.sound = sound

class Dog(Animal):
    def make_sound(self):
        return "bark"
    
scooby = Dog("dog walks", "bark") 

class Cat(Animal):
    def make_sound(self):
        return "meow"

topcat = Cat("cat walks", "meow")

def check_sound(obj):
    if obj.make_sound() == "meow":
        print("it is a cat")
    elif obj.make_sound() == "bark":
        print("it is a dog")

check_sound(topcat)
check_sound(scooby)
print(scooby.walk)   