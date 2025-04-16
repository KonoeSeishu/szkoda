import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None
    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)
        
    class School:
        def __init__(self, name, city):
            self.name = name
            self.city = city
            self.studentList = []
            self.fieldsOfStudy = []
            
        def addStudent(self, student):
            if isinstance(student, Student):
                self.studentList.append(student)
                student.schoolName = self.name
                student.fieldOfStudy = random.choice(self.fieldsOfStudy)
                
        def printSchoolInfo(self):
            print(f"")