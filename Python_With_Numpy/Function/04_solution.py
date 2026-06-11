radius = int(input("Enter the radius of the circle: "))

def circle(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return area, circumference
area , circumference = circle(radius)
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)