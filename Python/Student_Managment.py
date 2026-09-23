# Student Management System
student_data=['ANIL','AMIT','ANKIT']
def viewdata():
    print("Student Data:\nNAME - AGE")
    for i in range(0, len(student_data)):
        print(student_data[i])


def adddata():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    student_data.append(name)
    print("Student added successfully.")


def removedata():
    name = input("Enter student name to remove: ").strip().lower()
    for i in range(0, len(student_data)):
        if student_data[i].lower() == name:
            student_data.remove(student_data[i])
            print("Student removed successfully.")
            return
    print("Student not found.")


def searchdata():
    name = input("Enter student name to search: ").lower()
    for i in range(0, len(student_data)):
        if student_data[i].lower() == name:
            print("Student found:", student_data[i])
            return
    print("Student not found.")


print("Welcome to the Student Management System\n")
while True:
    try:
        choice = int(input(
            "1. View student list\n"
            "2. Add new student\n"
            "3. Remove student\n"
            "4. Search student\n"
            "5. Exit\n"
            "Enter your choice: "
        ))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue

    match choice:
        case 1:
            viewdata()
        case 2:
            adddata()
        case 3:
            removedata()
        case 4:
            searchdata()
        case 5:
            print("Thank you for using the Student Management System.")
            break
        case _:
            print("Invalid choice.")

    print()



# # Student Managment System Using File Handling
# from pathlib import Path

# DATA_FILE = Path(__file__).with_name("data2.txt")

# def viewdata():
#     print("Student Data:\nNAME")
#     with DATA_FILE.open("r", encoding="utf-8") as file:
#         for student in file:
#             print(student.strip())


# def adddata():
#     name = input("Enter student name: ").strip()
#     if not name:
#         print("Name cannot be empty.")
#         return
#     contents = DATA_FILE.read_text(encoding="utf-8")
#     separator = "" if not contents or contents.endswith("\n") else "\n"
#     DATA_FILE.write_text(contents + separator + name + "\n", encoding="utf-8")
#     print("Student added successfully.")


# def removedata():
#     name = input("Enter student name to remove: ").strip().lower()
#     with DATA_FILE.open("r", encoding="utf-8") as file:
#         students = [student.strip() for student in file if student.strip()]
#     for index, student in enumerate(students):
#         if student.lower() == name:
#             students.pop(index)
#             DATA_FILE.write_text("\n".join(students) + "\n", encoding="utf-8")
#             print("Student removed successfully.")
#             return
#     print("Student not found.")


# def searchdata():
#     name = input("Enter student name to search: ").lower()
#     with DATA_FILE.open("r", encoding="utf-8") as file:
#         for student in file:
#             student = student.strip()
#             if student.lower() == name:
#                 print("Student found:", student)
#                 return
#     print("Student not found.")


# print("--------Welcome to the Student Management System--------\n")
# while True:
#     try:
#         choice = int(input(
#             "1. View student list\n"
#             "2. Add new student\n"
#             "3. Remove student\n"
#             "4. Search student\n"
#             "5. Exit\n"
#             "Enter your choice: "
#         ))
#     except ValueError:
#         print("Please enter a number from 1 to 5.")
#         continue

#     match choice:
#         case 1:
#             viewdata()
#         case 2:
#             adddata()
#         case 3:
#             removedata()
#         case 4:
#             searchdata()
#         case 5:
#             print("Thank you for using the Student Management System.")
#             break
#         case _:
#             print("Invalid choice.")

#     print()











