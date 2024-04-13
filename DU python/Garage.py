from collections import deque

def garageSum(n,m,coefs, weights, arrDep):
    garage = [None]*n
    totalCost = 0
    parked = [None]*(m+1)
    que = deque()

    for i in range(2*m):
        action = arrDep[i]
        carIndex = abs(action)
        carWeight = weights[carIndex]

        if action >0:
            if que:
                que.append(carIndex)
            else:
                for j in range(n):
                    if garage[j]==None:
                        garage[j]=carIndex
                        totalCost += coefs[j]*carWeight
                        parked[carIndex] = j
                        break
                if parked[carIndex] == None:
                    que.append(carIndex)

        else:
            j = parked[carIndex]
            garage[j] = None
            parked[carIndex] = None

            if que:
                carIndex = que.popleft()
                garage[j] = carIndex
                totalCost += coefs[j] * (weights[carIndex])
                parked[carIndex] = j

    print(totalCost)


n, m = [int(s) for s in input().split()]
n = int(n)
m = int(m)
coefs = []
weights = []
arrDep = []

for i in range(n):
    coefs.append(int(input()))
weights.append(None)
for i in range(m):
    weights.append(int(input()))

for i in range(2*m):
    arrDep.append(int(input()))

garageSum(n,m,coefs, weights, arrDep)