class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D"