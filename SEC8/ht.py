class HT:
    def __init__(self,size=7):
        self.data_map = [None]*size #espacios en la tabla 
    
    def _hash(self,key):
        myhash = 0 
        for character in key:
            (myhash + ord(character)* 49) % len(len(self.data_map))
        return myhash #indice de la tabal en la que se guarada el par llave-valor

    def print_HT(self):
        for i, val in enumerate(self.data_map):
            print( i + ':' + val) #indice la tabla vs valor
