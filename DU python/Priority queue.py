import heapq as heapque

popOut = []
heap = []
heapque.heapify(heap)

while True:
    data = input()
    if "->" in data:
        popOut.append((-(heapque.heappop(heap))))
    elif "-end-" in data:
        break
    else:
        heapque.heappush(heap, -int(data))

for i in popOut:
    print(i)
print("-end-")