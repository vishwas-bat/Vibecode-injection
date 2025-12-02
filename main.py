# Simple list
arr = [10, 20, 30, 40, 50]

# Get index from user
index = int(input("Enter index (0 to 4): "))

# Fetch and print element
if 0 <= index < len(arr):
    print("Element at index", index, "is:", arr[index])
else:
    print("Invalid index")
