class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Negative index not allowed...")

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(index - 1):
                if current_node is None:
                    raise IndexError("Index out of range...")
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def remove(self):
        if self.head is None:
            raise ValueError("LinkedList is empty...")
        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next and current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def view_elements(self):
        if self.head is None:
            raise ValueError("LinkedList is empty...")

        current_node = self.head
        while current_node:
            if current_node.next:
                print(current_node.value, end=' -> ')
            else:
                print(current_node.value)
            current_node = current_node.next


ll1 = LinkedList()

ll1.append(22)
ll1.append(2)
ll1.append(77)
ll1.append(6)
ll1.append(43)
ll1.append(76)
ll1.append(89)
ll1.append(75)

ll1.insert(0, 20)
ll1.insert(5, 64)

ll1.remove()
ll1.remove()

ll1.view_elements()
