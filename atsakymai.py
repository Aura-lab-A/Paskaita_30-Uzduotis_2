class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        for course in self.enrolled_courses:
            grade = self.grades.get(course, "No grade yet")
            print(f"Student: {self.name}, Course: {course.name}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return [course.name for course in self.courses]

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = []
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            print(f"Student: {student.name}, Attendance: {attendance_record}")

    def add_lesson(self, lesson): # REIKETU PAUPDATINTI - PAUPDATINTA
        if isinstance(lesson, Lesson):
            self.lessons.append(lesson) # SITOJ VIETOJ LEISTU PRIDETI TIK LESSON OBJEKTA, SUFLERIS "ISINSTANCE"
        else:
            print("Lesson does not belong to class Lesson!") # JEI TAI KAZKOKIA NESAMONE KAIP "MANTAS!!!", NEPRIDET

    def get_lessons(self):
        for lesson in self.lessons:
            print(lesson.get_info()) # MES TIKIMES SITOJ VIETOJ NORMALAUS LESSON OBJEKTO, O NE MANTAS!!

class Lesson:
    def __init__(self, topic, date, resources):
        self.topic = topic
        self.date = date
        self.resources = resources

    def get_info(self):
        return f"Lesson: {self.topic}, Date: {self.date}, Resources: {self.resources}"

lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Geometry Basics", "2024-02-02", ["Geometry Textbook Chapter 1"])

# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
english_course = Course("English", math_teacher)

math_course.add_lesson(lesson1) # GERAI
math_course.add_lesson(lesson2) # GERAI
math_course.add_lesson("MANTAS!!!!!") # BLOGAI, NEGALIMA PRIDETI STRINGO, CIA NEGERAI

print(math_course.get_lessons())


alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
alice.enroll(english_course)

bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
# alice.record_grade(english_course, "A++")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
bob.performance_report()
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']