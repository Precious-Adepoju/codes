class Employee:
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@joyfieldrealestate.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('Moses', 'Ibukunoluwa', 80000)
emp_2 = Employee('Oyetola', 'Ibukunoluwa', 40000)
emp_3 = Employee('Rehoboth', 'Ibukunoluwa', 50000)

# print(emp_1)
# print(emp_2)

# print(emp_1.fullname())
# print(emp_2.fullname())
# print(Employee.fullname(emp_1))
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.__dict__)
emp_1.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_1.__dict__)

# print(Employee.num_of_employees)


class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest
    
    def value_after(self, years):
        return self.principal * (1 + (self.interest) / 100) ** years
    
    def __str__(self):
        return f"Principal is ${self.principal}, Interest rate is {self.interest}%"
Invest = Investment(10000, 5)
print(Invest)
print("Value after 2 years:", Invest.value_after(2))



