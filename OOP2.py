# Məqsəd: Obyektin daxilindəki verilənlər üzərində əməliyyat icra edən metodlar yazmaq və enkapsulyasiya prinsiplərini göstərmək.

# Təlimatlar:

# Birinci tapşırıqda yaratdığınız Person sinfinə və ya yeni bir sinifə (məsələn, BankAccount) keçid edin.
# O sinfə obyektin (instance) məlumatlarından istifadə edən metodlar əlavə edin (məsələn, deposit, withdraw, check_balance və s.).
# Əsas blokda (main) və ya test hissəsində bu metodlardan istifadə nümunələri göstərin.



class Person:

    def __init__ (self, name, age, midname, profession, gender):
        self.name = name
        self.age = age
        self.midname = midname if midname else None
        self.profession = profession
        self.gender = gender
    
    def print_all(self):
        print(f"{self.name} {self.age} {self.midname} {self.profession} {self.gender}")

    def cng_midname (self, newmidname):
        if self.midname:
            self.midname = newmidname
            print(f"{self.name} sexsinin yeni leqebi {newmidname}")
        else:
            print(f"{self.name} sexsinin leqebi yoxdur")
    
    def cng_profession (self, newprofession):
        self.profession = newprofession
        print(f"{self.name} adli sexsin yeni pesesi {newprofession}")
    
        
    def cng_gender (self, newgender, newname):
        self.gender = newgender
        print(f"{self.name} cinsini deyiserek {newgender} oldu ve yeni adi {newname}")
        self.name = newname

person1 = Person("Henry", "19", "Bazooka", "Muellim", "Man")
person2 = Person("Oscar", "32", "", "Pilot", "Man")

person1.print_all()
person2.print_all()

person1.cng_gender("Woman", "Alexa")
person2.cng_gender("Woman", "Jane")
person1.cng_midname("Papaq")
person2.cng_midname("Kotuk")
person1.cng_profession("Kosmonavt")
person2.cng_profession("Polis")







