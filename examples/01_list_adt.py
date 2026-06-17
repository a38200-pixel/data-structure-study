class ArrayList:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def insert(self, pos, item):
        if self.is_full():
            raise IndexError("리스트가 가득 찼습니다.")
        if pos < 0 or pos > self.count:
            raise IndexError("삽입 위치가 올바르지 않습니다.")

        for i in range(self.count, pos, -1):
            self.items[i] = self.items[i - 1]

        self.items[pos] = item
        self.count += 1

    def delete(self, pos):
        if self.is_empty():
            raise IndexError("리스트가 비어 있습니다.")
        if pos < 0 or pos >= self.count:
            raise IndexError("삭제 위치가 올바르지 않습니다.")

        removed = self.items[pos]

        for i in range(pos, self.count - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.count - 1] = None
        self.count -= 1
        return removed

    def get_entry(self, pos):
        if pos < 0 or pos >= self.count:
            raise IndexError("위치가 올바르지 않습니다.")
        return self.items[pos]

    def display(self):
        print(self.items[:self.count])


if __name__ == "__main__":
    arr = ArrayList(5)
    arr.insert(0, "A")
    arr.insert(1, "B")
    arr.insert(1, "C")
    arr.display()

    print("삭제:", arr.delete(1))
    arr.display()
