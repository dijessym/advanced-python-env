# ===== DILYAZ STYLE =====

class Person:
    def __init__(self, dname, dage):
        self._dname = dname      # encapsulation (protected)
        self._dage = dage

    def get_info(self):
        return f"Name: {self._dname}, Age: {self._dage}"


class Student(Person):
    def __init__(self, dname, dage, dstudent_id):
        super().__init__(dname, dage)   # inheritance
        self._dstudent_id = dstudent_id

    def get_info(self):   # method overriding (polymorphism)
        return f"Student: {self._dname}, Age: {self._dage}, ID: {self._dstudent_id}"


# Demonstration
dperson = Person("Aida", 30)
dstudent = Student("Dilyaz", 18, "S123")

print(dperson.get_info())
print(dstudent.get_info())
