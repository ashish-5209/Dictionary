class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def intersection(self, h1, h2):
        s = set()
        while h1:
            s.add(h1)
            h1 = h1.next
        while h2:
            if h2 in s:
                print(h2, end=" ")
            h2 = h2.next
        print()

l1 = LinkedList()
l1.push(10)
l1.push(15)
l1.push(4)
l1.push(20)

l2 = LinkedList()
l2.push(8)
l2.push(4)
l2.push(2)
l2.push(10)
l1.printList()
l2.printList()
llist = LinkedList()
llist.intersection(l1, l2)
