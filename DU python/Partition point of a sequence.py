list = []
temp = 0

while(True):
    n = int(input())
    if (n == -1):
        break
    list.append(n)

if (len(list) ==0):
    temp = -1
else:
    max = list[0]
    listMax = [0]
    for i in range(0, len(list)):
        if (list[i]>max):
            max = list[i]
            listMax.append(i)

    min = list[-1]
    listMin = [len(list)-1]
    for j in range(len(list)-1, -1, -1):
        if(list[j]<min):
            min = list[j]
            listMin.append(j)

    listTemp = set(listMin)
    for p in listMax:
        if p in listTemp:
            temp = p
            break
        else:
            temp = -1

print(temp)
