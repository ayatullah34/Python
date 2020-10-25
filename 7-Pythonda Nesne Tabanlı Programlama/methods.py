
# class Person:

#     address = 'no information'

#     #constructor
#     def __init__(self,name,year):

#         self.name = name
#         self.year = year
#         print("init çalıştı")

#     #instance methods
#     def intro(self):
#         print("hello there " + self.name)

#     def calculateAge(self):
#         return 2019 - self.year

    

# p1 = Person("ali",1990)
# p2 = Person("veli",1920)

# p1.name = "cem"

# print (f'name:{p1.name}  year:{p1.year} address:{p1.address}')

# p1.intro()
# p2.intro()

# print(f'name:{p1.name} yaş:{p1.calculateAge()} ')
# print(f'name:{p2.name} yaş:{p2.calculateAge()} ')


class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,r = 1):
        self.r = r

    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.r

    def alan_hesapla(self):
        return self.pi * (self.r ** 2)

    
c1 = Circle()
c2 = Circle(5)

print(f'c1: alan={c1.alan_hesapla()} cevre={c1.cevre_hesapla()}')

print(f'c2: alan={c2.alan_hesapla()} cevre={c2.cevre_hesapla()}')



