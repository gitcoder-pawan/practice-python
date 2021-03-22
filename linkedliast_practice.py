class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class L:
    def __init__(self):
        self.head = None

    def insBeg(self, value=None):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next= self.head
            self.head = node

    def traversal(self):
        if self.head == None:
            print('Linked list is empty')
        else:
            temp = self.head
            while temp!=None:
                print(temp.data, end=" ")
                temp= temp.next

    def insEnd(self,value=None):
        node= Node(value)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node

    def clear(self):
        self.head=None

    def insAft(self,pos,value=None):
        node=Node(value)
        temp=self.head
        while temp!=None:
            if temp.data==pos:
                node.next = temp.next
                temp.next = node
                break
            temp=temp.next
        if temp==None:
            print("pos not found")

l1=L()
l1.insBeg(100)
l1.insBeg(6)
l1.insBeg(9)
l1.insEnd(2.5)
l1.insEnd(200)
l1.insAft(9,5)
l1.insAft(9,5)
l1.insAft(9,5)
l1.clear()
l1.traversal()