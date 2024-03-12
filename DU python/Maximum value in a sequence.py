n = int(input())
seznam = list(map(int, input().split()))
vyskyt = []

maxCislo = max(seznam)
for i in range(len(seznam)):
    if (seznam[i] == maxCislo):
        vyskyt.append(i+1)
print(maxCislo)
print(*vyskyt)