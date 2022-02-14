class Node :
    def __init__(self, data):
        self.prev=None
        self.data = data
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def display(self):
        if self.is_empty():
            print("Double Linked List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print()

    def push_front(self, data):

        if self.is_empty():
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_back(self, data):
        if self.is_empty():
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node
        new_node.prev = temp

    def pop_front(self):
        if self.is_empty():
            return
        if self.head.next is None:
            prev = self.head.data
            self.head = None
            return prev
        prev = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return prev

    def pop_back(self):
        if self.is_empty():
            return
        if self.head.next is None:
            prev = self.head.data
            self.head = None
            return prev
        temp = self.head
        while temp.next:
            temp = temp.next
        prev = temp.data
        temp.prev.next = None




dl1 = DLL()
# dl1.push_front(5)
dl1.push_front(76)
dl1.push_front(98)
dl1.push_back(6)
dl1.display()
dl1.pop_front()
dl1.display()
dl1.pop_back()
dl1.display()