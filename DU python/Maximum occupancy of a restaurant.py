k = int(input())

temp = 0
list = []
maxNumber = 0

while True:
    n = input()
    if "-end-" in n:
        break
    else:
        n = int(n)
        if len(list)<k:
            list.append(n)
        else:
            list.pop(0)
            list.append(n)
        temp = 0
        for i in list:
            temp = temp + i
        if temp > maxNumber:
            maxNumber = temp

print(maxNumber)
