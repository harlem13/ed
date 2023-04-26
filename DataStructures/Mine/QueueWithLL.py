class Item:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(item) for item in self]
        return 'The queue consists of : '+' '.join(values)

    def enqueue(self, value):
        newItem = Item(value)
        if self.head == None:
            self.head = newItem
            self.tail = newItem
        else:
            self.tail.next = newItem
            self.tail = newItem


    def dequeue(self):
        if self.head is None:
            return "The queue is empty"
        else:
            dequeuedItem = self.head
            if self.head == self.tail:
                self.head = self.tail = None
                print("Now the queue is empty")
            else:
                self.head = self.head.next
                print(str(dequeuedItem) + " has been removed from queue")
            return str(dequeuedItem)
q1 = Queue()
print(q1)
print("..........")
q1.enqueue(10)
print(q1)
print("..........")
q1.enqueue(11)
print(q1)
print(q1.head.value)
print(q1.tail.value)

q1.enqueue(12)
print(q1)
print(q1.head.value)
print(q1.tail.value)
for item in q1:
    if item.next == None:
        print("EOF")
    else:
        print(".." +str(item.next.value))

q1.dequeue()
print(q1)
print(q1.head.value)
print(q1.tail.value)
q1.dequeue()
print(q1)
print(q1.head.value)
print(q1.tail.value)
q1.dequeue()
print(q1)
print(q1.head is None)
print(q1.tail is None)

