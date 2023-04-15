"""an implementation of ucu"""
class Person:
    """a class for a person"""
    def __init__(self, name, age, sex, goal):
        self.name = name
        self.__age = age
        self.sex = sex
        self.goal = goal
        if not (isinstance(name, str) and isinstance(age, int) and isinstance(goal, str)):
            raise ValueError
        if sex not in ['male', 'female']:
            raise ValueError

    @property
    def age(self):
        """the age of the person"""
        return self.__age

    @age.setter
    def set_age(self, given_age):
        self.__age = given_age

    def __str__(self):
        if self.sex == 'male':
            return f'This is {self.name}. He`s {self.age} and his goal is {self.goal}'
        return f'This is {self.name}. She`s {self.age} and her goal is {self.goal}'

class Visitor(Person):
    """a class for a visitor"""
    def __init__(self, name, age, sex, goal = 'see UCU'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Student(Person):
    """a class for a student"""
    def __init__(self, name, age, sex, goal = 'study'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Teacher(Person):
    """a class for a teacher"""
    def __init__(self, name, age, sex, goal = 'teach'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Classroom():
    """a class for a classroom"""
    def __init__(self, number, capacity, people = [], register = False, opportunity = []):
        self.number = number
        self.capacity = capacity
        self.people = []
        self.register = register
        self.opportunity = opportunity
        if not (isinstance(number, int) and isinstance(capacity, int) \
and isinstance(register, bool)):
            raise ValueError

    def __str__(self):
        return f'This is a class {self.number}'

    def registration(self, teacher, students):
        """a method for a registration"""
        if not isinstance(students, list):
            raise ValueError
        if self.register:
            return 'This class is taken'
        if isinstance(teacher, Teacher):
            if all(isinstance(student, Student) for student in students):
                if len(students) <= self.capacity - len(self.people):
                    self.people += students
                    self.register = True
                    return 'Registration is succesful'
                return 'This is too small classroom for all students'
            return 'Students need to be a class Student object'
        return "Student can`t do a registration"

    def add_opportunity(self, opp):
        """adding an opportunity method"""
        self.opportunity.append(opp)

class UCU():
    """an implementation of ucu"""
    classrooms = []
    visitors = []

    def __init__(self):
        pass

    def __str__(self):
        return f'This is the most beautiful university in Ukraine'

    def add_person(self, person):
        """a method for adding a person"""
        try:
            self.visitors = self.visitors + person
        except Exception:
            self.visitors.append(person)

    def add_class(self, classroom):
        """a method for adding a classroom"""
        self.classrooms.append(classroom)
        self.add_person(classroom.people)

    def is_empty(self):
        """a method for checking if the class is empty"""
        return len(self.visitors) == 0

    @classmethod
    def number_of_class(cls):
        """a method for getting the number of classrooms"""
        return len(cls.classrooms)
