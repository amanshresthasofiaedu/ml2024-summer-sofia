class NumberSearch:
    def __init__(self, n):
        self.data = [0] * n
        self.size = n
        self.count = 0  

    def insert(self, value):
        if self.count < self.size:
            self.data[self.count] = value
            self.count += 1
            return True  
        else:
            return False 


    def search(self, x):
        for i in range(self.count):  
            if self.data[i] == x:
                return i + 1
        return -1