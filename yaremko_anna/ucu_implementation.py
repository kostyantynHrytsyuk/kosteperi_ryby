"""task for add. marks"""

class Person:
    """
    Main class
    """
    def __init__(self, name, age, sex, goal) -> None:
        if not (
            isinstance(name, str) and
            isinstance(age, int) and
            isinstance(sex, str) and
            (sex == 'male' or sex == 'female') and
            isinstance(goal, str)
        ):
            raise ValueError
        self.name = name
        self.__age = age
        self.sex = sex
        self.goal = goal
    
    @property
    def age(self):
        return self.__age

    def set_age(self):
        return self.__age
        
    def __str__(self):
        sex1, sex2 = ('He', 'his') if self.sex == 'male' else ('She', 'her')
        return f'This is {self.name}. {sex1}`s {self.age} and {sex2} goal is {self.goal}'
    
class Visitor(Person):
    """
    Subclass
    """

    def __init__(self, name, age, sex, goal="see UCU") -> None:
        super().__init__(name, age, sex, goal)
        self.__age = age

class Student(Person):
    """
    Subclass
    """

    def __init__(self, name, age, sex, goal="study") -> None:
        super().__init__(name, age, sex, goal)
        self.__age = age

class Teacher(Person):
    """
    Subclass
    """

    def __init__(self, name, age, sex, goal="teach") -> None:
        super().__init__(name, age, sex, goal)
        self.__age = age

class Classroom:
    """
    Main class
    """

    def __init__(self, number, capacity) -> None:
        if not (isinstance(number, int) and isinstance(capacity, int)):
            raise ValueError
        self.number = number
        self.capacity = capacity
        self.people = []
        self.register = False
        self.opportunity = []

    def __str__(self) -> str:
        return f'This is a class {self.number}'
    
    def registration(self, teacher, students):
        if not isinstance(students, list):
            raise ValueError
        if self.register:
            return 'This class is taken'
        for stud in students:
            if not isinstance(stud, Student):
                return 'Students need to be a class Student object'
        if len(students) > self.capacity:
            return 'This is too small classroom for all students'
        if not isinstance(teacher, Teacher):
            return "Student can`t do a registration"
        for stud in students:
            self.people.append(stud)
        self.register = True
        return "Registration is succesful"

    def add_opportunity(self, opportunity):
        self.opportunity.append(opportunity)

    
class UCU:
    """
    Main class
    """
    classrooms = []
    number = 0

    def __init__(self) -> None:
        self.visitors = []

    def __str__(self) -> str:
        return 'This is the most beautiful university in Ukraine'
    
    def add_person(self, person):
        if isinstance(person, list):
            for pers in person:
                self.visitors.append(pers)
        else:
            self.visitors.append(person)
    
    def is_empty(self):
        return True if self.visitors == [] else False
    
    def add_class(self, classroom):
        self.add_person(classroom.people)
        UCU.classrooms.append(classroom)
        UCU.number += 1
    
    @classmethod
    def number_of_class(cls):
        return cls.number