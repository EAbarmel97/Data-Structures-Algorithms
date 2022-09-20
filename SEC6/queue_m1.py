class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class Queue:
    def __init__(self,value):
       new_node = Node(value)
       self.first = new_node 
       self.last = new_node
       self.length = 1 

    def print_queue(self):
        temp = self.first
        while temp is not None: #mientras el nodo no sea vacio, imprimimos el valor 
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        #cuando hay 0 elemento
        if self.length == 0:
            self.first = new_node #ref inicial  apunta al nuevo nodo 
            self.last = new_node   #ref final apunta al nuevo nodo 

        else:
            self.last.next = new_node #hacemos la ref final apuntar al nuevo nodo 
            self.last = new_node #movemos la ref final al nuevo nodo y con eso el nuevo nodo se agrega 
        self.length +=1 #incremento en el tamaño de la lista 
        return True 

my_queue = Queue(5)
my_queue.enqueue(7)
my_queue.print_queue()

