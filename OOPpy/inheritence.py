# Parent Class
class Employee:
    def __init__(self, empname, empage, empsalary, emprole):
        self.empname = empname
        self.empage = empage
        self.empsalary = empsalary
        self.emprole = emprole

    # Inherited method
    def displayinfo(self):
        print(f"Name: {self.empname}")
        print(f"Age: {self.empage}")
        print(f"Salary: {self.empsalary}")
        print(f"Role: {self.emprole}")

    # Method to be overridden
    def work(self):
        print("Employee is working")

# Child Class - Developer
class Developer(Employee):
    # Overriding method
    def work(self):
        print("Development Work")
    # Specialized method
    def project(self, project_name):
        print(f"Developer is developing project: {project_name}")

# Child Class - Tester
class Tester(Employee):
    # Overriding method
    def work(self):
        print("Testing Work")

    # Specialized method
    def project(self, project_name):
        print(f"Tester is testing project: {project_name}")

dev = Developer("Alice", 25, 50000, "Developer")
test = Tester("Bob", 27, 45000, "Tester")

print("---- Developer ----")
dev.displayinfo()      # inherited
dev.work()             # overridden
dev.project("Bank App")  # specialized

print("\n---- Tester ----")
test.displayinfo()     # inherited
test.work()            # overridden
test.project("E-commerce App")  # specialized