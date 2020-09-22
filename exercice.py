#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0:
        nb=-number
    else:
        nb=number
    return nb


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    word_list=[]
    for k in prefixes:
        word_list.append(k + suffixe)
    return word_list



def prime_integer_summation() -> int:

    return


def factorial(number: int) -> int:
    x = 1
    for i in range(1,(number+1)):
        x *= i
    return x


def use_continue() -> None:
    for i in range(10+1):
        if i==5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    rep=[]
    for w in groups:
        if len(w) <= 3 or len(w) > 10:
            rep.append(False)
            continue
        if 25 in w :
            rep.append(True)
            continue
        if 50 in w :
            is_50 = True
        else :
            is_50 = False
        is_accepted = True
        for p in w :
            if (p < 18) or (p > 70 and is_50):
                is_accepted = False
                break
        rep.append(is_accepted)
    return [rep]




def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
