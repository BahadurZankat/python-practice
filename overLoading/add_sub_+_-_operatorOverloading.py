# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
class Complex:
    def __init__(self,rel,img):
        self.rel=rel
        self.img=img
    
    def showNumber(self):
        print(self.rel," i +",self.img," j")

    def __add__(self,num2):
        newReal=self.rel+num2.rel
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.rel-num2.rel
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    
num1=Complex(8,2)
num1.showNumber()

num2=Complex(1,4)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num4=num1-num2
num4.showNumber()