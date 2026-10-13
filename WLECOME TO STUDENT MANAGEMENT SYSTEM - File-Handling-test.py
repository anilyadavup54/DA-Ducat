print(" ")

print("----------------------------------------------------")
print("******* WLECOME TO STUDENT MANAGEMENT SYSTEM *******")

sms=open("database.txt","a+")

def viewname():
    sms=open("database.txt","r")
    for i in sms:
        print(i)
    sms.close()

def addname():
    sms=open("database.txt","a+")
    a=input("Enter the New Student name : ")
    a=a+'\n'
    sms.write(a)
    print("Student name added")
    sms.close()

def removename():
    sms=open("database.txt","a+")
    a = input("Search Student name to Remove : ")
    a=a+'\n'
    sms.seek(0)
    rn = sms.readlines()
    if a in rn:
        rn.remove(a)
        print("Removed Student Name from List",a)
        s=''
        s = ''.join([str(i) for i in rn])
        f1 = open('database.txt','w')
        f1.write(s)
        f1.close()
    else:
        print("Student not found")
    sms.close()

def searchname():
    sms=open("database.txt","r")
    a=input("Search Student name : ")
    readfile = sms.read()
    if a in readfile:
        print("Student found",a)
    else:
        print("Student not found")
    sms.close()

while(True):
    print("----------------------------------------------------")
    print("Please choose any one options:")
    print("1. To view student list")
    print("2. To add new list")
    print("3. To remove the data")
    print("4. To serach data")
    print("5. Exit")

    ch=int(input("Enter your Choose : "))

    if ch==1:
        viewname()
    elif ch==2:
        addname()
    elif ch==3:
        removename()
    elif ch==4:
        searchname()
    elif ch==5:
        exit()
    else:
        print("Wrong Entry")

    c=input("Do you want to continue y/n :")

    if(c=="y"):
        continue
    elif(c=="n"):
        break
