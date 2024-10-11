# Initialize the heap
heap = []  # Use a dynamic list
curr_size = 0

# Function to insert a value into the heap
def insertKey(x):
    global curr_size
    heap.append(x)  # Append the new element
    curr_size += 1

    i = curr_size - 1
    # Move up the tree to maintain the min-heap property
    while i != 0 and heap[(i - 1) // 2] > heap[i]:
        heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
        i = (i - 1) // 2

# Function to heapify a subtree rooted at index i
def heapify(i):
    global curr_size
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < curr_size and heap[left] < heap[smallest]:
        smallest = left
    if right < curr_size and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(smallest)  # Recursively heapify the affected subtree

# Function to delete a key at index i
def deleteKey(i):
    global curr_size
    if curr_size == 0:
        return "Heap is Empty"
    if i < curr_size:
        heap[i] = heap[curr_size - 1]
        heap.pop()  # Remove the last element
        curr_size -= 1
        if curr_size > 0:
            heapify(i)

# Function to extract the minimum value in the heap
def extractMin():
    global curr_size
    if curr_size == 0:
        return -1

    min_val = heap[0]  # Get the root (minimum value)
    heap[0] = heap[curr_size - 1]
    heap.pop()  # Remove the last element
    curr_size -= 1

    if curr_size > 0:
        heapify(0)  # Start heapifying from the root

    return min_val

# Function to print the current state of the heap
def printHeap():
    global curr_size
    print("Current Heap:", heap[:curr_size])

# TEST CASES

# Test Insertions
print("Inserting values into the heap:")
insertKey(10)
printHeap()  # Expected: [10]

insertKey(20)
printHeap()  # Expected: [10, 20]

insertKey(5)
printHeap()  # Expected: [5, 20, 10]

insertKey(2)
printHeap()  # Expected: [2, 5, 10, 20]

insertKey(15)
printHeap()  # Expected: [2, 5, 10, 20, 15]

# Test Deletion
print("\nDeleting values from the heap:")
deleteKey(0)  # Delete the root (smallest element, i.e., 2)
printHeap()  # Expected: [5, 15, 10, 20]

deleteKey(2)  # Delete element at index 2 (i.e., 10)
printHeap()  # Expected: [5, 15, 20]

# Extracting minimum
print("\nExtracting minimum value from the heap:")
min_val = extractMin()
print(f"Extracted Min: {min_val}")  # Expected: 5
printHeap()  # Expected: [15, 20]
