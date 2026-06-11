# age = int(input("Enter your age: "))
# day = input("Enter the day of the week: ")
# if age > 18 and day in ["Monday", "Tuesday", "Thursday", "Friday", "Saturday", "Sunday"]:
#     print("Your ticket price is $12")
# elif age > 18 and day == "Wednesday":
#     print("Your ticket price is $10,You get a discount on Wednesdays of $2!")
# elif age < 18 and day in ["Monday", "Tuesday", "Thursday", "Friday", "Saturday", "Sunday"]:
#     print("Your ticket price is $8")
# elif age < 18 and day == "Wednesday":
#     print("Your ticket price is $6,You get a discount on Wednesdays of $2!")
# else:
#     print("Invalid input")

age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)