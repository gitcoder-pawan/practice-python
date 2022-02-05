class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    l = 0

    def __init__(self):
        self.head = None

    def push(self, data):
        Stack.l += 1
        if self.head == None:
            self.head=Node(data)
        else:
            temp = self.head
            new_node = Node(data)
            self.head = new_node
            self.head.next = temp

    def pop(self):
        if self.head:
            self.head = self.head.next

    def peek(self):
        if self.head:
            return self.head.data

    def is_empty(self):
        if self.head:
            return False
        return True

    def length(self):
        return Stack.l

    def display(self):
        if self.head:
            temp=self.head
            while(temp):
                print(temp.data, end=" -> ")
                temp=temp.next
        else:
            return "Stack is Empty"



