from datetime import date
class Studant:
    def __init__(self, name , age=0 ):
        self.__name=name
        self.__age = age 

    def describe(self):
        print(f"name {self.__name} and age {self.__age}")

    @classmethod 
    def inityear(cls,name,birthyear):
        return cls(name, date.today().year - birthyear)

studant1 = Studant("rami", 20)
stud2 = Studant.inityear("salh", 2003)
studant1.describe()
stud2.describe()
