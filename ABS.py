class Stack():

    def __init__(self):
        self.data = []

    def __str__(self):
        return f"{self.data}"

    def push(self, ent):
        self.data.append(ent)

    def pop(self):
        return self.data.pop()

class Queue():
    
    def __init__(self):
        self.storage = []
        self.size = 0
        
    def __str__(self):
        return f"{self.storage}"

    def __len__(self):
        return self.size

    def enqueue(self, a):
        self.storage.append(a)
        self.size += 1

    def dequeue(self):
        if len(self.storage) > 0:
            ans = self.storage.pop(0)
            self.size -= 1
            return ans
        else:
            return False
        
    def front(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return False
    
    def is_empty(self):
        return len(self.storage) == 0

class PriorityQueue():

    def __init__(self):
        self.data = []
    
    def __str__(self):
        return f"{self.data}"

    def enqueue(self, ent):
        self.data.append(ent)

    def dequeue(self):
        if (len(self.data) > 0):
            max = 0
            for i in range(len(self.data)):
                if(self.data[i][0] > self.data[max][0]):
                    max = i
            item =  self.data[max]
            del self.data[max]
            return item
        else:
            raise Exception("Priority Queue is empty")

class HeapQueue():
    
    def __init__(self):
        self.data = []

    def __str__(self):
        return f"{self.data}"

    def enqueue(self, ent):
        self.data.append(ent)

    def dequeue(self):
        if (len(self.data) == 0):
            raise Exception("Heap Queue is empty")
        max = 0
        for i in range(len(self.data)):
            if(self.data[i] > self.data[max]):
                max = i
            item = self.data[max]
            del self.data[max]
            return item

