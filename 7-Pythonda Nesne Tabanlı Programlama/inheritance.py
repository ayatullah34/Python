# Inheritance (Kalıtım): Miras alma

# Person => name, lastname , age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print("person created")

    def who_am_i(self):
        print("i am a person")

    def eat(self):
        print("i am eating")

class Student(Person):

    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number = number
        print("student created")

    #overriding
    def who_am_i(self):
        print("i am a student")

    def sayHello(self):
        print("hi i am a student")


class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"i am a {self.branch} teacher")
    


p1 = Person("ali","yılmaz")
p2 = Student("veli","turan",23)
p3 = Teacher("aziz","nesin","edebiyat")

print(p1.firstname + " " + p1.lastname)
print(p2.firstname + " " + p2.lastname + " " + str(p2.number))
print(p3.firstname + " " + p3.lastname)

p1.who_am_i()
p2.who_am_i()
p3.who_am_i()

p1.eat()
p2.eat()

p2.sayHello()