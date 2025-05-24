class Person:
    name="Anynoumous"

    def changeName(self,name):
        self.name=name

    def changeClassName(self,name):
        Person.name=name
    def changeClassNameMethod2(self,name):
        self.__class__.name=name    

p1=Person()
p1.changeName("shradhha")
print(p1.name) # This will represent object variable name  [output is => shradhha]
print(Person.name) # This will represent class level variable name  [output is => Anynoumous]
p1.changeClassName("khapra")
print(Person.name) # This will represent class level variable name  [output is => khapra]
p1.changeClassName("khapra method 2")
print(Person.name) # This will represent class level variable name  [output is => khapra method 2]

