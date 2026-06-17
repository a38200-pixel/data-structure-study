class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full.")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[self.front]


def example():
    queue = CircularQueue(3)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(queue.dequeue())  # A
    queue.enqueue("D")      # rear wraps around to the first index.
    print(queue.dequeue())  # B
    print(queue.dequeue())  # C
    print(queue.dequeue())  # D


if __name__ == "__main__":
    import unittest

    class TestCircularQueue(unittest.TestCase):
        def test_enqueue_dequeue(self):
            queue = CircularQueue(3)
            queue.enqueue(10)
            queue.enqueue(20)
            queue.enqueue(30)

            self.assertTrue(queue.is_full())
            self.assertEqual(queue.dequeue(), 10)

            queue.enqueue(40)
            self.assertEqual(queue.dequeue(), 20)
            self.assertEqual(queue.dequeue(), 30)
            self.assertEqual(queue.dequeue(), 40)
            self.assertTrue(queue.is_empty())

        def test_empty_error(self):
            queue = CircularQueue(2)
            with self.assertRaises(IndexError):
                queue.dequeue()

        def test_full_error(self):
            queue = CircularQueue(2)
            queue.enqueue(1)
            queue.enqueue(2)
            with self.assertRaises(OverflowError):
                queue.enqueue(3)

    example()
    unittest.main(argv=[""], exit=False)
