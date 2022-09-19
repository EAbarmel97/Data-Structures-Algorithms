class Node:
    def __init__(self,value):
        self.value = value #valor del nodo 
        self.next = None  #apuntador hacia la derecha
        self.prev = None  #apuntador hacia la izq 

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_dll(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp=temp.next #reasiganmos para poder correr la lista

#agregar un elemento al final de la dll 
    def append(self,value):
       new_node = Node(value)
       #si la lista es vacía 
       if self.head is None:
        self.head = new_node 
        self.tail = new_node 

       # para cuando la lista tiene un elemento o más 
       else:
          self.tail.next = new_node #último nodo de la list apunta al nuevo nodo 
          new_node.prev = self.tail # el apuntador previo apunta a al final de la lista 
          self.tail = new_node #se une la lista y el apuntador del final se pasa al nuevo nodo
       self.length += 1 
       return True 
    
mi_2_lista =DoublyLinkedList(1)
mi_2_lista.append(2)

mi_2_lista.print_dll() 