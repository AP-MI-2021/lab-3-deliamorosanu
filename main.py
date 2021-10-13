def citiredate():
    lst = []
    givenstring = input(" Dati datele problemei, separate prin virgula")
    numersasstring = givenstring.split(",")
    for x in numersasstring:
        lst.append(int(x))
    return lst


'''
7. Toate nu sunt prime.
'''

def is_prime(n) -> bool:
    '''
    Determina primalitatea lui n
    :param n: nr natural
    :return: True daca n este prim, altfel False
    '''
    if int(n) < 2:
        return False
    for i in range(2, int(n) // 2 + 1):
        if int(n) % int(i) == 0: return False
    return True

def verify_all_are_prime(lst: list[int]) -> bool:
    for nr in lst:
        if is_prime(nr) == False:
            return False
    return True


def get_longest_all_prime(lst: list[int]) -> list[int]:
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if verify_all_are_prime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j + 1]
    return result


def test_get_longest_all_prime():
    assert get_longest_all_prime([1,2,3,4,5]) == [2,3]
    assert get_longest_all_prime([1,6,2,3,5,7,11]) == [2,3,5,7,11]
    assert get_longest_all_prime([6,9,10,7,6,49,56]) == [7]



def arithmetic_progression(lst: list[int]):
    for i in range(2, len(lst) - 1):
        if lst[i] != (lst[i - 1] + lst[i + 1]) / 2:
            return True
        return False
    pass

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



'''
10. Toate numerele sunt pare.
'''


def este_par(n):
    '''
    Verifica daca un numar este par
    :return:True daca numarul este par, False in caz contrar
    '''
    if n%2 == 0:
        return True
    return False


def toate_sunt_pare(lst):
    '''
    Verifica daca toate elementele din lista sunt pare
    :param lst: lista
    :return: True, daca toate elementele sunt pare, False in caz contrar
    '''
    for x in lst:
        if este_par(int(x)) is False:
            return False
    return True


def test_toate_sunt_pare():
    assert toate_sunt_pare([2,4,6,8]) is True
    assert toate_sunt_pare([1,3,6,3]) is False
    assert toate_sunt_pare([1,3]) is False


def get_longest_all_even(lst):
    lst_max = []
    for i in range(0,len(lst)):
        for j in range(i,len(lst)):
            if toate_sunt_pare(lst[i:j+1]) and (len(lst[i:j+1]) > len(lst_max)):
                lst_max = lst[i:j+1]
    return lst_max


def test_get_longest_all_even():
    assert (get_longest_all_even([2,4,5]) == [2,4]) is True
    assert (get_longest_all_even([1,2,3,5,4]) == [2,4]) is False


def main():
    lst = []
    while True:
        print("1. Citire date.")
        print("2. Cea mai mare subsecventa de numere neprime")
        print("3. Cea mai mare subsecventa de numere in progresie aritmetica.")
        print("4. Cea mai lunga subsecventa de numere pare.")
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
        elif optiune == "4":
            print(get_longest_all_even(lst))
            print("\n")
        elif optiune == "x":
            break
        else:
            print("Reincercati")


if __name__ == "__main__":
    test_get_longest_all_even()
    test_get_longest_all_prime()

main()
exit(0)
