class Person:
    name="test" # class variable

    def __init__(self,name):
        self.name=name  # instance variable

    @classmethod
    def changeNameUsingClassMethod(cls,name):# This class Method can change the class variable name
        cls.name=name


p1=Person("person")
print(p1.name)
print(Person.name)
p1.changeNameUsingClassMethod("class Person")
print(Person.name)

# OUT PUT :
#    person
#    test
#    class Person

