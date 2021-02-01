"""class Person:#class list
    def __init__(self,fname,lname,age):#cnstructor or object vaiables like index in list
        self.fname=fname
        self.lname=lname
        self.age=age
    def full_name(self): #instance method like append ,clear,pop,etc in list
        return self.fname+" "+self.lname

p1=Person('pawan','kumar',20)#object l1=[1,2,3,4]
print(p1.fname) #printing value of object variables like l1[0]
print(p1.full_name()) #like l1.pop() in list"""

"""class Laptop:
    def __init__(self,brand,price, model):
        self.brand=brand
        self.price=price
        self.model=model
    def after_discount(self,percent):
        return self.price-(percent/100*self.price)
laptop1=Laptop('hp',70000,'xxx')
laptop2=Laptop('dell',60000,'yyy')
print(f"price of laptop1 after discount is {laptop1.after_discount(10)} or {Laptop.after_discount(laptop1,10)}")
print(f"price of laptop2 after discount is {laptop2.after_discount(10)} or {Laptop.after_discount(laptop2,10)}")"""
# class variale

"""class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*(self.radius**2)
    def perimeter(self):
        return 2*Circle.pi*self.radius
circle1=Circle(10)
print(f"radius is {circle1.radius}")
print(f"area is {circle1.area()}")
print(f"perimeter is {circle1.perimeter()}") """
"""class Laptop:
    percent=10
    def __init__(self,brand,price, model):
        self.brand=brand
        self.price=price
        self.model=model
    def after_discount(self):
        return self.price-(self.percent/100*self.price)

laptop1=Laptop('hp',70000,'xxx')
laptop2=Laptop('dell',60000,'yyy')
laptop2.percent=100
print(f"price of laptop1 after discount is {laptop1.after_discount()} or {Laptop.after_discount(laptop1)}")
print(f"price of laptop2 after discount is {laptop2.after_discount()} or {Laptop.after_discount(laptop2)}")
print(laptop2.__dict__)"""
"""class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.__price=price
phone1=Phone('nokia',1100,1000)

print(phone1._Phone__price)
phone1._Phone__price=500#no change in original value
print(phone1.__dict__)"""
#property setter decorator
"""class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price= max(price,0)
        # if price>0:
        #     self.price=price
        # self.price=0
    @property
    def info(self):
        return f"{self.name}{self.model} price is {self._price} "
    @property
    def price(self):
        return self._price
    @price.setter
    def pric(self,new_price):
        self._price= max(new_price,0)
phone1=Phone('nokia',110,1000)
phone1.pric=-500000  #setter pric mathod
print(phone1.price)  # property price method
print(phone1.info)
print(phone1.__dict__)"""
#inheritance
"""class Phone:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Smartphone:
    def __init__(self,name,price,ram):
        Phone.__init__(self,name,price)
        self.ram=ram
sma=Smartphone('nokia',1000,'6gb')
print(sma.ram)"""
