class SingleLL:
    def __init__(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value=None):
        self.value = value

singleLList = SingleLL()
node1 = Node(1)
node2 = Node(6)

singleLList.head = node1
singleLList.head.next = node2
singleLList.tail = node2

print(singleLList)
