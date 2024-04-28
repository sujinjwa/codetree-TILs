import heapq

q = []
n = int(input())

orders = [
    input()
    for _ in range(n)
]

for order in orders:
    order = order.split()
    
    if order[0] == 'push':
        heapq.heappush(q, -int(order[1]))
    
    elif order[0] == 'size':
        print(len(q))
    
    elif order[0] == 'empty':
        print(0 if q else 1)
    
    elif order[0] == 'pop':
        print(-int(heapq.heappop(q)))
    
    else: # top
        print(-int(q[0]))