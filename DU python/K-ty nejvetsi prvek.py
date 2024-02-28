seznam = []
while True:
    cislo = int(input())
    if cislo == -1:
        break
    seznam.append(cislo)
k = int(input())

max = 0
a = 0
while True:
    for i in range(len(seznam)):
        if seznam[i] > max:
            max = seznam[i]
            a = i
    k = k-1
    if k<1:
        break
    seznam[a] = 0
    max = 0
print(max)
