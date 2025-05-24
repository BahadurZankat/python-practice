class Student:
    def __init__(self,name):
        self.name=name


s1= Student("Shradha")
print("#Before Nothing gets Deleted")
print(s1)
print(s1.name)
del s1.name
print("#After Name property Deleted")
print(s1)
print(s1.name)
del s1
print("#After Entire Object Deleted Deleted")
print(s1)