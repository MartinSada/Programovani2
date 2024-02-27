m = 0
list = []

while (True):
    m = int(input())
    if m == 0:
        break
    list.append(m)

n = ""
for i in list:
    cifry = []
    b = True
    while i>0:
        cifry.append(i%10)
        i = i//10
    for j in range(0, len(cifry)):
        if cifry[j] != cifry[len(cifry)-j-1]:
            b = False
        if(cifry[0] == 0):
            b = False
    if (b):
        for j in cifry:
            n += str(j)
        n += " "
print(n)



