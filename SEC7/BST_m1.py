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

nuevo_bst = BST(2)   

nuevo_bst.insert(1)
nuevo_bst.insert(3)

print(nuevo_bst.root.value)
print(nuevo_bst.root.left.value)
print(nuevo_bst.root.rigth.value)






