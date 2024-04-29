import heapq

n = int(input())

numbers = [
    int(input())
    for _ in range(n)
]

pq = []

for number in numbers:
    if number == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)

    else:
        heapq.heappush(pq, number)