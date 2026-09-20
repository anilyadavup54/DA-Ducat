# Student Management System
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("data2.json")


def load_data():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(student_data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(student_data, file, indent=4)


student_data = load_data()


def viewdata():
    print("Student Data:\nNAME - AGE")
    for student in student_data:
        print(student["name"], "-", student["age"])


def adddata():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid age. Please enter a valid integer.")
        return
    student_data.append({"name": name, "age": age})
    student_data.sort(key=lambda x: x["name"].lower())
    save_data(student_data)
    print("Student added successfully.")


def removedata():
    name = input("Enter student name to remove: ").strip().lower()
    for student in student_data:
        if student["name"].lower() == name:
            student_data.remove(student)
            save_data(student_data)
            print("Student removed successfully.")
            return
    print("Student not found.")


def searchdata():
    name = input("Enter student name to search: ").lower()
    for student in student_data:
        if student["name"].lower() == name:
            print("Student found:", student)
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





