# from stack import Stack
#
#
# def decimal2Binary(n, s):
#     if n > 2 ** 31 - 1:
#         return 0
#     # if n < 0:
#     #     m = n
#     #     mask = 0
#     #     while (m):
#     #
#     #         mask = (mask << 1) | 1
#     #         m = m >> 1
#     #     return mask and ~n
#     while n:
#         # print(n%2)
#         s.push(n % 2)
#         n //= 2
#     bin = ""
#
#     while not s.is_empty():
#         bin += str(s.peek())
#         s.pop()
#     return bin
#
#
# s = Stack()
# n = int(input())
# bin = decimal2Binary(n, s)
# print(bin)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def size(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def pop(self, i):
        count = 1
        n = self.size()
        t = n + 1 - i

        temp = self.head
        while count < t-1:
            temp = temp.next
            count += 1
        prev = temp.next.data
        temp.next = temp.next.next
        return prev

    def display(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


l1 = LL()
l1.push_back(2)
l1.push_back(3)
l1.push_back(1)
l1.push_back(7)
l1.display()
print(l1.size())
print(l1.pop(2))
l1.display()
