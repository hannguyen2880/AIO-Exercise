from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob
    
    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")
    
class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__list_of_people = list()

    def add_person(self, person:Person):
        self.__list_of_people.append(person)

    def count_doctor(self):
        cnt = 0
        for person in self.__list_of_people:
            if isinstance(person, Doctor): cnt += 1
        return cnt
    
    def compute_average(self):
        count_teacher = 0
        total_year = 0

        for person in self.__list_of_people:
            if isinstance(person, Teacher):
                count_teacher += 1
                total_year += person.get_yob()
        return total_year / count_teacher
    
    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__list_of_people:
            person.describe()

    def sort_age(self):
        self.__list_of_people.sort(key=lambda x: x.get_yob(), reverse=True)
