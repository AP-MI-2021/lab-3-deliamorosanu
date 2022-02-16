'''
Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2..
    :param : un numar natural
    :return: un număr dat din baza 2 în baza 16
'''
def get_base_16_from_2(n):
    form = "0123456789ABCDEF"
    nr_16 = ""
    nr_10 = 0
    put = 1
    numar = int(n)
    while numar != 0:
        cifra = numar % 10
        nr_10 = nr_10 + cifra * put
        put = put * 2
        numar = numar // 10
    while nr_10 != 0:
        i = nr_10 % 16
        nr_16 = form[i] + nr_16
        nr_10 = nr_10 // 16
    return nr_16


'''
Calculează combinări de n luate câte k (n și k date).
    :param n: un numar natural
    :param k: un numar natural
    :return: combinări de n luate câte k 
'''
def get_n_choose_k_v1(n: int, k: int):
    import math
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))
def test_get_n_choose_k():
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(7, 4) == 35
    assert get_n_choose_k(5, 2) == 10
'''
sau
'''
def factorial(n: int):
    p = 1
    for i in range(1, n + 1):
        p = p * i
    return p
def get_n_choose_k(n: int, k: int):
    return factorial(n) // (factorial(n - k) * factorial(k))


'''
Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, `233` este superprim,
 deoarece `2`, `23` și `233` sunt toate prime, dar `237` nu este superprim, deoarece `237` nu este prim. 
    :param n: un numar natural
    :return: True/False
'''

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def is_superprime(n):
    if n < 2:
        return False
    while n > 0:
        if n < 2:
            return False
        if isPrime(n) == False:
            return False
        n = n // 10
    return True
def test_is_superprime():
    assert is_superprime(23) is True
    assert is_superprime(88) is False
    assert is_superprime(55) is False


def main():
    while True:
        print("1. Transformarea unui numar din baza 2 in baza 16.")
        print("2. Combinari de n luate cate k.")
        print("3. Determina daca este supeprim.")
        print("4. Iesire din program.")
        optiune = input("Alege optiunea")
        if optiune == "1":
            n = int(input("Dati numarul n:"))
            print(get_base_16_from_2(n))
            print("\n")
        elif optiune == "2":
            n = int(input("dati numarul n:"))
            k = int(input("Dati numarul k:"))
            print(f"Combinari de n luate cate k este: {get_n_choose_k(n, k)}")
            print("\n")
        elif optiune == "3":
            nr = int(input("Dati numarul"))
            print(is_superprime(nr))
        elif optiune == "4":
            break
        else:
            print("Reincercati")


if __name__ == "main":
    test_get_n_choose_k()
    test_is_superprime()

main()