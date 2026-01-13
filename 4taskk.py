# ===== DILYAZ STYLE =====

class Employee:
    def __init__(self, dsalary):
        self._salary = dsalary   # private/protected attribute

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, dsalary, dbonus):
        super().__init__(dsalary)
        self._dbonus = dbonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._dbonus


def print_employees(demployees):
    for demployee in demployees:
        print(demployee.get_role(), "-", demployee.get_salary())


# Demonstration
demp1 = Employee(200000)
demp2 = Manager(300000, 50000)

dlist = [demp1, demp2]
print_employees(dlist)
