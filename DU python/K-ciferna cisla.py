import math
def generateNumbers(k, n, currentSum, currentNum, result, temp):
    if k == 0:
        if currentSum == n:
            result.append(currentNum)
        return
    else:
        if currentNum == 0:
            startDigit = 1
        elif n>9 and temp >= 1:
            startDigit = min(temp, n-currentSum)
        else:
            startDigit = 0

        endDigit = 10 if n-currentSum>9 else n-currentSum+1

        for digit in range(startDigit, endDigit):
            generateNumbers(k - 1, n, currentSum + digit, currentNum * 10 + digit, result, temp)

result = []
k = int(input())
n = int(input())
temp = math.floor(n/k)
if n > 9 * k:
    print("Nelze dosáhnout výsledku.")
elif k == 1:
    if n <= 9:
        print(n)
    else:
        print("Nelze dosáhnout výsledku.")
else:
    generateNumbers(k, n, 0, 0, result, temp)
    print(*result)