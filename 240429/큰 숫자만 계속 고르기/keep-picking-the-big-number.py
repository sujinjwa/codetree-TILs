import heapq

# n : 숫자 개수, m : 연산 반복 횟수
n, m = tuple(map(int, input().split()))

# numbers : n개의 숫자들
numbers = list(map(int, input().split()))

pq = []
for number in numbers:
    heapq.heappush(pq, -number)

for _ in range(m):
    # 1. 최대를 골라 1 빼줌
    max_num = -heapq.heappop(pq)
    max_num -= 1

    # 2. 1 빼준 값 다시 push
    heapq.heappush(pq, -max_num)

# 최종 최댓값 출력
print(-pq[0])