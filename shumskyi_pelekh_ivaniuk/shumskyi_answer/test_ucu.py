import unittest
from ucu_implementation import *

class TestUCU(unittest.TestCase):
    def test_person(self):
        person1= Person('Danya', 34, 'male', 'go to cafee')
        self.assertTrue(hasattr(person1, 'age') == True)
        self.assertTrue(isinstance(person1, Person))
        self.assertTrue(person1.name=='Danya')
        self.assertTrue(person1.age==34)
        self.assertTrue(person1.sex=='male')
        self.assertTrue(person1.goal=='go to cafee')
        self.assertTrue(str(person1)=='This is Danya. He`s 34 and his goal is go to cafee')
        self.assertTrue(person1._Person__age == 34)

    def test_visitor(self):
        visitor1 = Visitor("John", 25, "male")
        self.assertTrue(isinstance(visitor1, Visitor))
        self.assertTrue(isinstance(visitor1, Person))
        self.assertTrue(visitor1.name == "John")
        self.assertTrue(visitor1.age == 25)
        self.assertTrue(visitor1.sex == "male")
        self.assertTrue(visitor1.goal == "see UCU")
        self.assertTrue(str(visitor1)=='This is John. He`s 25 and his goal is see UCU')
        self.assertTrue(visitor1._Visitor__age == 25)

    def test_student(self):
        student1 = Student("Alice", 20, "female")
        self.assertTrue(isinstance(student1, Student))
        self.assertTrue(isinstance(student1, Person))
        self.assertTrue(student1.name == "Alice")
        self.assertTrue(student1.age == 20)
        self.assertTrue(student1.sex == "female")
        self.assertTrue(student1.goal == "study")
        self.assertTrue(str(student1)=='This is Alice. She`s 20 and her goal is study')
        self.assertTrue(student1._Student__age == 20)

    def test_teacher(self):
        teacher1 = Teacher("Bob", 30, "male")
        self.assertTrue(isinstance(teacher1, Teacher))
        self.assertTrue(isinstance(teacher1, Person))
        self.assertTrue(teacher1.name == "Bob")
        self.assertTrue(teacher1.age == 30)
        self.assertTrue(teacher1.sex == "male")
        self.assertTrue(teacher1.goal == "teach")
        self.assertTrue(str(teacher1)=='This is Bob. He`s 30 and his goal is teach')
        self.assertTrue(teacher1._Teacher__age == 30)

    def test_classroom(self):
        classroom1 = Classroom(101, 30)
        self.assertTrue(isinstance(classroom1, Classroom))
        self.assertTrue(classroom1.number == 101)
        self.assertTrue(classroom1.capacity == 30)
        self.assertTrue(classroom1.people == [])
        self.assertTrue(classroom1.register == False)
        # self.assertTrue(classroom1.opportunity == [])
        self.assertTrue(str(classroom1)== 'This is a class 101')

    def test_UCU(self):
        # UCU object
        visitor1 = Visitor("John", 25, "male")
        ucu1 = UCU()
        self.assertTrue(str(ucu1)=='This is the most beautiful university in Ukraine')
        self.assertTrue(ucu1.is_empty()==True)
        self.assertTrue(ucu1.visitors==[])
        self.assertTrue(UCU.classrooms==[])

        # Test adding a Person object to UCU
        ucu1.add_person(visitor1)
        self.assertTrue(visitor1 in ucu1.visitors)

    def test_registration(self):
        classroom1 = Classroom(101, 30)
        student1 = Student("Alice", 20, "female")
        teacher1 = Teacher("Bob", 30, "male")
        student2 = Student("Mike", 21, "male")
        student3 = Student("Linda", 22, "female")
        result1 = classroom1.registration(teacher1, [student1, student2, student3])
        self.assertTrue(result1 == "Registration is succesful")
        self.assertTrue(classroom1.register == True)
        self.assertTrue(classroom1.people == [student1, student2, student3])

    def test_class(self):
        classroom1 = Classroom(101, 30)
        ucu1 = UCU()
        student1 = Student("Alice", 20, "female")
        teacher1 = Teacher("Bob", 30, "male")
        student2 = Student("Mike", 21, "male")
        student3 = Student("Linda", 22, "female")
        visitor1 = Visitor("John", 25, "male")

        # Add class
        classroom7 = Classroom(204, 30)
        ucu1.add_class(classroom1)
        ucu1.add_class(classroom7)
        # self.assertTrue(classroom1 in UCU.classrooms)
        # self.assertTrue(student1 in ucu1.visitors)
        # self.assertTrue(student2 in ucu1.visitors)
        # self.assertTrue(student3 in ucu1.visitors)
        # self.assertTrue(UCU.number_of_class()==2)

        # Test taken Classroom
        student4 = Student("Tom", 22, "male")
        student5 = Student("Olivia", 23, "female")
        student6 = Student("Max", 24, "male")
        result5 = classroom1.registration(teacher1, [student4, student5, student6])
        # self.assertTrue(result5=='This class is taken')

        # Test Classroom registration with non-Student objects
        classroom2 = Classroom(202, 5)
        visitor2 = Visitor("Mary", 25, "female")
        result3 = classroom2.registration(teacher1, [visitor1, visitor2])
        self.assertTrue(result3 == 'Students need to be a class Student object')
        self.assertTrue(classroom2.register == False)

        # Test Classroom registration with too many students
        student4 = Student("Tom", 22, "male")
        student5 = Student("Olivia", 23, "female")
        student6 = Student("Max", 24, "male")
        result2 = classroom2.registration(teacher1, [student1, student2, student3, student4, student5, student6])
        self.assertTrue(result2 == 'This is too small classroom for all students')

        # Test Classroom registration with non-Teacher object
        classroom3 = Classroom(303, 30)
        result4 = classroom3.registration(student1, [student2])
        self.assertTrue(result4 == "Student can`t do a registration")
        self.assertTrue(classroom3.register == False)
        self.assertTrue(classroom3.people == [])

        # Test adding opportunity to a Classroom
        classroom1.add_opportunity("use projector")
        classroom1.add_opportunity("use whiteboard")
        self.assertTrue(classroom1.opportunity == ["use projector", "use whiteboard"])




if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
