from students import Student

def menu():

    while True:
        print("----------------Student Management system------------")
        print("\n 1.add student:")
        print("2.update student marks")
        print("3.Show all students")
        print("4.Exit")
        
        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print("enter valid choice 1-4")
            continue

        if choice==1:
            Student.add_student()
        elif choice == 2 :
            Student.update_student_marks()
        elif choice == 3:
            Student.show_all_students()
        elif choice == 4 :
            print("Exiting the program...")
            break

if __name__ == "__main__":
    menu()