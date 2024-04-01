import sys

def bucketSort(words, position = 0):
    if len(words) < 2:
        return words

    buckets = [[] for i in range(27)]
    for word in words:
        if position < len(word):
            buckets[ord(word[position]) - ord('`')].append(word)
        else:
            buckets[0].append(word)

    sortedBuckets = []

    for i, n in enumerate(buckets):
        if len(n) > 1:
            buckets[i] = bucketSort(n, position + 1)

    for bucket in buckets:
        sortedBuckets.extend(bucket)

    return sortedBuckets

words = []
for line in sys.stdin:
    word = line.strip()
    if word == "-end-":
        break
    words.append(word)

sortedWords = bucketSort(words)
for word in sortedWords:
    print(word)

print("-end-")