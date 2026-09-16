#OQ3zGw1zSh708lyQ
import json

# def open(file_name):
#     with open(file_name, "r") as f:
#         students = json.load(f)
from pathlib import Path

file_path = Path(__file__).parent / "Students.json"

with open("Students.json", "r") as file:
    students = json.load(file)
    
# def save(file_name):
#     with open(file_name, "w") as f:
#             json.dump(students, f, indent=4)
            
def save_dict(dict, file_name):
    with open(file_name, "w") as f:
        for key, value in dict.items():
             f.write(str(key) + "," + str(value))
    return
def read_dict(file_name):
    students = {}
    with open(file_name, "r") as f:
        for m in f:
            value = m.split(",")
            students[value[0]] = value[1].split("\n")[0]
    return students

def add_student(name):
    if name not in students:
        students[name] = {}
    else:
        print(f"Student {name} already exists.")

def add_grade(name, subject, grade):
    if name in students:
        students[name][subject] = grade
    else:
        print(f"Student {name} does not exist. Please add the student first.")

def remove_student(name):
    if name in students:
        del students[name]
        print(f"Now {name} is ex student.")
    else:
        print(f"Student {name} does not exist.")

def remove_subject(name, subject):
    if name in students:
        del students[name][subject]
        print(f"{name}`s {subject} removed.")
    else:
        print(f"Student {name} does not exist.")

def get_student_grades(name):
    return list(students.get(name, {}).items())

def get_average_grade(name):
    grades = get_student_grades(name)
    if grades:
        return sum(grade for subject, grade in grades) / len(grades)
    else:
        return None

def get_all_students():
    return students.keys()

def get_all_subjects():   
    # result = []
    # for grades in students.values():
    #     for subject in grades.keys():
    #         if subject not in result:
    #             result.append(subject)
    # return result
    return [ subject for grades in students.values() for subject in grades.keys()]

def lock():
    while True:
        username = input("Username:")
        password = input("Password:")
        if username == "":
            break
        if username == "usku" and password == "pass":
            main_thing()
        else:
            print("Username or Password wrong. Try Again")
            continue

    

def main_thing():
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Student Grades")
        print("4. Get Average Grade")
        print("5. Get All Students")
        print("6. Get All Subjects")
        print("7. Remove Student")
        print("8. Remove Grades")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)
        elif choice == "2":
            name = input("Enter student name: ")
            if name not in students:
                print(f"Student {name} does not exist. Please add the student first.")
                continue
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            add_grade(name, subject, grade)
        elif choice == "3":
            name = input("Enter student name: ")
            grades = get_student_grades(name)
            if grades:
                print(f"{name}'s grades: {grades}")
            else:
                print(f"No grades found for {name}.")
        elif choice == "4":
            name = input("Enter student name: ")
            average = get_average_grade(name)
            if average is not None:
                print(f"{name}'s average grade: {average:.2f}")
            else:
                print(f"No grades found for {name}.")
        elif choice == "5":
            students_list = get_all_students()
            print(f"All students: {list(students_list)}")
        elif choice == "6":
            all_subjects = get_all_subjects()
            print(f"All subjects: {all_subjects}")
        elif choice == "7":
            name = input("Enter students name: ")
            remove_student(name)
        elif choice == "8":
            name = input("Enter students name: ")
            if name not in students:
                print(f"Student {name} does not exist. Please add the student first.")
                continue
            subject = input("Enter students subject:")
            if subject not in get_all_subjects():
                print(f"Subject {subject} does not exist")
                continue
            remove_subject(name, subject)
        elif choice == "t":
            print(students)
        elif choice == "0":
            break
        else:
            print("Dang whaaat?")

#students = read_dict("Students.txt")
# open("Students.json")
lock()
#main_thing()
with open("Students.json", "w") as file:
    json.dump(students, file, indent=4)
# save("Student.json")
#save_dict(students, "students.txt")