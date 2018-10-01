class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Raghu','Paredla',60000)
emp_2 = Employee('Vamsi','Krishna',80000)

# emp_1.first = 'Raghu'
# emp_1.last = 'Paredla'
# emp_1.pay = 60000
# emp_1.email = raghu.paredla@company.com

# print('{} {}'.format(emp_1.first,emp_1.last))
print(emp_1.fullname())
# print(emp_2.fullname())
print(Employee.fullname(emp_2))
