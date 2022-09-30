from pivot import partition 

def quick_sort_helper(array,pivot_index,end_index):
    #caso base 
    if len(array) == 1:
        return array 

    ####### CASO RECURSIVO ########
    if pivot_index < end_index:
        p = partition(array, pivot_index, end_index)
        quick_sort_helper(array,pivot_index,p-1)
        quick_sort_helper(array,p+1,end_index)
    return array 

def quick_sort(array):
    return quick_sort_helper(array, 0, len(array)-1)        

my_list = [4,6,1,7,3,2,5]
print(my_list)
print(quick_sort(my_list))          
