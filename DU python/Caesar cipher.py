k = int(input())
text = list(input().lower())

def encrypt(text,k):
    for i in range(len(text)):
        if (ord(text[i]) >= 97 and ord(text[i]) <= 122):
            text[i] = chr((ord(text[i]) - 97 + k) % 26 + 97)
    text = [x.upper() for x in text]
    print(*text, sep = '')

encrypt(text, k)

