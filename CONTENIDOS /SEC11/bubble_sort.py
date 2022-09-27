def bubble_sort(array):
    for i in range(len(array)-1, 0,-1):#se toma len(lista) -1 porque python las listas empiezan en 0. 
        for j in range(i):#comparamos con las elementos de indices < i
            if array[j] > array[j+1]:
                temp = array[j] #var auxiliar para guardar 
                #el valor de la j-esima entrada
                array[j] = array[j+1] #la j-esima entrada se cambia
                #por la j+1-esima entrada
                array[j+1] = temp #la ref de la j+1-entrada cambia a la 
                #por el valor de v.aux temp 
    return array

print(bubble_sort([4,2,6,5,1,3]))            
