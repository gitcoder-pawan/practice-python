class User:
    def __init__(self, name, mob_no):
        self._name=name
        self._mob_no=mob_no
    def show_details(self):
        self._name=10
        self._mob_no="x"
        return  f"{self._name *2} {self._mob_no}"

class Employee(User):
    def __init__(self, name, mob_no, eid):
        super().__init__(name, mob_no)
        self.eid=eid
    def show_details(self):
        return f"{self.eid} : {self._name} - {self._mob_no}"

user1=User('pawan kumar ', 6205244673)
emp1=Employee('pawan kumar', 6205244673,1)
print(dir(user1))
print(user1.show_details())
print(emp1.show_details())