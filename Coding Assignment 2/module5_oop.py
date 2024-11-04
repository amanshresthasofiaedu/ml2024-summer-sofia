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
    
size = int(input("Enter the number of items to be in the list: "))
num_list = NumberSearch(size)

for i in range(0,size):
    if num_list.insert(int(input("Enter the number to add: "))):
        print("Successfully added")
    else:
        print("Unsuccessful")

print(num_list.search(int(input("Enter the number to search: "))))