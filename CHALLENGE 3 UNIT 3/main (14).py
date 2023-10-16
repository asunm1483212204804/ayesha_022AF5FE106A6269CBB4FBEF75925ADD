class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name} (Roll: {self.roll_number}, CGPA: {self.cgpa})"


def sort_students(students):
    sorted_students = sorted(students, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Test the function with sample student data
students_list = [
    Student("FB", "A801", 3.1),
    Student("AP", "B802", 3.3),
    Student("AY", "C803", 3.5),
    Student("AR", "D804", 3.7)
]

sorted_students = sort_students(students_list)

# Print the sorted students
for student in sorted_students:
    print(student)
