class User:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def show_details(self):
        self._name = 10
        self.age = "x"
        return f"{self._name *2} {self.age}"

    def __repr__(self):
        return f"{self._name} -- {self.age}"

    def __str__(self, ):
        return f"name={self._name } age={self.age } "

    def __add__(self, other):
        if type(other) == type(self._name):
            self._name += other
        if type(other) == type(self.age):
            self.age += other
        # return f"name={self._name} age={self.age} "
        return self.show(other)

    @staticmethod
    def show(arg):
        return f"name=pawan age={arg+200} show method called"


user1 = User("pawan", 20)
# print(user1+20+"pawan" + " kumar")
print(user1+10+"10")

