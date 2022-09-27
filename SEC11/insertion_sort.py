def insertion_sort(array):
    for i in range(1,len(array)): #se empieza desde el segundo elemento
        temp = array[i] #var auxiliar 
        j = i-1 
        while temp < array[j] and j > -1: #mientras ocurra que la var auxiliar 
            #es menor 
            array[j+1] = array[j] #la j+1-esima entrada se cambia por la j-esima, así 
            array[j] = temp 
            j-=1 #se recorre a la izquierda 
    return array #lista ordenada            