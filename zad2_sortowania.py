def f1_1(_tablica, _n, _x):  # przez wstawianie 1 5 5 4 3 2 1
    # Program musi dodatkowo (poza tablicą wynikową) wyświetlić na ekranie zawartość sortowanej
    # tablicy po każdym obiegu zewnętrznej pętli for.
    for j in range(1, _n):
        key = _tablica[j]
        i = j-1
        while i >= 0 and _tablica[i] > key: # >= bo my indeksujemy od 0
            _tablica[i+1] = _tablica[i]
            i = i-1
        _tablica[i+1] = key
        if _x:
            print(_tablica)

    return _tablica


def f1_2(_tablica, _n):  # bąbelkowe
    # Program musi dodatkowo (poza tablicą wynikową) wyświetlić na ekranie zawartość sortowanej
    # tablicy po każdym obiegu zewnętrznej pętli for.
    """for i in range(0, _n):  # staly
        for j in range(1, _n):
            if _tablica[j] < _tablica[j-1]:
                temp = _tablica[j]
                _tablica[j] = _tablica[j-1]
                _tablica[j-1] = temp
        print(_tablica)"""

    for i in range(0, _n):
        for j in range(n-1, i, -1): # od i musimy odjąć 1, a do n dodać względem cormena
            if _tablica[j] < _tablica[j - 1]:
                _tablica[j], _tablica[j - 1] = _tablica[j - 1], _tablica[j]
        print(_tablica)

    return _tablica


def f1_3(_tablica, _n):  # kubełkowe 215
    # Przed wyświetleniem wynikowej tablicy, należy wyświetlić zawartość tablicy pomocniczej (po
    # sortowaniu wewnętrznych list, w Cormenie jest to tablica B). Tablica pomocnicza powinna być
    # wyświetlona jako „lista list” (tak jak robi to funkcja print w Pythonie).
    # Na przykład tablica z rysunku 8.4 z Cormena powinna być wyświetlona jako

    # [[], [0.12, 0.17], [0.21, 0.23, 0.26], [0.39], [], [], [0.68], [0.72, 0.78], [], [0.94]]

    # Brak elementu na danej pozycji jest reprezentowany przez pustą listę ([]).

    kubelki = [[] for i in range(_n)]
    for i in range(0, _n):  # dodawanie elementów do kubełków
        kubelki[int((_n*_tablica[i])//1)].append(_tablica[i]) # tu moze by cproblem?

    for j in range(0, _n):  # Sortowanie każdego z kubełków za pomocą sortowania przez wstawianie
        f1_1(kubelki[j], len(kubelki[j]), 0)  # 3 parametr czy wyswietlac czy nie

    wynik = [i for kubelek in kubelki for i in kubelek]  # zlozenie jakby, dla każdego kubełka w
    # liście kubełków, dla każdego elementu w kubełku dodaj do listy

    """for kubelek in kubelki:
        for i in kubelek:
            wynik.append(i) """
    print(kubelki)
    return wynik


n_margeSort = 0
n_Sort = 0


def f1_4(tablica, n):  # przez scalanie
    #  Przed wyświetleniem wynikowej tablicy program wyświetla na ekranie liczbę wykonanych wywołań
    # funkcji mergeSort oraz liczbę wywołań funkcji merge. Wartość te należy wyświetlić w
    # jednej linii najpierw liczbę wywołań mergeSort, a następnie liczbę wywołań merge. Wartości
    # te należy oddzielić od siebie spacją. W liczbie wywołań mergeSort należy uwzględnić również
    # oryginalne wywołanie w celu posortowania tablicy.

    # A tablica, p,q,r indeksy, takie że: p<=q<r
    #
    # merge scala dwie tablice posortowane w jedną (bierze po pierwszym elemecnie, porównuje i mniejszy dodaje do nowej)

    global n_margeSort
    n_margeSort += 1

    if n <= 1:
        return tablica

    _srodek = n // 2  # bierzemy srodkowy (bardziej lewy)
    _l_tab = tablica[:_srodek]
    _p_tab = tablica[_srodek:]  # srodek w tej tablicy, ona bedzie dlozsza
    _l_tab = f1_4(_l_tab, len(_l_tab))
    _p_tab = f1_4(_p_tab, len(_p_tab))
    _tab = merge(_l_tab, _p_tab)
    return _tab


def merge(tab1, tab2):
    global n_Sort
    n_Sort += 1

    _tab_wy = []
    while len(tab1) and len(tab2):  # jesli sa elementy w dwóch
        if tab1[0] <= tab2[0]:
            _tab_wy.append(tab1.pop(0))
        else:
            _tab_wy.append(tab2.pop(0))
    # albo tak można, to samo tylko że za pomocą list comprehension, dobra, jednak się nie da tak
    # bo nie wiemy ile razy będziemy musieli obejść do wyczerpania jednej z listy
    # tab_wy = [_tab1.pop(0) if _tab1[0] < _tab2[0] and len(_tab1) and len(_tab2) else _tab2.pop(0) for i in range(min(len(_tab1), len(_tab2)))]

    if len(tab1):  # jeszcze w pierwszej są
        _tab_wy.extend(tab1)  # dopisujemy wszystkie pozostałe elementy
    else:
        _tab_wy.extend(tab2)
    return _tab_wy


n_partition = 0
n_quickSort = 0

# Przed wyświetleniem wynikowej tablicy program wyświetla na ekranie liczbę wykonanych wywołań funkcji quickSort
    # oraz liczbę wywołań funkcji partition. Wartość te należy wyświetlić w jednej linii najpierw liczbę wywołań
    # quickSort, a następnie liczbę wywołań partition. Wartości te należy oddzielić od siebie spacją. W liczbie
    # wywołań quickSort należy uwzględnić również oryginalne wywołanie w celu posortowania tablicy. W implementacji
    # należy zastosować metodę partycjonowania Lomuty (metoda PARTITION z Cormena).


def f1_5(tablica, p, r):  # szybkie  186
    global n_quickSort
    n_quickSort += 1
    if p < r:
        _q = partion(tablica, p, r)
        f1_5(tablica, p, _q-1)
        f1_5(tablica, _q+1, r)  # miałem n-1 :)

    return tablica


def partion(tab, p, r):
    global n_partition
    n_partition += 1  # tak samo jak ot miałem w forze :)
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1



if __name__ == '__main__':

    setup = [float(i) for i in input().split()]
    if setup[0] == -1 and setup[1] == 0:
        print("koniec")

    n = int(setup[1])
    tablica = setup[2:]
    print(tablica)

    while True:
        we = [float(i) for i in input().split()]
        if we[0] == -1 and we[1] == 0:
            print("koniec")
            break
        elif we[0] == 0 and we[1] == 0:
            print(tablica)
        else:
            tablica_kopia = tablica.copy()
            x = we[0]
            y = we[1]

            if x == 1 and y == 0:
                print(f1_1(tablica_kopia, n, 1))

            elif x == 2 and y == 0:
                f1_2(tablica_kopia, n)

            elif x == 3 and y == 0:
                print(f1_3(tablica_kopia, n))

            elif x == 4 and y == 0:
                n_margeSort = 0
                n_Sort = 0
                x = f1_4(tablica_kopia, n)
                print(n_margeSort, n_Sort)
                print(x)

            elif x == 5 and y == 0:
                n_quickSort = 0
                n_partition = 0
                x = f1_5(tablica_kopia, 0, n-1)
                print(n_quickSort, n_partition)
                print(x)
