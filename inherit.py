class User:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname

    def email(self):
        return f'{self.lname}{self.fname}@company.com'

    def __repr__(self):
        return f'User account: {self.fname} {self.lname} {self.email()}'

class Developer(User):
    def __init__(self, fname , lname , salary , stack):
        super().__init__(fname, lname)
        self.salary = salary
        self.stack = stack

    def email(self):
        return f'Developer mail: {self.lname}{self.stack}@example.com'

    def __repr__(self):
        return f'Developer Profile: {self.fname} {self.lname} {self.salary} {self.stack}'

dev1= Developer('willson', 'frd', '12000' , 'python')
print(dev1)
print(dev1.email())