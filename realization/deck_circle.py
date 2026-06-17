class CircularDeque:
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

    def add_front(self, item):
        if self.is_full():
            raise OverflowError("Deque is full.")
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item
        self.size += 1

    def add_rear(self, item):
        if self.is_full():
            raise OverflowError("Deque is full.")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        self.rear = (self.rear - 1) % self.capacity
        item = self.items[self.rear]
        self.items[self.rear] = None
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items[self.front]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items[(self.rear - 1) % self.capacity]


def example():
    deque = CircularDeque(4)
    deque.add_rear("B")
    deque.add_front("A")
    deque.add_rear("C")
    deque.add_front("Start")

    print(deque.delete_front())  # Start
    print(deque.delete_rear())   # C

    deque.add_rear("D")          # rear wraps around if needed.
    print(deque.delete_front())  # A
    print(deque.delete_front())  # B
    print(deque.delete_front())  # D


if __name__ == "__main__":
    import unittest

    class TestCircularDeque(unittest.TestCase):
        def test_add_delete(self):
            deque = CircularDeque(4)
            deque.add_rear(20)
            deque.add_front(10)
            deque.add_rear(30)
            deque.add_front(0)

            self.assertTrue(deque.is_full())
            self.assertEqual(deque.peek_front(), 0)
            self.assertEqual(deque.peek_rear(), 30)
            self.assertEqual(deque.delete_front(), 0)
            self.assertEqual(deque.delete_rear(), 30)

            deque.add_rear(40)
            self.assertEqual(deque.delete_front(), 10)
            self.assertEqual(deque.delete_front(), 20)
            self.assertEqual(deque.delete_front(), 40)
            self.assertTrue(deque.is_empty())

        def test_empty_error(self):
            deque = CircularDeque(2)
            with self.assertRaises(IndexError):
                deque.delete_front()

        def test_full_error(self):
            deque = CircularDeque(2)
            deque.add_front(1)
            deque.add_rear(2)
            with self.assertRaises(OverflowError):
                deque.add_front(3)

    example()
    unittest.main(argv=[""], exit=False)
