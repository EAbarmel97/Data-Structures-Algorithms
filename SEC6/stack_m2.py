class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

class Stack:
    def __init__(self,value):
        new_node = Node(value) #se crea un nodo 
        self.top = new_node 
        self.height = 1 

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def push(self, value):
        new_node = Node(value)
        #cuando la lista tiene 0 elementos 
        if self.height == 0:
            self.top = new_node #referencia del nodo 
        #lista con 1 elemento o más     
        else:
             new_node.next = self.top #el nuevo nodo apunta a la ref del último nodo 
             self.top = new_node #la ref se mueve al nodo recien agregado 
        self.height +=1 
        return True
        
    def pop(self):
        if self.length == 0: 
            return None
        pass           