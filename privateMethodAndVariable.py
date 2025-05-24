class Person:
    __name="undefine"

    def __init__(self,name):
        self.__name=name

    def __hello(self):
        return self.__name

    def welcome(self):
        return self.__hello()  #Privarte methods are accessible within the class

s1= Person("shradhha")
#print(s1.__hello()) # Error as Private method not accessible out side of class
#print(s1.__name) # Error as Private variable not accessible out side of class
print(s1.welcome()) # shradhha