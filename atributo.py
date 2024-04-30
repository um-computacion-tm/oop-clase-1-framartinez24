import random

class Profesor:

    def __init__(self, atribute_name, atribute_email):
        self.__name__ = atribute_name
        self.__email__ = atribute_email

    def get_name(self):
        return self.__name__
    

profesor_terminator = Profesor("Terminator", "T110@Skymail.com")

profesor_robocop = Profesor("Robocop", "fae.martinez@NewYork.com")

print(f'Profesor to be arrested data:', profesor_robocop.get_name())

class Student:

    def __init__(self, atribute_name):
        self.__name__ = atribute_name
        self.__subject__ = None
        self.__average__ = None

    def get_name(self):
        return self.__name__

    def subject(self):
        subject_list = ["spaniol" , "ESI", "compu_1_the_best_one", "Math", "Lab"]
        self.__subject__ = random.choice(subject_list)
        return self.__subject__

    def average(self):
        average_list = ["good", "not good", "not notgood", "missing data",]
        self.__average__ = random.choice(average_list)
        return self.__average__

student_fran = Student("fran")
student_fran.average()
student_fran.subject()
print(f'Student data: name',student_fran.get_name(),'averga' ,student_fran.average(), 'Favorite subject',  student_fran.subject())
