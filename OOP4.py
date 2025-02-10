# Miras (Inheritance): Animal və törəmə siniflər
# 1 xal
# Məqsəd: Baza sinif (superclass) və ondan irsi götürən törəmə siniflərin (subclass) yaradılmasını məşq etmək.

# Təlimatlar:

# Animal adlı baza sinfi yaradın, name və age atributları olsun.
# Animal sinfində make_sound() adlı metod yaradın. Məsələn, print("Some generic sound").
# Dog və Cat adlı iki törəmə sinif yaradın və Animal-dan miras alsınlar.
# make_sound() metodunu hər sinifdə yenidən (override) təyin edin. Məsələn, Dog üçün print("Bark!"), Cat üçün print("Meow!").
# Dog və Cat obyektləri yaradın, make_sound() metodlarını çağırın və fərqli nəticələr aldığınızı yoxlayın.

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self, ses):
        print(f"{self.name} bele ses cixarir: {ses}")

class Dog(Animal):
    
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Hav-Hav!")

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Miyau!")

husky = Dog("Qarabas", 2)
lili = Cat("Lili", 6)

husky.make_sound()
lili.make_sound()

doberman = Animal("Boo", 5)

doberman.make_sound("AUUUU")