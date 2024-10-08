The ceiling of a key in a Binary Search Tree (BST) is the smallest value in the tree that is greater than or equal to the given key. If no such value exists, the function should return -1.

Here’s how we can implement this:

Steps to find the ceiling:
Start at the root.
If the current node’s key is equal to the target key, the ceiling is the current node.
If the current node’s key is smaller than the target key, move to the right subtree (since larger values are on the right).
If the current node’s key is greater than the target key, this node could be a candidate for the ceiling, but we also need to check the left subtree to see if there’s a smaller valid candidate.
If no valid ceiling is found, return -1.
Python Code:
python
Copy code
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find the ceiling of a given key in a BST
def ceiling(root, key):
    # If the root is None, there is no ceiling, so return -1
    if not root:
        return -1

    # If the root's key is equal to the target key, the ceiling is the key itself
    if root.key == key:
        return root.key

    # If the root's key is smaller than the target key, move to the right subtree
    if root.key < key:
        return ceiling(root.right, key)

    # If the root's key is greater than the key, check the left subtree for a closer ceiling
    ceilingValue = ceiling(root.left, key)

    # If a valid ceiling is found in the left subtree, return it; otherwise, return the current node's key
    if ceilingValue != -1 and ceilingValue >= key:
        return ceilingValue
    else:
        return root.key

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
# Constructing the BST with input 4 2 15 1
root = None
arr = [4, 2, 15, 1]
for key in arr:
    root = insert(root, key)

# Test cases
# Test case 1
target = 19
print("Ceiling of", target, "is", ceiling(root, target))  # Output should be -1 (no value greater than or equal to 19)

# Test case 2
target = 3
print("Ceiling of", target, "is", ceiling(root, target))  # Output should be 4

# Test case 3
target = 1
print("Ceiling of", target, "is", ceiling(root, target))  # Output should be 1 (exact match)

# Test case 4 (target smaller than any element in the tree)
target = 0
print("Ceiling of", target, "is", ceiling(root, target))  # Output should be 1 (smallest element greater than or equal to 0)
Key Points:
Return -1 if no ceiling exists: This happens when all elements in the tree are smaller than the target key.
Ceiling logic: If the current node’s value is greater than the target, it becomes a potential candidate for the ceiling, but we need to check the left subtree for smaller valid candidates.
Edge cases handled: If the tree is empty, or if the target key is larger than all elements in the tree, the function will return -1.
Example Test Cases:
Target = 19: Output should be -1 (no element in the tree is greater than or equal to 19).
Target = 3: Output should be 4 (smallest element greater than or equal to 3).
Target = 1: Output should be 1 (exact match).
Target = 0: Output should be 1 (smallest element greater than or equal to 0).