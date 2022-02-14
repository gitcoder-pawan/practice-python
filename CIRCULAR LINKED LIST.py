class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def display(self):
        if self.is_empty():
            print("Doubly Circular Linked List is Empty")
            return
        curr = self.head
        while curr.next is not self.head:  # loop will break at the last node so it will not print hte last node
            print(curr.data, end=" -> ")
            curr = curr.next
        print(curr.data)  # to print the last we are printing the last node

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next is not self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def push_front(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head

    def pop_front(self):
        if self.is_empty():
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        prev = self.head.data
        self.head = self.head.next
        temp.next = self.head
        return prev

    def pop_back(self):
        if self.is_empty():
            return
        elif self.head.next is self.head:
            prev = self.head.data
            self.head = None
            return prev
        else:
            temp = self.head
            while temp.next.next is not self.head:
                temp = temp.next
            prev = temp.next.data
            temp.next = self.head
            return prev


def is_circular_linkedlist(l1):
    if l1.is_empty():
        return False
    temp = l1.head
    while temp.next is not None:
        if temp.next is l1.head:
            return True
        temp = temp.next
    return False


cl1 = CLL()
cl1.push_back(5)
cl1.push_back(7)
cl1.push_front(45)
cl1.push_back(6)
cl1.display()
print(f"pop front :: {cl1.pop_front()}")
cl1.display()
print(f"pop back :: {cl1.pop_back()}")
print(f"is circular linked list :: {is_circular_linkedlist(cl1)}")
cl1.display()
