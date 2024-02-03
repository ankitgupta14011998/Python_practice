class Employee:
        
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self): 
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'    

    def __repr__(self):
        return f"Employee('{self.first}', '{self.second}', '{self.pay}')"
