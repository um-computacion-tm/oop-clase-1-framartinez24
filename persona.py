class Person:

    def __init__(self, name: str = 'Terminator' , surname: str = 'T100' , id: int = '00000001'):           
        self.__name__= name
        self.__surname__ = surname
        self.__id__ = id

    def showData(self):
        print(f'name = {self.__name__} surname = {self.__surname__} id = {self.__id__}')