def display_menu():
        print("===== STUDENT MANAGEMENT SYSTEM =====\n")
        print("1. Add Student\n")
        print("2. View Students\n")
        print("3. Search Student\n")
        print("4. Update Student\n")
        print("5. Delete Student\n")
        print("6. Exit\n")

def add_student():
       try:
            student_id = int(input("Enter Student ID: "))
            student_name = input("Enter Student Name: ")
            student_age = int(input("Enter Student Age: "))
            if not student_name.isalpha():
                  print("Invalid Name,Please Enter Valid Name:")
                  return
            student = {
            "id": student_id,
            "name": student_name,
            "age": student_age
            }
            students.append(student)
            print("Student Added Successfully")
            with open("Student.txt","a") as f:
                f.write(f"{student_id},{student_name},{student_age}\n")
            
       except ValueError:
            print("Error, Please Input a Valid Choice")
            return
def view_student():
      with open("Student.txt","r") as f:
            data = f.readlines()
      if len(data) == 0:
                print("No Students Found")
      else:
        for line in data:
            student_data = line.strip().split(",")
            print("-----------")
            print("ID: ",student_data[0])
            print("Name: ",student_data[1])
            print("Age: ",student_data[2])
            print("-------------")
def search_student():
       try:
             with open("Student.txt","r") as f:
                data = f.readlines()
             search_id = str(input("Enter Student ID to Search:"))
             found = False
             for line in data:
                students_search = line.strip().split(",")
                if search_id == students_search[0]:
                    found = True
                    print("Student Found")
                    print("ID: ",students_search[0])
                    print("Name: ",students_search[1])
                    print("Age: ",students_search[2])
                        
             if found == False:
               print("No Students Found")
       except ValueError:
              print("Error, Please Input a Valid Choice")
              return
def update_student():
    try:
        update_stu = input("Enter Student ID to Update: ")
        found = False
        updated_data = []

        with open("Student.txt", "r") as f:
            data = f.readlines()

        for line in data:
            student_data = line.strip().split(",")

            if update_stu == student_data[0]:
                found = True

                student_data[1] = input("Enter New Name: ")
                student_data[2] = input("Enter New Age: ")

                print("Student Updated Successfully")

            updated_data.append(
                f"{student_data[0]},{student_data[1]},{student_data[2]}\n"
            )

        with open("Student.txt", "w") as f:
            f.writelines(updated_data)

        if found == False:
            print("No Student Found")

    except ValueError:
        print("Error, Please Input a Valid Choice")

def delete_student():
      try:
            del_stu = input("Enter the Studen ID to Delete: ")
            found3 = False
            remaining_records = []
            with open("Student.txt", "r") as f:
                data = f.readlines()
            for line in data:
                  deleted_data = line.strip().split(",")
                  if del_stu == deleted_data[0]:
                        found3 = True
                        print("Student Deleted Successfully")
                  else:
                        remaining_records.append(f"{deleted_data[0]},{deleted_data[1]},{deleted_data[2]}\n"
            )
                  with open("Student.txt", "w") as f:
                        f.writelines(remaining_records)
            if found3 == False:
                  print("No Student Found")
      except ValueError:
            print("Error, Please Input a Valid Choice")
            return

students = []

while True:
    display_menu()
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
          print("Error, Please Input a Valid Choice")
          continue
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Thanks for Choosing Student Management System")
        break
    else:
            print("Invalid Choice")
            
    
        
