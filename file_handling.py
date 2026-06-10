
# name = input("Enter the Name:")
# f = open("name.txt","a")
# f.write(f"{name}\n")
# print("Name Saved Succesfully")
# f.close()

# with open("name.txt","r") as f:
#     data = f.readlines()
# count = 1
# for items in data:
#     print(f"Students {count}:", items.strip())
#     count += 1
    
student_id = int(input("Enter the ID: "))
student_name = input("Enter the Name: ")
student_age = int(input("Enter the Age: "))

with open("student.txt", "a") as f:
    f.write(f"{student_id},{student_name},{student_age}\n")

print("Student Added Successfully")

print("\nStored Students:\n")

with open("student.txt", "r") as f:
    data = f.readlines()

for line in data:
    student_data = line.strip().split(",")

    print(
        f"ID: {student_data[0]} | "
        f"Name: {student_data[1]} | "
        f"Age: {student_data[2]}"
    )
    
    
