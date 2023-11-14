
class Employee:
    def __init__(self, name, proffesion, salary):
        self.name = name
        self.proffession = proffesion
        self.salary = salary

    @staticmethod
    def employee_payment(Ammount):
        annual_payment = Ammount
        return annual_payment

    def employee_Scheduler(self, E_Info):
        employee_Info = {}
        employee_Info.update(
            {"name": self.name, "proffession": self.proffession, "salary": self.salary,
             "work_timing": E_Info[0], "net_worth": E_Info[1]})
        return employee_Info


Emp = Employee("Juda", "c. scientist", 500)
emp_sch = Emp.employee_Scheduler(["monday-friday 3h per day", 50004])
print(emp_sch)
# satic method can be called directly on class without having to call it on a class Instance
print(Employee.employee_payment(200))


# now tackling  python inheritance


class Boss(Employee):
    __keynote = ""

    def __init__(self, name, proffesion, salary, isFired):
        super().__init__(name, proffesion, salary)
        self.isFired = isFired

    @property
    def fired_emp(self):
        return self.isFired

    @fired_emp.setter
    def fired_emp(self, fired):
        self.isFired = fired
        return self.isFired

    def emp_assessment(self):
        if self.isFired == bool(True):
            self.__keynote = "the employee is still working in the enterprise"
        else:
            self.__keynote = "this employee is fired"
        return self.__keynote


Bs = Boss("Rosemon", "web developper", 400, True)
res = Bs.employee_Scheduler(["tuesday-friday 2-5h per day", 400])
print(res)
# using getter to access employee value
print(Bs.fired_emp)
print(Bs.emp_assessment())
# using setter to alter the value of the employee
Bs.fired_emp = False
print("employee status after changing the value of isFired attribute")
print(Bs.emp_assessment())
