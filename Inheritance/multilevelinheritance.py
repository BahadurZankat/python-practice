class Car:   
    @staticmethod
    def start():
        print("Car Started")

    def stop():
        print("car Stopped")    

class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type


fortuner1=Fortuner("Diesel")
print(fortuner1.start())  
# out put is - ar Started
# this method is define at 3rd level still it can be accessible due to multi-level inheritance