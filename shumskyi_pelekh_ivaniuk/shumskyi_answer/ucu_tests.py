from ucu_implementation import *
# Test creating a Person object
person1= Person('Danya', 34, 'male', 'go to cafee')
assert hasattr(person1, 'age') == True
assert hasattr(person1, 'set_age') == True
assert isinstance(person1, Person)
assert(person1.name=='Danya')
assert(person1.age==34)
assert(person1.sex=='male')
assert(person1.goal=='go to cafee')
assert str(person1)=='This is Danya. He`s 34 and his goal is go to cafee'
assert(person1._Person__age == 34)

# Test creating a Visitor object
visitor1 = Visitor("John", 25, "male")
assert isinstance(visitor1, Visitor)
assert isinstance(visitor1, Person)
assert visitor1.name == "John"
assert visitor1.age == 25
assert visitor1.sex == "male"
assert visitor1.goal == "see UCU"
assert str(visitor1)=='This is John. He`s 25 and his goal is see UCU'
assert(visitor1._Visitor__age == 25)

# Test creating a Student object
student1 = Student("Alice", 20, "female")
assert isinstance(student1, Student)
assert isinstance(student1, Person)
assert student1.name == "Alice"
assert student1.age == 20
assert student1.sex == "female"
assert student1.goal == "study"
assert str(student1)=='This is Alice. She`s 20 and her goal is study'
assert(student1._Student__age == 20)

# Test creating a Teacher object
teacher1 = Teacher("Bob", 30, "male")
assert isinstance(teacher1, Teacher)
assert isinstance(teacher1, Person)
assert teacher1.name == "Bob"
assert teacher1.age == 30
assert teacher1.sex == "male"
assert teacher1.goal == "teach"
assert str(teacher1)=='This is Bob. He`s 30 and his goal is teach'
assert(teacher1._Teacher__age == 30)

# Test creating a Classroom object
classroom1 = Classroom(101, 30)
assert isinstance(classroom1, Classroom)
assert classroom1.number == 101
assert classroom1.capacity == 30
assert classroom1.people == []
assert classroom1.register == False
assert classroom1.opportunity == []
assert str(classroom1)== 'This is a class 101'

# UCU object
ucu1 = UCU()
assert str(ucu1)=='This is the most beautiful university in Ukraine'
assert ucu1.is_empty()==True
assert ucu1.visitors==[]
assert UCU.classrooms==[]

# Test adding a Person object to UCU
ucu1.add_person(visitor1)
assert visitor1 in ucu1.visitors

# Test Classroom registration
student2 = Student("Mike", 21, "male")
student3 = Student("Linda", 22, "female")
result1 = classroom1.registration(teacher1, [student1, student2, student3])
assert result1 == "Registration is succesful"
assert classroom1.register == True
assert classroom1.people == [student1, student2, student3]

# Add class
classroom7 = Classroom(204, 30)
ucu1.add_class(classroom1)
ucu1.add_class(classroom7)
assert classroom1 in UCU.classrooms
assert student1 in ucu1.visitors #hint - call add_person from add_class method
assert student2 in ucu1.visitors
assert student3 in ucu1.visitors
assert UCU.number_of_class()==2

# Test taken Classroom
student4 = Student("Tom", 22, "male")
student5 = Student("Olivia", 23, "female")
student6 = Student("Max", 24, "male")
result5 = classroom1.registration(teacher1, [student4, student5, student6])
assert result5=='This class is taken'

# Test Classroom registration with non-Student objects
classroom2 = Classroom(202, 5)
visitor2 = Visitor("Mary", 25, "female")
result3 = classroom2.registration(teacher1, [visitor1, visitor2])
assert result3 == 'Students need to be a class Student object'
assert classroom2.register == False

# Test Classroom registration with too many students
student4 = Student("Tom", 22, "male")
student5 = Student("Olivia", 23, "female")
student6 = Student("Max", 24, "male")
result2 = classroom2.registration(teacher1, [student1, student2, student3, student4, student5, student6])
assert result2 == 'This is too small classroom for all students'

# Test Classroom registration with non-Teacher object
classroom3 = Classroom(303, 30)
result4 = classroom3.registration(student1, [student2])
assert result4 == "Student can`t do a registration"
assert classroom3.register == False
assert classroom3.people == []

# Test adding opportunity to a Classroom
classroom1.add_opportunity("use projector")
classroom1.add_opportunity("use whiteboard")
assert classroom1.opportunity == ["use projector", "use whiteboard"]

# Test Error of Classroom
ok = False
try:
    classroom4=Classroom('bla', 30) #nubmer need to be int
except ValueError:
    ok =True
assert ok

ok = False
try:
    classroom4=Classroom(405, 'bla') #capacity need to be int
except ValueError:
    ok =True
assert ok

ok = False
classroom5=Classroom(505, 25)
try:
    classroom5.registration(teacher1, 'not list')
except ValueError:
    ok = True
assert ok

# Test error of Person
ok = False
try:
    person1= Person(5, 34, 'male', 'go to cafee') #name need to be str
except ValueError:
    ok = True
assert ok

ok = False
try:
    person1= Person('Danya', 'not int', 'male', 'go to cafee') #age need to be int
except ValueError:
    ok = True
assert ok

ok = False
try:
    person1= Person('Danya', 34, 'not male and not female', 'go to cafee') #sex need to be 'male' or 'female'
except ValueError:
    ok = True
assert ok

ok = False
try:
    person1= Person('Danya', 34, 'male', 7) #goal need to be str
except ValueError:
    ok = True
assert ok
