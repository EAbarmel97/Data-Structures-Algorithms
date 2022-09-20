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
        while temp is not None: #mientras la lista no es vacia, imprimimos el valor del nodo 
            print(temp.value)
            temp = temp.next
            
    #agergar un nodo 
    def push(self, value):
        new_node = Node(value)
        #cuando la lista tiene 0 elementos 
        if self.height == 0:
            self.top = new_node #referencia del nodo 
        #lista con 1 elemento o mas     
        else:
             new_node.next = self.top #el nuevo nodo apunta a la ref del ultimo nodo 
             self.top = new_node #la ref se mueve al nodo recien agregado 
        self.height +=1 
        return True

    #quitar un nodo 
    def pop(self):
        #cuando se tiene 1 elemento 
        if self.height == 0: 
            return None
        temp = self.top
        self.top = self.top.next #la ref del ultimo nodo se mueve al penultimo nodo 
        temp.next = None #spearamos el nodo 
        self.height -= 1
        return temp #devolvemos el nodo que se separa

nuevo_stack = Stack(7)
nuevo_stack.push(23)
nuevo_stack.push(3)
nuevo_stack.push(11)

nuevo_stack.print_stack()


        
            