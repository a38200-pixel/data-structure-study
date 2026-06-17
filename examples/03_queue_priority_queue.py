from collections import deque
import heapq


def queue_example():
    q = deque()
    q.append("첫 번째 요청")
    q.append("두 번째 요청")
    q.append("세 번째 요청")

    while q:
        print("처리:", q.popleft())


def priority_queue_example():
    pq = []
    heapq.heappush(pq, (3, "일반 작업"))
    heapq.heappush(pq, (1, "긴급 작업"))
    heapq.heappush(pq, (2, "중요 작업"))

    while pq:
        priority, task = heapq.heappop(pq)
        print(priority, task)


if __name__ == "__main__":
    print("[Queue]")
    queue_example()

    print("\n[Priority Queue]")
    priority_queue_example()
