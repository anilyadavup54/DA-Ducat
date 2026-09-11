# print(a:=10.55)

# Tuples function and methods
# len()
# min()
# max()
# .index()
# .count()

# tup=(2,3,4,5,6,7,8,9,10)
# for i in range(10):
#     print(tup[i])

# data1=(1,2,10,10,3,4,5)
# data2=('x','y','z,')
# data3=(10,20,'aman',34.5)
# data4=("a", 10,16.5)

# print(data1[0])
# print(data2[0])
# print(data3[0])
# print(data4[0])

# print(min(data1))
# print(max(data1))
# print(len(data2))
# print(data1.count(10))
# print(data1.index(10))
# print("H")



#Student Management System
student_data = [ {"name": "anil", "age": 20},
                 {"name": "aman", "age": 22},
                 {"name": "ankit", "age": 21}]
def viewdata():
    print("Student Data:\nNAME - AGE")
    for student in student_data:
        print(student.get("name"), "-", student.get("age"))

def adddata():
    name = input("Enter student name: ")
    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid age. Please enter a valid integer.")
        return
    student_data.append({"name": name, "age": age})
    student_data.sort(key=lambda x: x["name"].lower())
    print("Student added successfully.")

def removedata():
    name = input("Enter student name to remove: ")
    for student in student_data:
        if student["name"] == name:
            student_data.remove(student)
            print("Student removed successfully.")
            return
    print("Student not found.")


def searchdata():
    name = input("Enter student name to search: ").lower()
    for student in student_data:
        if student["name"] == name:
            print("Student found:", student)
            return
    print("Student not found.")




print("Welcome to the Student Management System \n")
flag=True
while flag:
    chr=int(input("1. To view student list\n 2. To add new list \n 3. To remove the data \n 4. To search th data \n 5. Exit\n"))
    flag=False
    match chr:
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
            exit()
        case _:
            print("Not Present")
    print("Do you want to continue? (y/n)")
    choice = input().lower()
    if choice == 'y':
        flag = True
    else:
        print("Thank you for using the Student Management System.")
        exit()


    


