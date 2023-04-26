class Queue:
    def __init__(self):
        self.items = []
        self.items

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "Item has been added to the end of the Queue"

q1 = Queue()
q1.enqueue(2082022)
q1.enqueue(3082022)
print(q1)

