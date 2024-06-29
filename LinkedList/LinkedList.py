class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        """
        Insert a new node at the beginning of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtEnd(self, data):
        """
        Insert a new node at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node

    def insertAtIndex(self, data, index):
        """
        Insert a new node at a specific index in the linked list.
        """
        if index == 0:
            self.insertAtBeginning(data)
            return
        
        new_node = Node(data)
        current_node = self.head
        position = 0
        
        while current_node is not None and position < index - 1:
            current_node = current_node.next
            position += 1
        
        if current_node is None:
            print("Index out of bounds")
        else:
            new_node.next = current_node.next
            current_node.next = new_node
                
    def updateAtIndex(self, val, index):
        """
        Update the value of the node at a specific index in the linked list.
        """
        current_node = self.head
        position = 0

        while current_node is not None and position != index:
            current_node = current_node.next
            position += 1
        
        if current_node is None:
            print("Index not present")
        else:
            current_node.data = val

    def removeFromHead(self):
        """
        Remove the node at the head of the linked list.
        """
        if self.head is None:
            return
        self.head = self.head.next
    
    def removeFromEnd(self):
        """
        Remove the node at the end of the linked list.
        """
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        
        current_node.next = None

    def removeAtIndex(self, index):
        """
        Remove the node at a specific index in the linked list.
        """
        if index == 0:
            self.removeFromHead()
            return
        
        current_node = self.head
        position = 0
        
        while current_node.next is not None and position < index - 1:
            current_node = current_node.next
            position += 1
        
        if current_node is None or current_node.next is None:
            print("Index not present")
        else:
            current_node.next = current_node.next.next

    def printSizeOfLL(self):
        """
        Return the size of the linked list.
        """
        if self.head is None:
            return 0
        
        current_node = self.head
        size = 0
        while current_node:
            current_node = current_node.next
            size += 1
        
        return size
    
    def searchInLL(self, value):
        """
        Search for a value in the linked list and return its index (1-based). Return -1 if not found.
        """
        current_node = self.head
        pos = 1

        while current_node is not None:
            if current_node.data == value:
                return pos
            pos += 1
            current_node = current_node.next
    
        return -1

    def printList(self):
        """
        Print the linked list.
        """
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Test cases
if __name__ == "__main__":
    # Initialize the linked list
    ll = LinkedList()

    # Test inserting at the beginning
    ll.insertAtBeginning(10)
    ll.insertAtBeginning(20)
    ll.insertAtBeginning(30)
    print("After inserting at the beginning:")
    ll.printList()  # Expected output: 30 -> 20 -> 10 -> None
    print("Updated size of the linked list:", ll.printSizeOfLL())  # Expected output: 3

    # Test inserting at the end
    ll.insertAtEnd(40)
    ll.insertAtEnd(50)
    print("After inserting at the end:")
    ll.printList()  # Expected output: 30 -> 20 -> 10 -> 40 -> 50 -> None
    print("Updated size of the linked list:", ll.printSizeOfLL())  # Expected output: 5

    # Additional test case: Insert at both beginning and end
    ll.insertAtBeginning(60)
    ll.insertAtEnd(70)
    print("After inserting at both beginning and end:")
    ll.printList()  # Expected output: 60 -> 30 -> 20 -> 10 -> 40 -> 50 -> 70 -> None

    # Test inserting at index
    ll.insertAtIndex(25, 2)  # Insert 25 at index 2
    print("After inserting at index 2:")
    ll.printList()  # Expected output: 60 -> 30 -> 25 -> 20 -> 10 -> 40 -> 50 -> 70 -> None

    ll.insertAtIndex(5, 0)   # Insert 5 at index 0 (beginning)
    print("After inserting at index 0:")
    ll.printList()  # Expected output: 5 -> 60 -> 30 -> 25 -> 20 -> 10 -> 40 -> 50 -> 70 -> None

    ll.insertAtIndex(65, 8)  # Insert 65 at index 8 (end)
    print("After inserting at index 8:")
    ll.printList()  # Expected output: 5 -> 60 -> 30 -> 25 -> 20 -> 10 -> 40 -> 50 -> 65 -> 70 -> None

    # Test out of bounds index
    ll.insertAtIndex(70, 15)  # Index out of bounds
    print("After attempting to insert at an out-of-bounds index:")
    ll.printList()  # Expected output: 5 -> 60 -> 30 -> 25 -> 20 -> 10 -> 40 -> 50 -> 65 -> 70 -> None

    # Test updating at index
    ll.updateAtIndex(100, 0)  # Update index 0
    print("After updating index 0 to 100:")
    ll.printList()  # Expected output: 100 -> 60 -> 30 -> 25 -> 20 -> 10 -> 40 -> 50 -> 65 -> 70 -> None

    ll.updateAtIndex(200, 3)  # Update index 3
    print("After updating index 3 to 200:")
    ll.printList()  # Expected output: 100 -> 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> 65 -> 70 -> None

    ll.updateAtIndex(300, 8)  # Update index 8
    print("After updating index 8 to 300:")
    ll.printList()  # Expected output: 100 -> 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> 300 -> 70 -> None

    # Test out of bounds update
    ll.updateAtIndex(400, 15)  # Index out of bounds
    print("After attempting to update an out-of-bounds index:")
    ll.printList()  # Expected output: 100 -> 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> 300 -> 70 -> None

    # Test removing from the head
    ll.removeFromHead()
    print("After removing from the head:")
    ll.printList()  # Expected output: 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> 300 -> 70 -> None

    # Test removing from the end
    ll.removeFromEnd()
    print("After removing from the end:")
    ll.printList()  # Expected output: 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> 300 -> None

    ll.removeFromEnd()
    print("After another removal from the end:")
    ll.printList()  # Expected output: 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> 50 -> None

    ll.removeFromEnd()
    print("After another removal from the end:")
    ll.printList()  # Expected output: 60 -> 30 -> 200 -> 20 -> 10 -> 40 -> None

    # Test removing at index
    ll.removeAtIndex(0)  # Remove index 0
    print("After removing index 0:")
    ll.printList()  # Expected output: 30 -> 200 -> 20 -> 10 -> 40 -> None

    ll.removeAtIndex(3)  # Remove index 3
    print("After removing index 3:")
    ll.printList()  # Expected output: 30 -> 200 -> 20 -> 40 -> None

    ll.removeAtIndex(2)  # Remove index 2
    print("After removing index 2:")
    ll.printList()  # Expected output: 30 -> 200 -> 40 -> None

    # Test out of bounds removal
    ll.removeAtIndex(10)  # Index out of bounds
    print("After attempting to remove an out-of-bounds index:")
    ll.printList()  # Expected output: 30 -> 200 -> 40 -> None
    print("Updated size of the linked list:", ll.printSizeOfLL())  # Expected output: 3

    # Test search in linked list
    print("Search for value 200 in the linked list:")
    print(ll.searchInLL(200))  # Expected output: 2 (1-based index)

    print("Search for value 40 in the linked list:")
    print(ll.searchInLL(40))  # Expected output: 3 (1-based index)

    print("Search for value 100 in the linked list:")
    print(ll.searchInLL(100))  # Expected output: -1 (not found)
