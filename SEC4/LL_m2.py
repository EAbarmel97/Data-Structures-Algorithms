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

    def append(self,value):
        new_node = Node(value) #creamos un nodo 
        if self.head is None: 
          self.head = new_node
          self.tail = new_node

        else:
            self.tail.next = new_node 
            self.tail = new_node #actualizamos el apuntador 
        self.length +=1 
        
#quitar elemento al final de la lista 
    def pop(self):
        #si la lista tiene 0 elemntos 
        if self.length == 0:
            return None 
        else:
            pre = self.head
            temp = self.tail 
            while(temp.next) is not None:
                pre = temp 
                temp = temp.next 
            self.tail = pre 
            self.tail.next = None 
            self.length -= 1
            if self.length == 0: 
                self.head = None 
                self.tail = None 
            return temp      


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_ll()

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
my_linked_list.print_ll()

# (1) Item -  Returns 1 Node
#print(my_linked_list.pop())
# (0) Items - Returns None

