import unittest
from ucu_implementation import *

class TestPerson(unittest.TestCase):

    def test_valid_arguments(self):
        p = Person("John", 25, "male", "study")
        self.assertEqual(p.name, "John")
        self.assertEqual(p.age, 25)
        self.assertEqual(p.sex, "male")
        self.assertEqual(p.goal, "study")
        self.assertEqual(p.set_age(), 'we dont use that')


    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            p = Person("John", "25", "male", "study")
        with self.assertRaises(ValueError):
            p = Person("John", 25, "man", "study")

    def test_str(self):
        student1 = Person("Alice", 20, "female", "study")
        self.assertEqual(str(student1), 'This is Alice. She`s 20 and her goal is study')
        person1= Person('Danya', 34, 'male', 'go to cafee')
        self.assertEqual(str(person1), 'This is Danya. He`s 34 and his goal is go to cafee')



class TestVisitor(unittest.TestCase):

    def test_valid_arguments(self):
        v = Visitor("Jane", 30, "female")
        self.assertEqual(v.name, "Jane")
        self.assertEqual(v.age, 30)
        self.assertEqual(v.sex, "female")
        self.assertEqual(v.goal, "see UCU")

class TestStudent(unittest.TestCase):

    def test_valid_arguments(self):
        s = Student("Jack", 20, "male")
        self.assertEqual(s.name, "Jack")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.sex, "male")
        self.assertEqual(s.goal, "study")

class TestTeacher(unittest.TestCase):

    def test_valid_arguments(self):
        t = Teacher("Sarah", 40, "female")
        self.assertEqual(t.name, "Sarah")
        self.assertEqual(t.age, 40)
        self.assertEqual(t.sex, "female")
        self.assertEqual(t.goal, "teach")

class TestClassroom(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("Tom", 35, "male")
        self.student1 = Student("Amy", 20, "female")
        self.student2 = Student("Bob", 22, "male")
        self.small_classroom = Classroom(101, 2)
        self.large_classroom = Classroom(201, 3)

    def test_str(self):
        classroom1 = Classroom(101, 30)
        self.assertEqual(str(classroom1), 'This is a class 101')

    def test_valid_arguments(self):
        self.assertEqual(self.small_classroom.number, 101)
        self.assertEqual(self.small_classroom.capacity, 2)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            c = Classroom("101", 1)
        with self.assertRaises(ValueError):
            c = Classroom(101, "1")
        with self.assertRaises(ValueError):
            result = self.small_classroom.registration(self.teacher, {self.student1, self.student2})

    def test_opportunity(self):
        self.large_classroom.add_opportunity("use projector")
        self.large_classroom.add_opportunity("use whiteboard")
        self.assertEqual(self.large_classroom.opportunity, ["use projector", "use whiteboard"])

    def test_registration(self):
        result = self.small_classroom.registration(self.teacher, [self.student1, self.student2])
        self.assertEqual(result, "Registration is succesful")
        result1 = self.small_classroom.registration(self.teacher, [self.student1])
        self.assertEqual(result1, 'This class is taken')
        self.assertTrue(self.small_classroom.register)
        self.assertIn(self.student1, self.small_classroom.people)
        self.assertIn(self.student2, self.small_classroom.people)

    def test_invalid_registration(self):
        result = self.small_classroom.registration(self.student1, [self.student2])
        self.assertEqual(result, "Student can`t do a registration")
        result = self.small_classroom.registration(self.teacher, [self.teacher])
        self.assertEqual(result, 'Students need to be a class Student object')
        result = self.small_classroom.registration(self.teacher, [self.student1, self.student2, Student("Mary", 23, "female")])
        self.assertEqual(result, 'This is too small classroom for all students')
        self.assertFalse(self.small_classroom.register)

class TestUCU(unittest.TestCase):
    def setUp(self):
        self.ucu = UCU()

    def test_str(self):
        self.assertEqual(str(self.ucu), 'This is the most beautiful university in Ukraine')

    def test_is_empty_when_empty(self):
        self.assertTrue(self.ucu.is_empty())

    def test_is_empty_when_not_empty(self):
        self.ucu.add_person('John')
        self.assertFalse(self.ucu.is_empty())

    def test_add_person(self):
        self.ucu.add_person('John')
        self.assertEqual(self.ucu.visitors, ['John'])

    def test_add_class(self):
        class_mock = type('ClassMock', (object,), {'people': ['John', 'Jane']})()
        self.ucu.add_class(class_mock)
        self.assertEqual(UCU.classrooms, [class_mock])
        self.assertEqual(self.ucu.visitors, ['John', 'Jane'])

    def test_number_of_class(self):
        class_mock1 = type('ClassMock', (object,), {})()
        class_mock2 = type('ClassMock', (object,), {})()
        UCU.classrooms = [class_mock1, class_mock2]
        self.assertEqual(UCU.number_of_class(), 2)


if __name__ == '__main__':
    unittest.main()
