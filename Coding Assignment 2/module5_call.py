import module5_mod

size = int(input("Enter the number of items to be in the list: "))
num_list = module5_mod.NumberSearch(size)

for i in range(0,size):
    if num_list.insert(int(input("Enter the number to add: "))):
        print("Successfully added")
    else:
        print("Unsuccessful")

print(num_list.search(int(input("Enter the number to search: "))))