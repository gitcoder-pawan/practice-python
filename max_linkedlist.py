class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def ins_beg(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def max(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            maximum = 0
            while temp is not None:
                if temp.data > maximum:
                    maximum = temp.data
                temp = temp.next
            return maximum

l1=LL()
n=input("enter no of elements: ")
for i in range(int(n)):
    l1.ins_beg(int(input()))
print(l1.max())