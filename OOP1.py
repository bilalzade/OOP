# Məqsəd: Sinifin (class) necə yaradılacağı, nümunələrin (instances) necə istifadə ediləcəyi və atributlara necə müraciət ediləcəyi barədə baza anlayışlarını öyrənmək.

# Təlimatlar:

# Person adlı sinif yaradın.
# Bu sinifdə name və age atributları olsun.
# __init__ metodu yazaraq bu atributları təyin edin.
# Müxtəlif name və age dəyərləri ilə iki-üç Person obyekti yaradın.
# Hər obyektin atributlarını ekranda (print vasitəsilə) göstərin.

class Person():

    def __init__ (self, name, age):
        self.name = name
        self.age = age    

person1 = Person("Harun", 32)
person2 = Person("Atilla", 24)
person3 = Person("Oqtay", 19)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(person3.name, person3.age)