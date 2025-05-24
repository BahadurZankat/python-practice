class Car:
    colour="black"

    @staticmethod
    def start():
        print("Car Started")

    def stop():
        print("car Stopped")    

class Toyota(Car):
    def __init__(self,name):
        self.name=name


car1=Toyota("My Car")
print(car1.name)  # used own propert
print(car1.colour) # Used Parent Property
car1.start() # Used Parent Method
# Note :
# This is called as siple or single inheritance.