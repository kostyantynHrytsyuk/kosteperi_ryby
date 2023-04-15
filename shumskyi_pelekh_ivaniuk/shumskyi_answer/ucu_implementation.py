"""UCU module"""

class Person:
    """Person module"""
    def __init__(self, name, age, sex, goal):
        self.name = name
        self.__age = age
        self.sex = sex
        self.goal = goal

        if (not isinstance(self.name, str) or
            not isinstance(self.__age, int) or
            not isinstance(self.goal, str)):
            raise ValueError

        if self.sex != 'male' and self.sex != 'female':
            raise ValueError

    def __str__(self):
        """str method"""
        if self.sex == "male":
            return f'This is {self.name}. He`s {self.__age} and his goal is {self.goal}'
        else:
            return f'This is {self.name}. She`s {self.__age} and her goal is {self.goal}'

    def set_age(self):
        """set person age"""
        pass

    @property
    def age(self):
        """age method"""
        return self.__age

class Visitor(Person):
    """Visitor module"""
    def __init__(self, name, age, sex, goal = 'see UCU'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Student(Person):
    """Student module"""
    def __init__(self, name, age, sex, goal = 'study'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Teacher(Person):
    """Student module"""
    def __init__(self, name, age, sex, goal = 'teach'):
        self.__age = age
        super().__init__(name, self.__age, sex, goal)

class Classroom:
    """Classroom module"""
    def __init__(self, number, capacity, people = [], register = False, opportunity = []):
        self.number = number
        self.capacity = capacity
        self.people = people
        self.register = register
        self.opportunity = opportunity
        if (not isinstance(number, int) or
            not isinstance(capacity, int)):
            raise ValueError

    def __str__(self):
        return f"This is a class {self.number}"

    def registration(self, teacher, students):
        """Register classroom"""
        if not isinstance(students, list):
            raise ValueError

        if self.register:
            return 'This class is taken'

        for student in students:
            if not isinstance(student, Student):
                return 'Students need to be a class Student object'

        if len(students) >= self.capacity - len(self.people):
            return 'This is too small classroom for all students'

        if not isinstance(teacher, Teacher):
            return "Student can`t do a registration"

        self.register = True
        self.people = students
        return "Registration is succesful"

    def add_opportunity(self, item):
        """Module to add opportunities"""
        self.opportunity.append(item)


class UCU:
    """UCU module"""
    classrooms = []
    def __init__(self):
        self.visitors = []

    def __str__(self):
        return 'This is the most beautiful university in Ukraine'

    def is_empty(self):
        """Check if there are visitors"""
        if len(self.visitors) == 0:
            return True
        return False

    def add_person(self, person):
        """Module to add person"""
        try:
            self.visitors = self.visitors + person
        except:
            self.visitors.append(person)

    def add_class(self, classroom):
        """Module to add classrooms"""
        self.classrooms.append(classroom)
        self.add_person(classroom.people)

    @staticmethod
    def number_of_class():
        return len(UCU.classrooms)
