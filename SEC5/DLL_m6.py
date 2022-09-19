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

    def pop(self):
        temp = self.tail
        #si hay cero elementos
        if self.length == 0:
            return None
        #1 elemento en la lista doble
        elif self.length == 1:
            self.head = None
            self.tail = None
        #cuando la dll tiene más de 1 elemento
        else:
            self.tail = self.tail.prev #el puntero del final se recorre al nodo anterior
            self.tail.next = None
            temp.prev = None #se separa el nodo
        self.length -= 1
        return temp.value#nodo que se quita del final

#agregar un nodo al incio de la lista doble
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node #el inicio se mueve al nuevo nodo
            self.head = new_node
        self.length +=1
        return True
#eliminar el primer elemento
    def pop_first(self):
        #o elementos en la lista 
        if self.length == 0:
            return None
        temp = self.head

        if self.length == 1: 
            self.head = None 
            self.tail = None
        #dos elementos o más      
        else:
            self.head = self.head.next #movemos el inicio al nodo anterior 
            self.head.prev = None #separamos la lista del nodo inicial 
            temp.next = None #separamo el nodo inical del resto de la lista 
        self.length -=1 
        return temp #devolvemos el nodo que quitamos  

#obtener el valor de un nodo asociado a un índice dado 
    def get(self,index):
        #para el indice fuera del rango asociado a la dll 
        if index < 0 or index >= self.length:
            return None 
        #índice dentro del rango 
        temp= self.head 
        if index < self.length/2: #para cuando el indice cae en la mitad izq de la lista 
            for _ in range(index):
                temp = temp.next
        else: #para cuando el índice cae en la otra mitad 
            temp = self.tail
            #la lista lista tiene 0, ..., n elementos y el bucle for por lo que para empezar desde el final (n)
            #tomamos (n+1)-1 de punto de partida y llegamos al indice buscado 
            for _ in range(self.length-1, index, -1):
                temp = temp.prev #recorremos nodos a la izquierda 
        return temp #nodo que buscamos 

#insertar un nuevo nodo en un índice dado
    def set_value(self,index,value):
        temp = self.get(index) #apuntador en el nodo cuyo índice buscamos
        if temp is not None:
            temp.value = value #cambiamos el valor del nodo 
            return True 
        return False #no se logró el cambio del  valo del nodo

my_dll1 = DoublyLinkedList(11)
my_dll1.append(3)
my_dll1.append(23)
my_dll1.append(7)

my_dll1.print_dll()

my_dll1.set_value(1,4)
#print(my_dll1.set_value(1,4))
print("\t")

my_dll1.print_dll()


