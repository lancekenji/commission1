import os
import sys

students = []

def add():
    print("-------- Add Student --------")
    idno = int(input("ID Number: "))
    name = input("Full Name: ")
    course = input("Course: ")
    level = input("Level: ")
    print("-----------------------------")
    
    student = {}
    student["idno"] = idno
    student["name"] = name
    student["course"] = course
    student["level"] = level
    students.append(student)
    os.system('cls')
    
    print("Student Added! ")
    main()

def find():
    print("-------- Find Student -------")
    idno = input("ID Number: ")

    print("----------- Result ----------")
    if len(students) == 0:
        print("There's no records in the student's list.")
        main()
    else:
        for x in students:
            if x["idno"] == int(idno):
                print("ID Number: "+ str(x["idno"]))
                print("Name: "+ x["name"])
                print("Course: "+ x["course"])
                print("Level: "+ x["level"])
                main()

def delete():
    print("------- Delete Student ------")
    idno = int(input("ID Number: "))

    print("----------- Result ----------")
    if len(students) == 0:
        print("There's no records in the student's list.")
        main()
    else:
        for i in range(len(students)):
            if students[i]["idno"] == idno:
                print("Student with ID Number: "+str(idno)+" has been deleted!")
                del students[i]
                main()

def display():
    print("-------- Display All --------")
    for x in students:
        print("ID Number: "+ str(x["idno"]))
        print("Name: "+ x["name"])
        print("Course: "+ x["course"])
        print("Level: "+ x["level"])
        print("-----------------------------")
    main()

def quit():
    os.system("cls")
    print("Thank you for using my system!")
    sys.exit()

def main()->None:
    print("--------- Main Menu ---------")
    print("1. Add Student")
    print("2. Find Student using idno")
    print("3. Delete Student using idno")
    print("4. Display All")
    print("0. Quit/End")
    choice = int(input("Enter Option(0..4): "))

    if choice == 1:
        add()
    elif choice == 2:
        find()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 0:
        quit()
    else:
        sys.exit("Invalid Selection! Exiting...")

if __name__=="__main__":
    main()
