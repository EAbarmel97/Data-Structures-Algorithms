class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None


class BST:
    # inicializar el BST
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    # para agregar elemento al BST
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node  # nodo que se agrega la raiz
            return True
        temp = self.root  # var auxiliar
        while True:
            # si hay un valor repetido se rompe el bucle while
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node  # al nodo izq le agregar el nodo creado
                    return True  # para continuar con el bucle
                temp = temp.left  # la ref auxiliar se mueve el nodo de la izquierda

            else:
                if temp.rigth is None:
                    temp.rigth = new_node  # al nodo izq le agregar el nodo creado
                    return True  # para continuar con el bucle
                temp = temp.rigth  # la ref auxiliar se mueve el nodo de la derecha

    # verifica si cierto valor se encuentra en el arbol
    def contains(self, value):
        # si el arbol es vacio
        if self.root is None:
            return False
        temp = self.root  # variable auxiliar para moverse sobre los niveles del arbol

        while temp is not None:
            if temp.value > value:
                temp = temp.left  # la referencia aux se mueve a la izquierda

            elif temp.value < value:
                temp = temp.rigth  # la referencia aux se mueve a la derecha

            else:
                return True  # el valor se encuentra en algun nodo
        return False  # cuando elemento no se encuentra en el arbol

    # encontrar el minimo de un subnodo
    def min_value_subnode(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left  # si el nodo no es vacio, la ref auxiliar se mueve a la izquierda
        # cuando se llega al elemento min el hijo izquierdo es vacio y el bucle se para
        return current_node.value  # devolvemos el nodo cuyo hijo izq es el m??nimo

    def BFS(self):
        current_node = self.root  # se empieza desde la raiz del BST
        queue = []  # para los nodos
        results = []  # resulatdos de recorrer padre-hijo izquierdo-hijo derecho
        queue.append(current_node)  # agregrar el nodo sobre el que actualmente esta
        while len(queue) != 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)  # el hijo izq se agrega a la cola
            if current_node.rigth is not None:
                queue.append(current_node.rigth)  # el hijo derecho se agrega a la cola
        return results  # devolvemos la lista que indica el recorrido del arbol

    @staticmethod
    def DFS_pre_order(current_node):
        results = []
        if current_node: #chechamos que no sea vacio
            ########funcion para recorrer en preorden ################
            def traverse(current_node,results):
                results.append(current_node.value) #se agrega el valor del nodo
                if current_node.left is not None:
                    traverse(current_node.left,results)
                if current_node.rigth is not None: #si el nodo derecho no es vacio
                    traverse(current_node.rigth,results) #se aplica la funcion

            #NOTA: Para esta funcion recorre el arbol de la forma hijo nodo padre-hijo izquierdo-hijo derecho (V-L-R)

        traverse(current_node,results)
        return results #lista de los valores de los nodos recorridos recursivamente traverse

    @staticmethod
    def DFS_post_order(current_node):
        results = [] #nodos recorridos
        if current_node: #checamos que no sea vacio
            ########funcion para recorrer en post-orden ################
            def traverse(current_node,results):
                if current_node.left is not None:
                    traverse(current_node.left,results)
                if current_node.rigth is not None:
                    traverse(current_node.rigth,results)
                results.append(current_node.value) #se agrega el valor del guardado en el nodo
            #NOTA: Para esta funcion recorre el arbol de la forma hijo izq-hijo derecho-nodo padre (L-R-V)

        traverse(current_node, results)
        return results #lista de nodos recorridos luego de aplicar recursivamente la funcion traverse


my_tree = BST(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

raiz_arbol = my_tree.root

print(my_tree.DFS_post_order(raiz_arbol))
