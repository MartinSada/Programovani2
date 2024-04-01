def garageSum(n,m,coefs, weights, arrDep):
    garage = [None]*n
    totalCost = 0
    parked = [None]*m
    que = []

    for i in range(2*m):
        action = arrDep[i]
        carIndex = abs(action)
        carWeight = weights[carIndex-1]

        if action >0:
            for j in range(n):
                if garage[j]==None:
                    garage[j]=carIndex
                    totalCost += coefs[j]*carWeight
                    parked[carIndex-1] = True
                    break

            if parked[carIndex-1] == False:
                que.append(carIndex)

        else:
            if (parked[carIndex-1]):
                for j in range(n):
                    if garage[j]==carIndex:
                        garage[j]=None
                        parked[carIndex-1] = False
                        if len(que)>0:
                            garage[j] = que[0]
                            totalCost += coefs[j] * (weights[que[0] - 1])
                            parked[que[0] - 1] = True
                            que.pop(0)
                        break

    print(totalCost)


n, m = input().strip().split(" ")
n = int(n)
m = int(m)
coefs = []
weights = []
arrDep = []

for i in range(n):
    coefs.append(int(input()))
for i in range(m):
    weights.append(int(input()))

for i in range(2*m):
    arrDep.append(int(input()))

garageSum(n,m,coefs, weights, arrDep)