#Basic Class
class Emp:
    def __int__(self):
        #object Attritbutes (obj is instance of class)
        self.id = 0 #Default value
        self.basic=0
        self.allowance=0
        self.NoofHr=0
        self.rate=0
    #Method
    def Permanent(self):
        permanent=self.basic + self.basic * self.allowance
        print("Total permanent salary is:",permanent)
    def Temporary(self):
        temporary = self.NoofHr * self.rate
        print("Total temporary salary is:",temporary)
        
#upto this only class was defined and now after this we have to creat instances of that class
#_inti_ run by default, is a intialiazation fun
#internally self is emp1.id

#Created object instance
emp1 = Emp()

#Assigned values to attributes
emp1.id = 1
print(emp1.id)
emp1.basic = 1000
emp1.allowance = 0.6
#Executing method of object
emp1.Permanent()

#Another attribute
emp2 = Emp()
emp2.id = 2
print(emp2.id)
emp2.NoofHr = 30
emp2.rate=100
emp2.Temporary()

####################################

# Inheritance
#Emp is parent class or super class
class Emp:
    def __int__(self):
        self.id = 0 #Default value
        self.basic=0
        self.NoofHr=0
        self.rate=0
    #Method
    def Permanent(self):
        permanent=self.basic + self.basic 
        print("Total permanent salary is:",permanent)
    def Temporary(self):
        temporary = self.NoofHr * self.rate
        print("Total temporary salary is:",temporary)
        
class Per(Emp):
    def _init_(self):
        super()._init_()
        self.allowance = 0
    def Per_Payment(self):
        permanent=self.basic + self.basic * self.allowance
        print("Total permanent salary is:",permanent)

per1 = Per()

per1.basic = 1000
per1.allowance = 0.6
per1.Per_Payment()

class Temp(Emp):
    def _init_(self):
        super()._init_()
    def Temp_Payment(self):
        temporary = self.NoofHr * self.rate
        print("Total temporary salary is:",temporary)

temp1 = Temp()

temp1.NoofHr = 30
temp1.rate = 100
temp1.Temp_Payment()
