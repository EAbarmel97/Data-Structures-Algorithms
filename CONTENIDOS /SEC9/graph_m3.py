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
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): #verifica si los vertices están en la gráfica
            if v1 == v2: #no hay arista con un solo vertice  
                return False 
            elif v1 not in self.adj_list[v2] and v2 not in self.adj_list[v1]: #verifica si no existe ya 
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
                return True 
            return False #if edge already exists 
        return False #both vertices do not exist in the graph     

    def remove_edge(self,v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():#si ambos vertices existen
           if v1 != v2:
            try: #error handling if the edge does not exist 
               self.adj_list[v1].remove(v2)
               self.adj_list[v2].remove(v1)
            except ValueError:
                return False 
            return True #edge deleted 
           else:
            return False #when the given vertices are the same   
        return False #the vertices do not exist 

mg = Graph()

mg.add_vertex("A")
mg.add_vertex("B")
mg.add_vertex("C")
mg.add_vertex("D")
mg.add_edge("A","B")
mg.add_edge("B","A")
mg.add_edge("A","C")
mg.add_edge("C","A")
mg.add_edge("B","C")
mg.add_edge("C","B")
mg.remove_edge("A", "B")
mg.remove_edge("A", "D")
mg.remove_edge("A", "A")
mg.print_Graph() 
