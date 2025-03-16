# list comprehension - zwięzły sposób tworzenia list w jednej linii

# standardowa pętla for
numbers = []
for i in range(10):
    numbers.append(i ** 2)  # append() to metoda w Pythonie, która służy do dodawania elementu na koniec listy.
print(numbers)

# to samo za pomocą list comprehension

numbers = [i ** 2 for i in range(10)]
print(numbers)


# Dekoratory - funkcje, które modyfikują inne funkcje

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper  # tu co ważne wrapper bez nawiasów, bo chcemy aby zwrócił funkcję, a nie wynik funkcji



@decorator
def hello():
    print("Hello")


hello()
hello = decorator(hello)


# Generatory - zwracają wartości leniwie, po jednej wartości na raz

def generator():
    for i in range(3):
        yield i  # to yield jest odpowiedzialne za to
        #print(i)

print(generator())
#generator()
print(next(generator()))

