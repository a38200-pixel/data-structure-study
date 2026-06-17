class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full.")
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[0]


def example():
    queue = LinearQueue(3)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print(queue.dequeue())  # A
    print(queue.dequeue())  # B

    queue.enqueue("D")
    print(queue.dequeue())  # C
    print(queue.dequeue())  # D


if __name__ == "__main__":
    import unittest

    class TestLinearQueue(unittest.TestCase):
        def test_enqueue_dequeue(self):
            queue = LinearQueue(3)
            queue.enqueue(10)
            queue.enqueue(20)
            queue.enqueue(30)

            self.assertTrue(queue.is_full())
            self.assertEqual(queue.peek(), 10)
            self.assertEqual(queue.dequeue(), 10)
            self.assertEqual(queue.dequeue(), 20)

            queue.enqueue(40)
            self.assertEqual(queue.dequeue(), 30)
            self.assertEqual(queue.dequeue(), 40)
            self.assertTrue(queue.is_empty())

        def test_empty_error(self):
            queue = LinearQueue(2)
            with self.assertRaises(IndexError):
                queue.dequeue()

        def test_full_error(self):
            queue = LinearQueue(2)
            queue.enqueue(1)
            queue.enqueue(2)
            with self.assertRaises(OverflowError):
                queue.enqueue(3)

    example()
    unittest.main(argv=[""], exit=False)
