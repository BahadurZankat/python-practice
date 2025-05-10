class Student:
    #This constructor called as default constructor.
    #created by python if not define explicitily
    def __init__(self):
        pass

    #This constructor called as parameterized constructor.
    def __init__(self,name,marks):
        print("you are inside parametrized constructor")
        self.name=name
        self.marks=marks

s1=Student("Bahadur")
print("Hey my name is" + s1.name)
s2=Student("Zankat")
print("Hey my name is" + s2.name)
s3=Student("Raju")
print("Hey my name is" + s3.name)
s4=Student("Zala")
print("Hey my name is" + s4.name)