class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find floor in a BST
def floor(root, key):

    # If the root is None, there is no floor
    if not root:
        return None

    # If the root's key is equal to the target key
    if root.key == key:
        return root.key

    # If the root's key is greater than the target key
    if root.key > key:
        return floor(root.left, key)

    # If root.key is less than or equal to key, check the right subtree
    floorValue = floor(root.right, key)

    # If floorValue is None or greater than key, the floor is root's key
    return floorValue if floorValue is not None and floorValue <= key else root.key

# Function to insert a node in the BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Example usage:
# Construct the BST with input 4 2 15 1
root = None
arr = [4, 2, 15, 1]
for key in arr:
    root = insert(root, key)

# Test case 1
target = 19
print("Floor of", target, "is", floor(root, target))  # Output should be 15

# Test case 2
target = 3
print("Floor of", target, "is", floor(root, target))  # Output should be 2

# Test case 3
target = 1
print("Floor of", target, "is", floor(root, target))  # Output should be 1
