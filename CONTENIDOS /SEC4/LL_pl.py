class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
#para inrpimir la lista 
    def print_ll(self):
           temp = self.head #inicio de la lista enlazada 
           while temp is not None:
               print(temp.value) # imprimimos el valor de cada nodo
               temp = temp.next #valor del sigueinte nodo 

           