class User:
    def __init__(self, name, age, salary=2000): # we can put def arg in the last only
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        return f"{self.name} is working as a user at age {self.age} with salary {self.salary} "


class SoftEng(User):
    def __init__(self, name, age, skills, salary=None):
        super().__init__(name, age)
        self.skills = skills
        self._salary = salary

    def work(self):
        return f"{self.name} is programming having skills {self.skills} at age {self.age} with salary {self.salary}"

    @property  # use _ or __ to change it privately
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, val):
        self._salary = val


class WebDev(SoftEng):
    def work(self):
        return f"{self.name} is a web developer having skills {self.skills} at age {self.age} with salary {self.salary}"


user1 = User('Pawan kumar', 25)
print(user1.work())

se = SoftEng('shekhar', 22,  'Python & DSA')
se.salary = 10
print(se.salary)

print(se.work())

wd = WebDev('kumar', 23, 'React.js & Mysql')
print(wd.work())
