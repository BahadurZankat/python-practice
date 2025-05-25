class Student:
    def __init__(self,phy,chm,math):
        self.phy=phy
        self.chm=chm
        self.math=math
        #self.percentage=str((self.phy+self.chm+self.math)/3)+" %"

    def getPercentage(self):
        self.percentage=str((self.phy+self.chm+self.math)/3)+" %"

    @property
    def percentage(self):
        return str((self.phy+self.chm+self.math)/3)+" %"

s1 = Student(10,78,52)        
print(s1.percentage)
s1.phy=100
print(s1.phy)
#s1.getPercentage()
print(s1.percentage)
