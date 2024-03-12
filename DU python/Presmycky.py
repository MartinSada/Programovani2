from collections import defaultdict

def indexSlova(zadani):
    index = defaultdict(list)

    for slovo in zadani:
        soucetZnaku = defaultdict(int)

        for znak in slovo:
            soucetZnaku[znak] += 1
        key = tuple(sorted(soucetZnaku.items()))
        index[key].append(slovo)
    return index

n = int(input())
hesla = [input() for _ in range(n)]
m = int(input())
dotazy = [input() for _ in range(m)]

index = indexSlova(hesla)

for dotaz in dotazy:
    soucetZnaku = defaultdict(int)
    for znak in dotaz:
        soucetZnaku[znak] += 1

    key = tuple(sorted(soucetZnaku.items()))
    if key in index:
        print(' '.join(sorted(index[key])))
    else:
        print()






