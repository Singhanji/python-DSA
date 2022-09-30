from xxlimited import new
from regex import D
from requests import NullHandler, head

# create a class of node having properties data and None
class CreateNode:

# define a constructor which initiates the object of the 'CreateNode' class
    def __init__(self, d) -> None:
        self.data = d
        self.next = None

# create another class for Linked List where, initially head is assigning empty List
class LinkedList:

# create a constructor to initiate the object of class LinkedList
    def __init__(self) -> None:
        self.head = None

# defining a method for creating the linked list by 'inserting nodes' into the list from scratch
    def CreateLL(self, newNode):
        # if there is no node in the list insert a new one
        if self.head is None:
            self.head = newNode
            # else, go to the last node make head a pointer at the last node make the last node's next to the new node
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

# create another method to print the Linked List
    def printList(self):
        # head->1->2->3->None
        if self.head is None:
            print('List is empty')
            return 
        
        temp = self.head
        while True:
            if temp is None:
                break
            print(temp.data)
            temp = temp.next

# Driver Code
# Firstly creating Node: which has--> data and next(pointer which will points to the address of the next node's data)



firstNode = CreateNode(1)
lList = LinkedList()
lList.CreateLL(firstNode)
secondNode = CreateNode(2)
lList.CreateLL(secondNode)
thirdNode = CreateNode(3)
lList.CreateLL(thirdNode)
lList.printList()