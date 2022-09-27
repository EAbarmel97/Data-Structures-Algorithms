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
        return False #si ya existe el vertice

    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():#si ambos vertices existen
            #agregamos al arista
            self.adj_list[v1].append(v2) #v1 teiene artista con v2
            self.adj_list[v2].append(v1) #v2 tiene arista con v1
            return True 
        return False  #si ya existe la arista 

    def remove_edge(self,v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():#si ambos vertices existen
            #puede removerse al arista
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True 
        return False     

mg = Graph()

mg.add_vertex("A")
mg.add_vertex("B")
mg.add_vertex("C")
mg.add_edge("A","B")
mg.print_Graph()
print(mg.adj_list.keys())
mg.add_edge("A","C")
mg.add_edge("B","C")
mg.print_Graph()


