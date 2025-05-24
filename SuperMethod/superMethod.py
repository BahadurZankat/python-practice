# Super Method is also known as special Method 
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("car Stopped")    

class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()


car1=Toyota("My Car","petrol")
print(car1.type) 
# OUT PUT :
# Car Started
# petrol



# Note :
#  Super() method is used to access the parent class method from child class method