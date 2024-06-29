#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteAtPosition(head, pos):
    #code here
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
        
    if current_node.next is None:
        print("Index out of bounds")
    else:
        current_node.next = current_node.next.next
    
    return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node
    
def printList(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp=tmp.next
    print()
        


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        x=int(input())

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res=deleteAtPosition(ll.head,x)
        printList(res)
# } Driver Code Ends