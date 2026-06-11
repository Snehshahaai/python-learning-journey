num = int(input("Enter a number: "))
if(num < 13):
    print("The Person is a child")
elif(num < 20 and num >= 13):
    print("The Person is a Teenager")
elif(num<60 and num>=20):
    print("The Person is an Adult")
else:
    print("The Person is a Senior Citizen")