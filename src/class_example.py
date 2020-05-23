# !/usr/bin/python3


class Employee:
    """Common base class for all employees"""
    _emp_count = 0   # private static variable of the class

    def __init__(self, name, salary):
        # these two are instance variables
        self.name = name
        self.salary = salary
        Employee._emp_count += 1

    @staticmethod
    def display_count():
        print("Total Employee %d" % Employee._emp_count)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.display_employee()
emp2.display_employee()
print("Total Employee", Employee._emp_count)   # not a good practice
Employee.display_count()


