from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

    def first(self):
        return self.name


p1 = Person("Mayank", 21)
p2 = Person.fromBirthYear('Mayank', 1996)
p3 = Person("Ram", 19)
p3.fromBirthYear("Ram", 1999)
print(p3.isAdult(11))

print(p1.age)
print(p2.age)

print(Person.isAdult(22))
