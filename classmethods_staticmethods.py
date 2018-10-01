class Employee:

    raise_amount = 1.04
    no_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emps +=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

emp_1 = Employee('Raghu','Paredla',60000)
emp_2 = Employee('Vamsi','Krishna',80000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
