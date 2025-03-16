
def common_letters():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # funkcja set() tworzy zbiór unikalnych elementów
    s1 = set(str1)
    s2 = set(str2)
    print(s1)
    print(s2)

    # & zwraca wspólne elementy dwóch zbiorów
    com_let = s1 & s2
    print(com_let)

common_letters()


# Poniżej ta sama metoda, ale od zera, bez metod wbudowanych:

def common_letters_from_scratch():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    unique_letters1 = []
    unique_letter2 = []

    for char in str1:
        if char not in unique_letters1:
            unique_letters1.append(char)
    

    for char in str2:
        if char not in unique_letter2:
            unique_letter2.append(char)

    common = []
    for char in unique_letters1:
        if char in unique_letter2:
            common.append(char)