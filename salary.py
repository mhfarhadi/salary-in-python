import profile


class Person:
    salary = 5000
    count = 0
    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

        Person.count += 1

    def increase_salary(self , num):
        self.salary += num

    @classmethod
    def insert_object(cls, input_text):
        name, age , gender = input_text.split(' ')
        return cls(name , age , gender)


    def __repr__(self):
        return f'Profile: {self.name} {self.age} {self.gender} {self.salary}'

information = input('Enter Name , Age and Gender ? ')

person1 = Person('Willson', 33 , 'male')
person2 = Person('Rose', 24 , 'female')
person3 = Person.insert_object(information)

person1.increase_salary(2000)
print(person1)
print(person2)
print(person3)