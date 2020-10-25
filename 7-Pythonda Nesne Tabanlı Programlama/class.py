
class Person:

    address = 'no information'

    def __init__(self,name,year):

        self.name = name
        self.year = year
        print("init çalıştı")

p1 = Person("ali",1990)
p2 = Person("veli",1990)

p1.name = "cem"

print (f'name:{p1.name}  year:{p1.year} address:{p1.address}')


