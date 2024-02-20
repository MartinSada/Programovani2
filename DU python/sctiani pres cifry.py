table = [[divmod (i+j, 10) for i in range (10)] for j in range (10)]
for row in table:
    print(row)
digits1 = [1,3,6]
digits2 = [5,6]
soucet = []
prenos = 0
from itertools import zip_longest
dvojice = list(zip_longest(reversed(digits1), reversed(digits2), fillvalue=0))
print(dvojice)
for pair in dvojice:
    c1, c2 = pair
    c1 += prenos
    prenos, suma = table[c1][c2]
    soucet.append(suma)
print(soucet.reverse())