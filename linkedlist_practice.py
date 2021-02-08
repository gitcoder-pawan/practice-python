class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Ll:
    def __init__(self):
        self.head = None

    def add(self, value):
        New_node = Node(value)
        New_node.next = self.head
        self.head = New_node

    def add_(self, value):
        New_node = Node(value)
        temp = self.head
        if temp == None:
            self.head = New_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = New_node

    def add_after(self, after, value):
        temp = self.head
        while temp != None:
            if temp.data == after:
                break
            temp = temp.next
        if temp == None:
            print("not found")
        else:
            New_node = Node(value)
            New_node.next = temp.next
            temp.next = New_node

    def traverse(self):
        temp = self.head
        if temp == None:
            print("empty list")
        else:
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
        print()

    def delete(self):
        if self.head == None:
            return "empty"
        else:
            self.head = self.head.next

    def delete_(self):
        if self.head == None:
            return "empty"
        else:

            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                temp.next = None

    def delete_after(self, after):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp.next != None:
                if temp.data == after:
                    temp.next = temp.next.next
                    return
                temp = temp.next
            print("not found")


l = Ll()
l.add(5)
l.add(6)
l.add_(7)
l.add_(8)
l.traverse()
l.add_after(6,7)
l.traverse()
l.delete()
l.traverse()
l.delete_()
l.traverse()
l.delete_after(6)
l.traverse()
