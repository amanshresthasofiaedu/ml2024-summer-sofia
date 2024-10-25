def createList():
    size = int(input("Enter the number of items to be in the list "))
    mainList = [0] * size
    for i in range (0, size):
        mainList[i] = int(input("Enter an item to store in the list "))
    
    return mainList

def findElement(list, value):
    for i in range(0,len(list)):
        if(list[i] == value):
            return i  + 1 # Response needs to be 1 to N inclusive
    return -1

mainList = createList()
toFind = int(input("Now enter an item you'd like to search "))
print(f"You can find the element at {findElement(mainList, toFind)}")

