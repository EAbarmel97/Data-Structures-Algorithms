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
        return True

    def pop(self):
        #si la lista tiene 0 elemntos 
        if self.length == 0:
            return None 
        #si la lista tiene 1 elemento o mas      
        else:
            pre = self.head 
            temp = self.tail 
            while(temp.next) is not None:
                pre = temp 
                temp = temp.next 
            self.tail = pre #penultimo nodo 
            self.tail.next = None 
            self.length -= 1
            if self.length == 0: 
                self.head = None 
                self.tail = None 
            return temp  #nodo que se retiró  


    def prepend(self,value):
        new_node = Node(value) #creamos un nodo 
        #lista con 0 elementos 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node 
        #lista con 1 o más elementos     
        else: 
            new_node.next = self.head  
            self.head = new_node
        self.length +=1     
        return True 
#eliminar elemento al inicio de a lista 
    def pop_first(self,value):
        new_node = Node(value)
        if self.length == 0:
            return None  
        else: 
            temp = self.head 
            self.head = self.head.next 
            temp.next = None 
            self.length -=1
            if self.length ==0: 
                self.tail = None      
        return temp
