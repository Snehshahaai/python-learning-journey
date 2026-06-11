def even_generation(limit):
    for i in range(1, limit + 1, 2):
        yield i

for even in even_generation(10):
    print(even)