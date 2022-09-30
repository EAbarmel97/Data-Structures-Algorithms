def swap(array, index1, index2):
    #indercambiamos valor en index1 por valor en index2 y viceversa 
    temp = array[index1] 
    array[index1] = array[index2]
    array[index2] = temp  

def partition(array,pivot_index,end_index):
    pivot = array[end_index] # 
    index = pivot_index - 1 #var auxiliar 
    for j in range(pivot_index, end_index):
        if array[j] <= pivot: #comparacion con el pivote 
            index += 1 #el indice se recorre a la derecha 
            swap(array,index,j) #intercambiar las entradas de la lista
            #index y j 
    swap(array,index+1,end_index) #intercambiar las entradas 
    return index + 1 #indice para la particion 

""" my_list = [2,8,7,1,3,5,6,4]

print(partition(my_list,0,6))
print(my_list) """
