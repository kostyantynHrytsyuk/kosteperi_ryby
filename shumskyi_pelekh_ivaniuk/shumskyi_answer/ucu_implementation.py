"""UCU module"""

class Person:
    """Person module"""
    def __init__(self, name, age, sex, goal):
        self.name = name
        self.__age = age
        self.sex = sex
        self.goal = goal

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
    def __init__(self, number, capacity):
        
