# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count = 0 
# for num in numbers:
#     if num < 0:
#         print(num, "is Negative")
#     else:
#         print(num, "is Positive")
#         count += 1
# print("Total Positive numbers:", count)
    

# n = [1,2,3,4,5,6,7,8,9,10]
# sum = 0 
# for num in n:
#         if num % 2 == 0:
#             sum += num
# print("Sum of even numbers:", sum)

# number = 4
# for i in range(1, 11):
#     if i == 5:
#         continue;
#     print(number, "x" , i, "=", number * i)

# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str  

# print(reversed_str)

# x = 0
# while x < 100:
#     x += 2
# print(x)

# n = 5 
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print("Factorial of", n, "is", factorial)

# I want to find a non repeating character in a string.

# str = "shshshu"
# for char in str:
#     print(char, str.count(char))
#     if str.count(char) == 1:
#         print("First non-repeating character:", char)
#         break


# while True:
#     user = int(input("Enter a number: "))
#     if 1 <= user <= 10:
#         print("You entered:", user)
#         break
#     else:
#         print("Invalid input. Please enter a number between 1 and 10.")
    
# number = 29
# is_prime = True

# if number > 1:
#     for i in range(2,number):
#         if number % i == 0:
#             is_prime = False
#             break
# print(number, "is a prime number." if is_prime else "is not a prime number.")

# items = ["apple", "banana", "orange", "apple", "mango"]
# for i in items:
#     if items.count(i) > 1:
#         print(i, "is a duplicate.")

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
