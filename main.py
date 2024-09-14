'''Paskaita 30 - Užduotis 2
https://docs.google.com/document/d/1Vu7Y37257x8mshhlBB9YZ9ghHGbFKQm_icff6atXAUM/edit'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses
        self.performance = [] #List to store different courses with their grades

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course.name)
            course.add_student(self)

    def performance_report(self):
        formatted_performance = ", ".join(f"Course: {item['Course']}, Grade: {item['Grade']}" for item in self.performance)
        print(f"Student: {self.name}, {formatted_performance}")

    def record_grade(self, course, grade):
        if course.name in self.enrolled_courses:
            self.grades["Course"] = course.name
            self.grades["Grade"] = grade
            self.performance.append(self.grades)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        print(f"Courses taught by {self.name}: {self.courses}")

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        teacher.courses.append(self.name)  # Add this course to the teacher's course list
        self.lessons = []

    def add_student(self, student):
        if student.name not in self.students:
            self.students.append(student.name)
            self.attendance[student.name] = []

    def record_attendance(self, student, date, status):
        if student.name in self.students:
            self.attendance[student.name].append((date, status))

    def generate_report(self):
        report = []
        for student in self.students:
            attendance_record = self.attendance.get(student, [])
            attendance_status = [f"{date}: {status}" for date, status in attendance_record]
            result = f"Student: {student}, Attendance: {attendance_status}"
            report.append(result)
        print(", ".join(report))

    def add_lesson(self, lesson):
        self.lessons.append(lesson.topic)

    def get_lessons(self):
        print(f"Course {self.name} has lessons: {self.lessons}")

class Lesson:
    def __init__(self, course_name, topic, date, materials):
        self.course_name = course_name
        self.topic = topic
        self.date = date
        self.materials = materials

    def show_details(self):
        print(f"Course_name: {self.course_name}, topic: {self.topic}, date: {self.date}, materials: {self.materials}")

    def add_material(self, new_materials):
        self.materials = self.materials + new_materials


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
lit_teacher = Teacher("Ms. Robins", 32, "Literature")
math_course = Course("Mathematics", math_teacher)
lit_course = Course("English literature", lit_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
alice.enroll(lit_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
alice.record_grade(lit_course, "C")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report() # Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
bob.performance_report()
math_teacher.list_courses()  # Courses taught by Mr. Smith: ['Mathematics']

lesson1 = Lesson(math_course.name, "Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson(math_course.name, "Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])
lesson3 = Lesson(lit_course.name, "Renaissance literature", "2024-02-16", ["Biography of William Shakespeare, Othello"])

math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)
lit_course.add_lesson(lesson3)

math_course.get_lessons()
lit_course.get_lessons()

lesson3.show_details()

lesson2.add_material(["Geometry Textbook"])
lesson2.show_details()