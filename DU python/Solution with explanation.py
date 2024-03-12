# Funkce pro získání všech přesmyček pro dané slovo
from collections import Counter


def get_anagrams(word, words):
    anagrams = []
    word_count = Counter(word)
    for w in words:
        if Counter(w) == word_count:
            anagrams.append(w)
    return anagrams

# Načtení vstupních dat
N = int(input())
dictionary = [input() for _ in range(N)]
M = int(input())
queries = [input() for _ in range(M)]

# Pro každý dotaz najděte přesmyčky
for query in queries:
    anagrams = get_anagrams(query, dictionary)
    if anagrams:
        print(' '.join(sorted(anagrams)))
    else:
        print()