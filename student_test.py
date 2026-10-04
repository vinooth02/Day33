import unittest
from student import Student


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Karan", 85)

    def test_result(self):
        result = self.student.get_result()
        self.assertEqual(result, "Pass")

    def test_grade(self):
        result = self.student.get_grade()
        self.assertEqual(result, "B")

    def test_student_name(self):
        self.assertEqual(self.student.name, "Karan")

    def test_marks(self):
        self.assertEqual(self.student.marks, 85)


if __name__ == "__main__":
    unittest.main()