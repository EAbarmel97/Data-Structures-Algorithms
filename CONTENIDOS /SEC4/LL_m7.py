#Clase para crear un nodo 
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
#quitar al final
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

#agregar al inicio nuevo nodo 
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
#eliminar nodo inicial
    def pop_first(self,value):
        new_node = Node(value)
        if self.length == 0:
            return None  
        else: 
            temp = self.head 
            self.head = self.head.next #el nodo inicial 
            temp.next = None #se separa el nodo 
            self.length -=1
            if self.length ==0: 
                self.tail = None      
        return temp
#obtener un elemento específico al inicio        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 

        else: 
            temp = self.head
            for _ in range(index): 
                temp = temp.next #se continua moviento el puntero hasta llegar al 
                #nodo cuyo indice buscamos
            return temp #nodo que vamos a devolver 

    def set_value(self,index, value):
        temp = self.get(index) #se obtiene el nodo cuyo indice buscamos 
        if temp is not None: 
            temp.value = value #remplazamos el valor del nodo que se seleccionó 
            return True
        return False 
#inserta un nuevo nodo en un cierto indice
    def insert(self,index, value):

        if index < 0 or index > self.length: 
            return False 
        #insertamos al inicio     
        if index == 0:
            return self.prepend(value)
        #insertamos al final 
        if index == self.length:
            return self.append(value)    
        new_node = Node(value)
        temp = self.get(index-1) #posición en la que se inserta 
        new_node.next = temp.next #dir en la que apunta el siguiente 
        temp.next = new_node #agrega a lista 
        self.length += 1 
        return True
#remueve un cierto elemento 
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
#si el elemnto que queremos quitar es el primer elemento de la lista            
        if index == 0:  
            return self.pop_first()
#si quitamos el ultimo elemento 
        if index == self.length:
            return self.pop()

        prev = self.get(index - 1) #nodo previo al que vamos a quitar 
        temp = prev.next 
        prev.next = temp.next 
        temp.next = None 
        self.length -=1
        return temp #nodo que se eleminó 


my_ll2 = LinkedList(11)      
my_ll2.append(3)
my_ll2.append(23)
my_ll2.append(7)

my_ll2.print_ll()

print("\t")
my_ll2.remove(2)

my_ll2.print_ll()


       


        


