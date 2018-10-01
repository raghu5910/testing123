class Employee:

    raise_amount = 1.04
    no_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emps +=1 # To count no of times this class is instansized
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        # self.pay = int(self.pay*1.04)
        self.pay = int(self.pay*self.raise_amount) #Here Employee.raise_amount = self.raise_amount
emp_1 = Employee('Raghu','Paredla',60000)
emp_2 = Employee('Vamsi','Krishna',80000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.__dict__) # namespace contains raise_amount
# print(emp_1.__dict__) # namespace does not contain raise_amount

Employee.raise_amount = 10.5

emp_1.raise_amount = 2.5 # emp_1 namespace contains raise_amount and it is overriding class variable
print(Employee.__dict__)
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
