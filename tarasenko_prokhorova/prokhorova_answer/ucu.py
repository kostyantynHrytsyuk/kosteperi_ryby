"""Classes Ucu"""
class UCU:
    """Class Ucu"""
    classrooms=[]
    def __init__(self) -> None:
        self.visitors=[]
    def __str__(self):
        return 'This is the most beautiful university in Ukraine'
    @classmethod
    def number_of_class(cls):
        """Number of class"""
        return len(cls.classrooms)
    def is_empty(self):
        """Is empty"""
        if not self.visitors:
            return True
        return False
    def add_person(self, person):
        """Add person"""
        if not isinstance(person, Person):
            return 'Visitor need to be a class Visitor object'
        self.visitors.append(person)
    def add_class(self, classroom):
        """Add class"""
        if not isinstance(classroom, Classroom):
            return 'Classroom need to be a class Classroom object'
        UCU.classrooms.append(classroom)
        self.visitors+=classroom.people
class Person:
    """Class Person"""
    def __init__(self, name, age, sex, goal):
        self.name = name
        self.sex=sex
        self.goal = goal
        self.__age=age
        if not isinstance(self.age, int):
            raise ValueError('Age need to be int')
        if not isinstance(self.goal, str):
            raise ValueError('Goal need to be str')
        if not isinstance(self.name, str):
            raise ValueError('Name need to be str')
        if self.sex!="male" and self.sex!="female":
            raise ValueError('This isn`t a sex')
    @property
    def age(self):
        """age"""
        return self.__age
    @age.setter
    def set_age(self, another_age):
        self.__age=another_age
    def __str__(self):
        return f'This is {self.name}. He`s {self.age} and his goal is {self.goal}' \
            if self.sex=='male' \
    else f'This is {self.name}. She`s {self.age} and her goal is {self.goal}'
class Visitor(Person):
    """Class Visitor"""
    def __init__(self, name, age, sex):
        self.__age=age
        super().__init__(name, self.__age, sex, 'see UCU')
class Student(Person):
    """Class Student"""
    def __init__(self, name, age, sex):
        self.__age=age
        super().__init__(name, self.__age, sex, 'study')
class Teacher(Person):
    """Class Teacher"""
    def __init__(self, name, age, sex):
        self.__age=age
        super().__init__(name, self.__age, sex, 'teach')
class Classroom:
    """Class Classroom"""
    def __init__(self, number, capacity) -> None:
        self.number = number
        self.capacity = capacity
        self.people=[]
        self.register = False
        self.opportunity= []
        if not isinstance(self.number, int):
            raise ValueError('Number need to be int')
        if not isinstance(self.capacity, int):
            raise ValueError('Capacity need to be int')
    def __str__(self) -> str:
        return f'This is a class {self.number}'
    def registration(self, person, list_of_students):
        """Registration"""
        if not isinstance(list_of_students, list):
            raise ValueError('you must give a list')
        for k in list_of_students:
            if not isinstance(k, Student):
                return 'Students need to be a class Student object'
        if not isinstance(person, Teacher):
            return 'Student can`t do a registration'
        if len(list_of_students)>self.capacity:
            return 'This is too small classroom for all students'
        if self.register:
            return 'This class is taken'
        self.register=True
        self.people=list_of_students
        return 'Registration is succesful'
    def add_opportunity(self, thing):
        """Add oportunity"""
        self.opportunity.append(thing)
