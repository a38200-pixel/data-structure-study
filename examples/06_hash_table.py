class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_func(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return None

    def delete(self, key):
        index = self.hash_func(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True

        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, bucket)


if __name__ == "__main__":
    ht = HashTable()
    ht.insert(10, "A")
    ht.insert(17, "B")  # 10과 같은 버킷에 저장됨
    ht.insert(24, "C")

    ht.display()
    print("17 검색:", ht.search(17))
