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

    def print_ll(self):
           temp = self.head #inicio de la lista enlazada 
           while temp is not None:
               print(temp.value) # imprimimos el valor de cada nodo
               temp = temp.next #valor del sigueinte nodo 
               
#agregar al final de la lista 
    def append(self,value):
        new_node = Node(value) #creamos un nodo 
        if self.head is None: 
          self.head = new_node
          self.tail = new_node

        else:
            self.tail.next = new_node 
            self.tail = new_node #actualizamos el apuntador 
        self.length +=1 
        return True


mi_nueva_lista = LinkedList(3)


mi_nueva_lista.append(2)

mi_nueva_lista.print_ll()
