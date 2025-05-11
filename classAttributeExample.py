class Student:
    college_name="L E College"
    name="claaa name"

    def __init__(self,name):
        self.name=name
s1=Student("Rahul")
print(s1.name)
print(s1.college_name)


s2=Student("Gandhi")
print(s2.name)
print(s2.college_name)

#here , object attribute has higher precedence then class attaribute hence the output is
#Rahul
#L E College
#Gandhi
#L E College