def radixSort(numbers):
    for i in range(1,8):
        buckets = [[] for p in range(10)]
        for number in numbers:
            digit = (number//(10**(i-1))) %10
            buckets[digit].append(number)
        numbers = [number for bucket in buckets for number in bucket]
        print(*numbers)


numbers = []

while True:
    try:
        number = int(input())
        numbers.append(number)
    except (ValueError, EOFError):
        break
radixSort(numbers)

