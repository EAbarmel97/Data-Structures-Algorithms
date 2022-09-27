from SEC12.merge import Merge 

def merge_sort(array):
    #caso base 
    if len(array) == 1 :
        return array 
    mid = int(len(array)/2) #punto medio del lista
    left_array = array[:mid] #mitad izq 
    rigth_array = array[mid:] #mitad derecha

    ##### PASO RECURSIVO ######## 
        