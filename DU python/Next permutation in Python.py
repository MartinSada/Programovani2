def nextPermutation(perm):
    n = len(perm)

    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1
    if i == 0:
        return "NEEXISTUJE"
    pivot = i - 1

    j = n - 1
    while perm[j] <= perm[pivot]:
        j -= 1
    perm[pivot], perm[j] = perm[j], perm[pivot]

    perm[i:] = reversed(perm[i:])
    return perm

n = int(input())
permutation = list(map(int, input().split()))

nextPerm = nextPermutation(permutation)

if nextPerm == "NEEXISTUJE":
    print("NEEXISTUJE")
else:
    print(*nextPerm)