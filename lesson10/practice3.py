class Employee:
   '''Common base class for all employees'''
   emp_count = 0
   def init(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.emp_count += 1
   
   def displayCount(self):
      return f"Total Employee {Employee.emp_count}"
   def displayEmployee(self):
      return f"Name : {self.name},  Salary: {self.salary}"

#####################################
emp1 = Employee("Liubov", 350)
emp2 = Employee("Vasyl", 600)
emp3 = Employee("Liubomyr", 270)
#######################################
print(Employee.emp_count)
print(emp1.displayCount())
print(emp3.displayEmployee())
#########################################
print(f"Employee.doc:{Employee.__doc__}")
print(f"Employee.name:{Employee.__name__}")
print(f"Employee.bases:{Employee.__bases__}")
print(f"Employee.dict:{Employee.__dict__}")