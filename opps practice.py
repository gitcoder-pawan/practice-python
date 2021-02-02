# CLASS VARIABLE / INSTANCE VARIABLE / CHANGE IN CLASS VARIABLE

class Laptop:
    percent=10
    def __init__(self,name,model,price):
        self.model=model
        self.name=name
        self._price=max(price,0)
    def discount(self):
        return self._price-(self.percent/100*self._price)
laptop1=Laptop('hp','xxx',70000)
laptop2=Laptop('dell','yyy',60000)
laptop1.percent=0
print(laptop1.discount())
print(laptop2.discount())

#  DUNDER

class Laptop:
    percent=10
    def __init__(self,name,model,price):
        self.model=model
        self.name=name
        # self._price=max(price,0)
        self.__price=max(price,0)
laptop1=Laptop('hp','xxx',70000)
# print(laptop1._price)
laptop1._Laptop__price=6000
print(laptop1._Laptop__price)
print(laptop1.__dict__)

# PROPERTY / SETTER DECORATOR

class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price= max(price,0)
    @property
    def spect(self):
        return f"{self.name}{self.model} price is {self._price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def set_price(self,new_price):
        self._price=max(new_price,0)
phone1 = Phone('nokia',110,-1000)
phone1.set_price=-500  # SETTER --> SET_PRICE
print(phone1._price)   # GETTER --> PRICE
print(phone1.spect)
print(phone1.__dict__)

# INHERITANCE

class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price= max(price,0)
class Smartphone(Phone):
    def __init__(self,name,model,price,ram):
        # Phone.__init__(self,name,model,price)
        super().__init__( name,model,price)
        self.ram=ram
smart=Smartphone('nokia','xxx',7000,'6gb')
print(smart.name)
print(smart.ram)

