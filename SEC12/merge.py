#esta funcion va a fusionar dos listas ordenads en unsa sola lista ordenada 
def Merge(array1, array2):
    comb_array = []
    i = 0 #valor inicial del indice primera lista 
    j = 0 #valor inicial del indice segunda lista 
    while i < len(array1) and j < len(array2): 
        if array1[i] < array2[j]:# elemto de la primera lista es mejor que el de la segunda.
            #Entonces se agrega el elemento menor  
            comb_array.append(array1[i]) 
            i += 1
        else: 
            comb_array.append(array2[j])    
            j += 1
    #si la lista 2 queda vacia      
    while i < len(array1):
        comb_array.append(array1[i])
        i += 1
    #si la lista 1 queda vacia    
    while j < len(array2):
        comb_array.append(array2[j])    
        j += 1    
    return comb_array #listas combinadas de forma ordenada    