sequential_list = []

class SequentialList:
    def __init__ (self):
        self.data = []
        self.length = 0
        self.capacity = 5
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def insert(self, index, value):
        if self.length >= self.capacity:
            return False
        else:
            self.data = self.data[:index] + [value] + self.data[index:]
            self.length += 1
            return True
    
    def append(self, value):
        self.data = self.data + [value]
        self.length += 1
        return True
    
    def prepend(self, value):
        self.data = [value] + self.data
        self.length += 1
        return True
    
    def delete(self, index):
        deleted = self.data[index]

        self.data = self.data[:index]+self.data[index+1:]
        self.length -= 1
        return deleted
    
    def delete_by_value(self, value):
        for i in enumerate(self.data):
            if self.data[i] == value:
                self.data = self.data[:i]+self.data[i+1:]
                self.length -= 1
                return True
        return False

    def delete_head(self):
        self.data = self.data[1:]
        self.length -= 1
        return True
    
    def delete_tail(self):
        self.data = self.data[:-1]
        self.length -= 1
        return True
    
    def get(self, index):
        return self.data[index]
    
    def update(self, index, value):
        self.data[index] = value
        return True
    
    def find(self, value):
        for i in enumerate(self.data):
            if self.data[i] == value:
                return i
        return False
    
    def display(self):
        print(self.data)
        return True

    def reverse(self):
        self.data = self.data[::-1]
        return True
    
    def clear(self):
        self.data = []
        self.length = 0
        return True
