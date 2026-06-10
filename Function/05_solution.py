name = input("Enter your name: ").strip()

def greet(name="Guest"):
    if not name:
        name = "Guest"
    return "Hello, " + name + '!'

print(greet(name))