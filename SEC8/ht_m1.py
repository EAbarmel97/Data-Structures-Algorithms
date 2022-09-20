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
        index  = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])    

my_hash_table = HT()

my_hash_table.set_item("llave1", 153)
my_hash_table.set_item("password2", 154)
my_hash_table.set_item("password3", 155)

my_hash_table.print_HT()