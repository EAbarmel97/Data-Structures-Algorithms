class Node:
    def __init__(self,value):
        self.value = value 
        self.left= None 
        self.rigth= None 

class BST:
    #inicializar el BST 
    def __init__(self,value):
        new_node = Node(value)
        self.root = new_node

    """ def print_BST(self):
        count = 0 
        temp = self.root
        while not temp:
            print("{temp.value}".format(temp.value))
            print('/" + " " + "\"') """


#para agregar elemento al BST 
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node #nodo que se agrega la raiz 
            return True 
        temp = self.root #var auxiliar 
        while True:
             #si hay un valor repetido se rompe el bucle while 
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node #al nodo izq le agregar el nodo creado
                    return True  #para continuar con el bucle
                temp = temp.left #la ref auxiliar se mueve el nodo de la izquierda

            else:
                if temp.rigth is None:
                    temp.rigth = new_node #al nodo izq le agregar el nodo creado
                    return True  #para continuar con el bucle
                temp = temp.rigth #la ref auxiliar se mueve el nodo de la derecha

    #verifica si cierto valor se encuentra en el arbol
    def contains(self, value):
        #si el arbol es vacio 
        if self.root is None:
            return False
        temp = self.root #variable auxiliar para moverse sobre los niveles del arbol 

        while temp is not None:
            if temp.value > value:
                temp = temp.left #la referencia aux se mueve a la izquierda 

            elif temp.value < value:
                temp = temp.rigth #la referencia aux se mueve a la derecha 
            
            else:
                return True #el valor se encuentra en algun nodo
        return False #cuando elemento no se encuentra en el arbol         

nuevo_bst1 = BST(47)
nuevo_bst1.insert(21)
nuevo_bst1.insert(76)
nuevo_bst1.insert(18)
nuevo_bst1.insert(27)
nuevo_bst1.insert(52)
nuevo_bst1.insert(82)

print(nuevo_bst1.contains(48))



         