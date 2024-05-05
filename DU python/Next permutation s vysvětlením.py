def next_permutation(perm):
    n = len(perm)

    # Step 1: Find the longest non-increasing suffix
    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1

    # If the entire permutation is non-increasing, there is no next permutation
    if i == 0:
        return "NEEXISTUJE"

    # Step 2: Identify the pivot
    pivot = i - 1

    # Step 3: Swap the pivot with the smallest element in the suffix that is larger than the pivot
    j = n - 1
    while perm[j] <= perm[pivot]:
        j -= 1
    perm[pivot], perm[j] = perm[j], perm[pivot]

    # Step 4: Reverse the suffix
    perm[i:] = reversed(perm[i:])

    return perm


# Read input
N = int(input())
permutation = list(map(int, input().split()))

# Get the next permutation
next_perm = next_permutation(permutation)

# Print the result
if next_perm == "NEEXISTUJE":
    print("NEEXISTUJE")
else:
    print(*next_perm)