def citiredate():
    lst = []
    givenstring = input(" Dati datele problemei, separate prin virgula")
    numersasstring = givenstring.split(", ")
    for x in numersasstring:
        lst.append(int(x))
    return lst


'''
7. Toate nu sunt prime.
'''


def not_prime(lst: list[int]):
    for i in range(1, len(lst)):
        for d in range(2, len(lst)):
            if lst[i] % d == 0:
                return True
    return False


def get_longest_all_not_prime(lst: list[int]):
    submax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if not_prime(lst[i: j + 1]) and len(lst[i: j + 1]) > len(submax):
                submax = lst[i: j + 1]
    return submax


def test_get_longest_not_all_prime():
    assert get_longest_all_not_prime(4, 6, 8, 10, 11, 13) == "4,6,8,10"


def arithmetic_progression(lst: list[int]):
    for i in range(2, len(lst) - 1):
        if lst[i] != (lst[i - 1] + lst[i + 1]) / 2:
            return True
    return False


def get_longest_arithmetic_progression(lst: list[int]):
    """
    16. Toate numerele sunt în progresie aritmetică.
    :type lst: lista
    """
    subprogarit = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if arithmetic_progression(lst[i: j + 1]) and len(lst[i: j + 1]) > len(subprogarit):
                subprogarit = lst[i: j + 1]
    return subprogarit


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression(1, 3, 4, 5) == "1,2,3,4,5"
    assert get_longest_arithmetic_progression(1, 4, 5, 8, 11, 14, 40, 47) == "5,8,11"
    assert get_longest_arithmetic_progression(11, 13, 15, 17, 21, 25, 26) == "11,13,15,17"


def main():
    lst = []
    while True:
        print("1. Citire date.")
        print("2. Cea mai mare subsecventa de numere neprime")
        print("3. Cea mai mare subsecventa de numere in progresie aritmetica.")
        print("x. Iesire din program.")
        optiune = input("Alege optiunea")
        if optiune == "1":
            lst = citiredate()
            print("\n")
        elif optiune == "2":
            print(get_longest_all_not_prime(lst))
            print("\n")
        elif optiune == "3":
            print(get_longest_arithmetic_progression(lst))
            print("\n")
        elif optiune == "x":
            break
        else:
            print("Reincercati")


if __name__ == "__main__":
    test_get_longest_arithmetic_progression()

main()
exit(0)
