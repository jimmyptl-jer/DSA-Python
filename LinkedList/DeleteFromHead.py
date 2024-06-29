# User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteAtPosition(head, pos):
    # Code to delete a node at a specific position in a linked list

    if head is None:
        return None
    
    if pos == 0:
        return head.next
    
    current_node = head
    position = 0
    
    while current_node.next is not None and position + 1 < pos:
        position += 1
        current_node = current_node.next
        
    if current_node.next is None or current_node is None:
        print("Index out of bounds")
    else:
        current_node.next = current_node.next.next
    
    return head


# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=' -> ')
        current = current.next
    print('None')


# Test cases
if __name__ == "__main__":
    # Test case 1: Deleting at position 2
    print("Test case 1:")
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    
    print("Before deletion:")
    printList(head1)  # Expected: 1 -> 2 -> 3 -> 4 -> None
    
    head1 = deleteAtPosition(head1, 2)
    print("After deleting at position 2:")
    printList(head1)  # Expected: 1 -> 2 -> 4 -> None
    print()

    # Test case 2: Deleting at position 0 (head)
    print("Test case 2:")
    head2 = Node(10)
    head2.next = Node(20)
    head2.next.next = Node(30)
    
    print("Before deletion:")
    printList(head2)  # Expected: 10 -> 20 -> 30 -> None
    
    head2 = deleteAtPosition(head2, 0)
    print("After deleting at position 0:")
    printList(head2)  # Expected: 20 -> 30 -> None
    print()

    # Test case 3: Deleting at position 1 (middle)
    print("Test case 3:")
    head3 = Node(5)
    head3.next = Node(15)
    head3.next.next = Node(25)
    head3.next.next.next = Node(35)
    
    print("Before deletion:")
    printList(head3)  # Expected: 5 -> 15 -> 25 -> 35 -> None
    
    head3 = deleteAtPosition(head3, 1)
    print("After deleting at position 1:")
    printList(head3)  # Expected: 5 -> 25 -> 35 -> None
    print()

    # Test case 4: Deleting at position out of bounds
    print("Test case 4:")
    head4 = Node(100)
    head4.next = Node(200)
    
    print("Before deletion:")
    printList(head4)  # Expected: 100 -> 200 -> None
    
    head4 = deleteAtPosition(head4, 5)  # Position 5 is out of bounds
    print("After attempting to delete at position 5 (out of bounds):")
    printList(head4)  # Expected: 100 -> 200 -> None
