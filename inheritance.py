#inheritance ->the process of inheriting the properties of the parent class 

class Person:
    def person_info(self, name,age) :
        print('inside person class')
        self.name= name
        print('Name = ',name,'Age=',age)


class Company:
    def company_info  (slef, company_name, location):
        print('Inside Comapny Class')  
        print('Name:',company_name,'Location:',location)

class Employee (Person,Company):
    def employee_info(self,salary,skill):
        super().person_info('Binod',20)
        print('Inside Employee class ')
        print('salary:',salary,'skill:',skill)

emp=Employee()
emp.person_info('jessi',28)
emp.employee_info(1200,'machine')