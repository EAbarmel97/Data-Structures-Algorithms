class HT:
    def __init__(self,size=13):
        self.data_map = [None]*size #espacios en la tabla 
    
    def _hash(self,key):
        myhash = 0 
        for character in key:
            myhash = (myhash + ord(character)*49) % len(self.data_map)
        return myhash #indice de la tabal en la que se guarada el par llave-valor

    def print_HT(self):
        for i, val in enumerate(self.data_map):
            print(i,':',val) #indice de la tabla vs valor

    def set_item(self, key, value):
        #segun la llave generamos el hash 
        index  = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] #convetimos "None" en una lista vacia 
        self.data_map[index].append([key,value]) #agregamos una lista que contiene el par llave-valor 

    def get_item(self,key):
        index = self._hash(key) #buscamos el indice asociado con la llave
        if index is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[i][1] #valor asociado a la llave 
        return None #si no existe ningun valor que este asociado a la llave en la tabla hash  


    def keys(self):
        all_keys = [] #lista vacia en donde pondres listas que contiene a su vez listas 
        #con todas las llaves segun el indice de la tabla hash 
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                 all_keys.append(self.data_map[i][j][0])
        return all_keys #lista con todas las llaves 

tabla_prueba = HT() 

tabla_prueba.set_item("llave1", 4)
tabla_prueba.set_item("password2", 154)
tabla_prueba.set_item("password3", 155)
tabla_prueba.set_item("palabra", 15)
tabla_prueba.print_HT()
print(tabla_prueba.keys())            