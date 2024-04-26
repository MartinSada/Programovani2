def generateNumbers(k, n, currentSum, currentNum, result):
    if k == 0:
        if currentSum == n:
            result.append(currentNum)
        return
    else:
        if currentNum == 0:
            startDigit = max(1, n-currentSum-(9*(k-1)))
        else:
            startDigit = max(0, n-currentSum-(9*(k-1)))

        endDigit = 10 if n-currentSum>9 else n-currentSum+1

        for digit in range(startDigit, endDigit):
            generateNumbers(k - 1, n, currentSum + digit, currentNum * 10 + digit, result)

result = []
k, n = [int(s) for s in input().split()]

if k == 1 and n <= 9:
    print(n)
else:
    generateNumbers(k, n, 0, 0, result)
    for i in result:
        print(i)

