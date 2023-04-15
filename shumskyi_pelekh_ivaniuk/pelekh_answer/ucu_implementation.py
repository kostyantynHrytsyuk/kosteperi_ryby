"""
classes for Tim's and Vika's asserts
"""
class Person:
    """
    A class representing a person.

    Attributes:
    - name (str): the name of the person
    - age (int): the age of the person
    - sex (str): the sex of the person, either "male" or "female"
    - goal (str): the person's goal, e.g. "study" or "teach"
    """

    def __init__(self, name: str, age: int, sex: str, goal: str) -> None:
        """
        Initializes a Person object with the given name, age, sex, and goal.

        Raises:
        - ValueError: if any of the arguments is of an invalid
        type or if sex is not "male" or "female"
        """
        if (not isinstance(name, str) or not isinstance(age, int)
            or not isinstance(sex, str) or not isinstance(goal, str)):
            raise ValueError
        if sex not in ('male', 'female'):
            raise ValueError
        self.name = name
        self.__age = age
        self.sex = sex
        self.goal = goal

    @property
    def age(self):
        """Returns the age of the person."""
        return self.__age

    def set_age(self):
        """Sets the age of the person."""
        return 'we dont use that'

    def __str__(self) -> str:
        """Returns a string representation of the person."""
        if self.sex == 'male':
            return f'This is {self.name}. He`s {self.age} and his goal is {self.goal}'
        return f'This is {self.name}. She`s {self.age} and her goal is {self.goal}'

class Visitor(Person):
    """
    A class representing a visitor to the university.

    Attributes:
    - name (str): the name of the visitor
    - age (int): the age of the visitor
    - sex (str): the sex of the visitor, either "male" or "female"
    """

    def __init__(self, name: str, age: int, sex: str) -> None:
        """
        Initializes a Visitor object with the given name, age,
        and sex, and a default goal of "see UCU".
        """
        super().__init__(name, age, sex, 'see UCU')
        self.__age = age

class Student(Person):
    """
    A class representing a student.

    Attributes:
    - name (str): the name of the student
    - age (int): the age of the student
    - sex (str): the sex of the student, either "male" or "female"
    """

    def __init__(self, name: str, age: int, sex: str) -> None:
        """
        Initializes a Student object with the given name, age,
        and sex, and a default goal of "study".
        """
        super().__init__(name, age, sex, 'study')
        self.__age = age

class Teacher(Person):
    """
    A class representing a teacher.

    Attributes:
    - name (str): the name of the teacher
    - age (int): the age of the teacher
    - sex (str): the sex of the teacher, either "male" or "female"
    """

    def __init__(self, name: str, age: int, sex: str) -> None:
        """
        Initializes a Teacher object with the given name, age,
        and sex, and a default goal of "teach".
        """
        super().__init__(name, age, sex, 'teach')
        self.__age = age

class Classroom:
    """
    A class representing a classroom at UCU.
    """
    def __init__(self, number: int, capacity: int) -> None:
        """
        Initialize a Classroom object with a number and a capacity.

        Args:
            number (int): the number of the classroom.
            capacity (int): the maximum capacity of the classroom.

        Raises:
            ValueError: if either `number` or `capacity` is not an integer.

        """
        if not isinstance(number, int) or not isinstance(capacity, int):
            raise ValueError
        self.number = number
        self.capacity = capacity
        self.people = []
        self.register = False
        self.opportunity= []


    def __str__(self) -> str:
        """
        Return a string representation of the Classroom object.

        Returns:
            str: a string that describes the Classroom object.

        """
        return f'This is a class {self.number}'

    def registration(self, teacher: object, students: list):
        """
        Register a list of students and a teacher to the classroom.

        Args:
            teacher (object): the teacher to be registered.
            students (list): a list of students to be registered.

        Returns:
            str: a message indicating the status of the registration.

        Raises:
            ValueError: if `students` is not a list.
        """
        if not isinstance(students, list):
            raise ValueError
        if self.register:
            return 'This class is taken'
        if isinstance(teacher, Student):
            return "Student can`t do a registration"
        if not all(isinstance(std, Student) for std in students):
            return 'Students need to be a class Student object'
        if self.capacity < len(students):
            return 'This is too small classroom for all students'
        self.register = True
        self.people += students
        return "Registration is succesful"

    def add_opportunity(self, opportunity):
        """
        Add an opportunity to the classroom.

        Args:
            opportunity: the opportunity to be added to the classroom.

        """
        self.opportunity.append(opportunity)


class UCU:
    """
    a class for university
    """
    classrooms=[]
    def __init__(self) -> None:
        """
        Initialize a UCU object.

        """
        self.visitors = []
    def __str__(self) -> str:
        """
        Return a string representation of the UCU object.

        Returns:
            str: a string that describes the UCU object.

        """
        return 'This is the most beautiful university in Ukraine'
    def is_empty(self):
        """
        Check if the UCU object has any visitors.

        Returns:
            bool: True if there are no visitors, False otherwise.

        """
        return not self.visitors
    def add_person(self, __o: object):
        """
        Add a person to the UCU object.

        Args:
            __o (object): the person to be added.

        """
        self.visitors.append(__o)
    def add_class(self, classroom: object):
        """
        Add a Classroom object to the UCU object.

        Args:
            classroom (object): the Classroom object to be added.

        """
        UCU.classrooms.append(classroom)
        for i in classroom.people:
            self.visitors.append(i)

    @staticmethod
    def number_of_class():
        """
        Return the number of Classroom objects in the UCU object.

        Returns:
            int: the number of Classroom objects.

        """
        return len(UCU.classrooms)
