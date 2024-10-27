class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay

class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang

dev1 = Developer('Son', 'Minh', 400, 'Python')
dev2 = Developer('Thanh', 'La', 500, 'C#')

class Manager(Employee):
    co_salary = 1.05
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        return self.employees
    def remove(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
        return self.employees
# thay đổi nội dung  
manager1 = Manager('Phu', 'Trong', 1000, [dev1, dev2])
manager1.remove(dev2)
print(manager1.employees[0].fullname())



