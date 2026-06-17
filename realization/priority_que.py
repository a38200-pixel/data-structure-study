class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.order = 0

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item, priority):
        if self.is_full():
            raise OverflowError("Queue is full.")
        self.items.append((priority, self.order, item))
        self.order += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        best_index = 0
        for i in range(1, len(self.items)):
            if self.items[i][:2] < self.items[best_index][:2]:
                best_index = i

        return self.items.pop(best_index)[2]

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")

        best = min(self.items, key=lambda data: data[:2])
        return best[2]


def example():
    queue = PriorityQueue(4)
    queue.enqueue("clean desk", 3)
    queue.enqueue("submit report", 1)
    queue.enqueue("reply email", 2)
    queue.enqueue("urgent call", 1)

    print(queue.dequeue())  # submit report
    print(queue.dequeue())  # urgent call
    print(queue.dequeue())  # reply email
    print(queue.dequeue())  # clean desk


if __name__ == "__main__":
    import unittest

    class TestPriorityQueue(unittest.TestCase):
        def test_priority_order(self):
            queue = PriorityQueue(4)
            queue.enqueue("low", 3)
            queue.enqueue("high-1", 1)
            queue.enqueue("middle", 2)
            queue.enqueue("high-2", 1)

            self.assertTrue(queue.is_full())
            self.assertEqual(queue.peek(), "high-1")
            self.assertEqual(queue.dequeue(), "high-1")
            self.assertEqual(queue.dequeue(), "high-2")
            self.assertEqual(queue.dequeue(), "middle")
            self.assertEqual(queue.dequeue(), "low")
            self.assertTrue(queue.is_empty())

        def test_empty_error(self):
            queue = PriorityQueue(2)
            with self.assertRaises(IndexError):
                queue.dequeue()

        def test_full_error(self):
            queue = PriorityQueue(2)
            queue.enqueue("A", 2)
            queue.enqueue("B", 1)
            with self.assertRaises(OverflowError):
                queue.enqueue("C", 0)

    example()
    unittest.main(argv=[""], exit=False)
