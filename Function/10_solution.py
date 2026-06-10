
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# print(fact(5))

# x = 20
# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 5
#         print("Inner x:", x)
#     inner()
#     print("Outer x:", x)
# outer()

#Closure example
# def func3(x):
#     def func2(y):
#         return x ** y
#     return func2
# add5 = func3(5)
# print(add5(10))
