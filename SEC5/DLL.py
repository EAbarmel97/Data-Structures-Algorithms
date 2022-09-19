class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_dll(self):
        temp = self.head 
        while temp.next is not None:
            print(temp.value)
            temp= temp.next #reasiganmos para poder correr la lista 

            
