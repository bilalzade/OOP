# Sinif dəyişənləri (class variables) və obyekt dəyişənləri (instance variables)
# 1 xal
# Məqsəd: Sinifə məxsus olan verilənlərlə hər bir obyektə məxsus olan verilənlərin fərqini göstərmək.

# Təlimatlar:

# Car adlı sinif yaradın və total_cars adlı sinif dəyişəni təyin edin; bu dəyişən yaradılan Car obyektlərinin ümumi sayını saxlasın.
# __init__ metodunda hər dəfə yeni Car obyekti yaradıldıqda total_cars dəyişənini artırın.
# Obyekt səviyyəsində (instance attribute) model və year atributları əlavə edin.
# Bir neçə Car nümunəsi yaradın və total_cars-ın necə dəyişdiyini, model və year kimi atributların isə hər obyektdə fərqli olduğunu nümayiş etdirin.

class Car:

    total_cars = 0

    def __init__ (self, model, year):
        self.model = model
        self.year = year
        Car.total_cars += 1

    def print(self):
        print(f"{self.model} avtomobili {self.year} il istehsalidir")


car1 = Car ("Toyota Corolla", 2012)
car2 = Car ("Ford Fusion", 2017)
car3 = Car ("Lexus LX570", 2013)
car4 = Car ("BMW 328i", 2014)

car1.print()
car2.print()
car3.print()
car4.print()

print(f"Umumi avtomobil sayi: {Car.total_cars}")

