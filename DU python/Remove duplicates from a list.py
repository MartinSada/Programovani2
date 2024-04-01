seznam = []

while True:
    n = int(input())
    if n == -1: break
    seznam.append(n)

vysledek = list(dict.fromkeys(seznam).keys())

print(vysledek)