import unittest

from atributo import *
from persona import * 


# class TestSubject(unittest.TestCase):
#     def test_subject(self):
#         profesor = Profesor()
#         subject = subject("Matemáticas", [profesor])
#         self.assertEqual(materia.obtener_profesores(), [profesor])

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesor_terminator = Profesor("Terminator", "T110@Skymail.com")
        self.assertEqual(profesor_terminator.get_name(), "Terminator")


class TestProfesorEmail(unittest.TestCase):
    def test_profesor_email(self):
        profesor_terminator = Profesor("Terminator", "T110@Skymail.com")
        self.assertEqual(profesor_terminator.__email__, "T110@Skymail.com")


class TestStudentName(unittest.TestCase):
    def test_Student(self):
        student_fran = Student("fran")

        self.assertEqual(student_fran.__name__, "fran")
        subject_list = ["spaniol" , "ESI", "compu_1_the_best_one", "Math", "Lab"]
        self.assertIn(student_fran.subject() , subject_list)

        average_list = ["good", "not good", "not notgood", "missing data"]
        self.assertIn(student_fran.average() , average_list)

if __name__ == '__main__':
    unittest.main()