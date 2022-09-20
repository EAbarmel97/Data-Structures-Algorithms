class Node:
    def __init__(self,value):
        self.value = value 
        self.left= None 
        self.rigth= None 

class BST:
    def __init__(self,value):
        new_node = Node(value)
        self.root = new_node

    def print_BST(self):
        pass      