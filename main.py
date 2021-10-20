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


def esteprim(x):
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
    return True


def test_esteprim():
    assert esteprim(13) is True
    assert esteprim(1) is False
    assert esteprim(2) is True


def niciunulnuesteprim (lst):
    for i in lst:
        if esteprim(i):
            return False
    return True


def test_niciunulnuesteprim():
    assert niciunulnuesteprim([6,8,9]) is True
    assert niciunulnuesteprim([1, 2, 3]) is False
    assert niciunulnuesteprim([1, 4, 8, 9]) is True


def get_longest_all_not_prime(lst):
    secvMax = []
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            if niciunulnuesteprim(lst[i: j + 1]) and len(lst[i: j + 1]) > len(secvMax):
                secvMax = lst[i: j + 1]
    return secvMax



def test_get_longest_all_not_prime():
    assert (get_longest_all_not_prime([1,2,3,4,5,6,8,10])==[6,8,10]) is True
    assert (get_longest_all_not_prime([1,3,5,7,8,9])==[5,7,8]) is False
    assert (get_longest_all_not_prime([4,5,6,8])==[6,8]) is True


'''
17. Toate numerele sunt in progresie artimetica.
'''

def prograrit(lst):
    for i in range(1,len(lst)-1):
        if lst[i] != (lst[i-1]+lst[i+1]) / 2:
            return False
    return True


def test_prograrit():
    assert prograrit([1,2,3,4,5]) is True
    assert prograrit([1,3,7]) is False
    assert prograrit([6,7,8]) is True


def get_longest_arithmetic_progression(lst):
    subarit=[]
    for i in range (len(lst)):
        for j in range (i, len(lst)):
            if prograrit(lst[i:j+1]) and len(lst[i:j+1]) > len(subarit):
                subarit= lst[i:j+1]
    return subarit


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1,2,3,4,5])==[1,2,3,4,5]
    assert get_longest_arithmetic_progression([1,2,5,6,7,9,10])==[5,6,7]
    assert get_longest_arithmetic_progression([1,4,6,9,12,15])==[6,9,12,15]




'''
10. Toate numerele sunt pare.
'''


def este_par(n):
    if n%2 == 0:
        return True
    return False


def test_este_par():
    assert este_par(2) is True
    assert  este_par(3) is False
    assert  este_par(1) is False


def toate_sunt_pare(lst):
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
    assert (get_longest_all_even([1,2,4,6]) == [2,4,6]) is True


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


if __name__ == "_main_":
    test_esteprim()
    test_niciunulnuesteprim()
    test_get_longest_all_not_prime()
    test_este_par()
    test_toate_sunt_pare()
    test_get_longest_all_even()
    test_get_longest_arithmetic_progression()
    test_prograrit()

main()
exit(0)