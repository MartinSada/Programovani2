n = int(input())
seznam = []
seznam2 = []
while n > 0:
    seznam.append(int(input()))
    n = n-1

m = int(input())
while m > 0:
    seznam2.append(int(input()))
    m = m-1

for i in seznam2:
    j=0
    while j<len(seznam):
        if (i<=seznam[j]):
            seznam.insert(j,i)
            break
        j = j+1
    if j==len(seznam):
        seznam.append(i)

p=0
while p<len(seznam):
    print(seznam[p])
    p=p+1

