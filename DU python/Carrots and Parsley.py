n = int(input())

S1 = 2
S2 = 3
def Sowing(n, S1, S2):

    if n == 0:
        return S1+S2
    else:
        return Sowing(n-1, S2, S1+S2)

if n == 1:
    print(S1)
elif n==2:
    print(S2)
else:
    n -= 3
    print(Sowing(n, S1, S2))