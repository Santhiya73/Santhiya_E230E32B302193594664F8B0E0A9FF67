# 3.2  implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average)in decending order . Each student object  has the following attributes :nmae (string),roll_number (string),and cpga(float). test the function with different input lists of students .


class Student:

  
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: 
                              student.cgpa, reverse=True)

  #syntax - lambda ard:exp
    return sorted_students 


# Example usage:
students = [
    Student("Madhu", "A126", 9.9),
    Student("Shiva", "B125", 9.1),
    Student("Danush", "C124", 8.9),
    Student("Hari", "D123", 7.8),
]

sorted_students = sort_students(students)


# print the sorted list of students

for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
