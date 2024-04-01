vstup = {}

def dictInversion(vstup):
    invertedDict = {}
    formerKeys = []

    for prop, sub in vstup.items():
        for s in sub:
            if s not in invertedDict:
                invertedDict[s] = []
            invertedDict[s].append(prop)
        formerKeys.append(prop)

    sortedSub = sorted(invertedDict.keys())
    for sub in sortedSub:
        keys = invertedDict[sub]
        keys.sort(key=lambda x: formerKeys.index(x))
        print(f"{sub}: {', '.join(keys)}")
    print("---")


while True:
    n = input().strip()
    if n == "---":
        break
    prop, sub = n.split(":")
    vstup[prop.strip()] = [i.strip() for i in sub.split(",")]
dictInversion(vstup)
