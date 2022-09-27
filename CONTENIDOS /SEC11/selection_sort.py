def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i 
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]: #si los elementos que siguen de i son mayores que 
                #este, se intercambian los indices
                min_index = j
        if i != min_index:
            temp = array[i] #var auxiliar pra guardar el valor 
            array[i] = array[min_index] #el valor de la i-esima entrada se cambia por la de
        #la j-esima entrada 
            array[min_index] = temp #el valor de la j-esima entrada se cambia por la de
        #la i-esima entrada
    return array #lista ordenada    
        

print(selection_sort([4,2,6,5,1,3]))            
