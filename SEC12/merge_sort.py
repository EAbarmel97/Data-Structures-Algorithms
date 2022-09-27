from merge import Merge 

def merge_sort(array):#esta es la funcion que particioan la lista 
    #caso base 
    if len(array) == 1 :
        return array 
    mid = int(len(array)/2) #punto medio del lista
    left_array = array[:mid] #mitad izq 
    rigth_array = array[mid:] #mitad derecha

    ##### PASO RECURSIVO ######## 
    return Merge(merge_sort(left_array),merge_sort(rigth_array)) #aplicamos recursivamente con las 
    #listas izq y der, despues las unimos usando la funcion Merge. 
print(merge_sort([9,10,1,5,4,13,2]))
