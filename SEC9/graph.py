class Graph:
    def __init__(self):
        self.adj_list = {} #dicionario vacio en el que se van a guardar 
        #los vertices ()

    def print_Graph(self):
        for vertex in self.adj_list:
            print(vertex ,':', self.adj_list[vertex]) #vertice vs lista de de vertices adjacentes

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys(): #si el vertice existe agregamos un lista vacia 
            #en la que iran los vertices con lo que hay union
            self.adj_list[vertex] = []
            return True 
        return False #falso si ya existe el vertice

