import sys
import re
from collections import defaultdict, Counter
from operator import itemgetter

def nejcastejsiVyskyt(txt):
    slova = re.findall(r'\b[a-zA-Z]+\b', txt.lower())
    delkySlov = defaultdict(list)
    pocetSlov = Counter(slova)

    for slovo in slova:
        length = len(slovo)
        delkySlov[length].append(slovo)

    delkaSeznamu = sorted(delkySlov.items(), key=itemgetter(0), reverse=True)
    nejcastejsiSlova = {}

    for delka, seznam in delkaSeznamu:
        pocetVyskytu = Counter(seznam).most_common()
        nejcastejsiSlova[delka] = pocetVyskytu

    return nejcastejsiSlova


def vypisVysledky(nejcastejsiSlova):
    vystup = []
    for delka in sorted(nejcastejsiSlova.keys()):
        vyskyt = nejcastejsiSlova[delka]
        nejvyssiPocet = vyskyt[0][1]
        mostCommon = [slovo for slovo, pocet in vyskyt if pocet == nejvyssiPocet]

        vystup.append(f"length {delka}: {' '.join(sorted(mostCommon))} ({nejvyssiPocet} {'occurrence' if nejvyssiPocet == 1 else 'occurrences'})")
    return "\n".join(vystup)

lines = sys.stdin.readlines()
text = " ".join(lines).casefold()

nejcastejsiSlova = nejcastejsiVyskyt(text)
vystup = vypisVysledky(nejcastejsiSlova)
print(vystup)
