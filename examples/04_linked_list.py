class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        self.head = Node(data, self.head)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.link is not None:
            current = current.link

        current.link = new_node

    def delete(self, data):
        current = self.head
        prev = None

        while current is not None:
            if current.data == data:
                if prev is None:
                    self.head = current.link
                else:
                    prev.link = current.link
                return True

            prev = current
            current = current.link

        return False

    def display(self):
        current = self.head
        values = []

        while current is not None:
            values.append(current.data)
            current = current.link

        print(values)


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.insert_front(5)
    ll.display()

    ll.delete(20)
    ll.display()
