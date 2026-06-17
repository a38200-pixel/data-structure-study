class LinearDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def add_front(self, item):
        if self.is_full():
            raise OverflowError("Deque is full.")
        self.items.insert(0, item)

    def add_rear(self, item):
        if self.is_full():
            raise OverflowError("Deque is full.")
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items[0]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.items[-1]


def example():
    deque = LinearDeque(4)
    deque.add_rear("B")
    deque.add_front("A")
    deque.add_rear("C")
    deque.add_front("Start")

    print(deque.delete_front())  # Start
    print(deque.delete_front())  # A
    print(deque.delete_rear())   # C
    print(deque.delete_rear())   # B


if __name__ == "__main__":
    import unittest

    class TestLinearDeque(unittest.TestCase):
        def test_add_delete(self):
            deque = LinearDeque(4)
            deque.add_rear(20)
            deque.add_front(10)
            deque.add_rear(30)
            deque.add_front(0)

            self.assertTrue(deque.is_full())
            self.assertEqual(deque.peek_front(), 0)
            self.assertEqual(deque.peek_rear(), 30)
            self.assertEqual(deque.delete_front(), 0)
            self.assertEqual(deque.delete_rear(), 30)
            self.assertEqual(deque.delete_front(), 10)
            self.assertEqual(deque.delete_rear(), 20)
            self.assertTrue(deque.is_empty())

        def test_empty_error(self):
            deque = LinearDeque(2)
            with self.assertRaises(IndexError):
                deque.delete_front()

        def test_full_error(self):
            deque = LinearDeque(2)
            deque.add_front(1)
            deque.add_rear(2)
            with self.assertRaises(OverflowError):
                deque.add_rear(3)

    example()
    unittest.main(argv=[""], exit=False)
