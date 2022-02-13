class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def push_back(self, data):
        if self.is_empty():
            self.head = Node(data)
            return

        temp = self.head
        new_node = Node(data)
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            print(temp.data, end= " -> ")
            temp = temp.next
        print()

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp

    def push_before(self, fdata, pdata):
        if self.is_empty():
            return
        if self.head.data == fdata:
            self.push_front(pdata)
            return

        temp = self.head
        while temp.next is not None and temp.next.data != fdata: #condition  ordering matters other it will give error as if temp.next will be none and condition 2nd second will be at 1st position then error will occur that None type has no attribute data
            temp = temp.next
        if temp.next is not None:
            curr = temp.next
            new_node = Node(pdata)
            temp.next = new_node
            new_node.next = curr

    def push_after(self, fdata, pdata):

        if self.is_empty():
            return

        temp = self.head
        while temp is not None and temp.data != fdata: #condition  ordering matters other it will give error as if temp will be none and condition 2nd second will be at 1st position then error will occur that None type has no attribute data
            temp = temp.next
        if temp is not None:
            new_node = Node(pdata)
            curr = temp.next
            temp.next = new_node
            new_node.next = curr

    def pop_back(self):

        if self.is_empty() :
            return

        prev = self.head.data
        if self.head.next is None:
            self.head = None
            return prev

        temp = self.head
        while temp.next.next:
            temp = temp.next
        prev = temp.next.data
        temp.next = None

        return prev

    def pop_front(self):

        if self.is_empty():
            return
        prev = self.head.data
        if self.head.next is None:
            self.head = None
            return prev

        self.head = self.head.next
        return prev

    def pop_before(self, fdata):
        if self.is_empty() or self.head.next is None :
            return
        temp = self.head
        if temp.next.data == fdata:
            return self.pop_front()
        # temp = self.head
        while temp.next.next is not None and temp.next.next.data != fdata  : #condition  ordering matters other it will give error as if temp.next.next will be none and condition 2nd second will be at 1st position then error will occur
            temp = temp.next
        if temp.next.next is not None :
            curr = temp.next.next
            prev = temp.next.data
            temp.next = curr
            return prev

    def pop_after(self, fdata):

        if self.is_empty() or self.head.next is None :
            return
        temp = self.head
        while temp is not None and temp.data != fdata :
            temp = temp.next

        if temp is not None:
            if temp.next is None:
                return
            curr = temp.next.next
            prev = temp.next.data
            temp.next = curr
            return prev

    def update(self, fdata, udata):
        if self.is_empty():
            return
        temp = self.head
        while temp:
            if temp.data == fdata:
                temp.data = udata
            temp = temp.next
        return

    def is_search(self, fdata):
        if self.is_empty():
            return False
        temp = self.head
        while temp:
            if temp.data == fdata:
                return True
            temp = temp.next
        return False

    def size(self):
        length = 0
        temp = self.head
        while temp is not None:
            length = length + 1
            temp = temp.next
        return length

    def middle(self):
        if self.is_empty():
            return -1
        n = self.size()
        if n <= 2:
            return self.head.data
        mid = n//2 if n % 2 == 0 else n // 2 + 1
        temp = self.head
        while mid - 1:
            temp = temp.next
            mid -= 1
        return temp.data

    def reverse(self):
        if self.is_empty():
            return
        temp = self.head
        prev = None
        while temp:
            curr = temp.next
            temp.next = prev
            prev = temp
            temp = curr
        self.head = prev


l1 = LL()
l1.push_back(5)
# l1.push_back(-9)
l1.push_front(8)
l1.push_before(5, 6)
l1.push_before(6, 4)
l1.push_before(5,3)
# l1.push_before(10,10)
l1.display()
# l1.push_after(10,10)
# print(f"pop back {l1.pop_back()}")
# print(l1.is_empty())
# print (f"pop front {l1.pop_front()}")
# print (f" pop before  10 is {l1.pop_before(10)}")
# print(f' pop after 8 is  {l1.pop_after(6)}')
l1.update(6, 10)
print("after updation ")
l1.display()
print(l1.size())
print(l1.is_search(11))
print (f'middle is {l1.middle()}')
l1.display()
l1.reverse()
l1.display()