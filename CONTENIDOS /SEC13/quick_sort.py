from pivot import partition 

def quick_sort(array,pivot_index,end_index):
    #caso base 
    if len(array) == 1:
        return array 

    ####### CASO RECURSIVO ########
    if pivot_index < end_index:
        p = partition(array, pivot_index, end_index)
        quick_sort(array,pivot_index,p-1)
        quick_sort(array,p+1,end_index)

my_list = [4,6,1,7,3,2,5]
print(my_list)
quick_sort(my_list,0,6)
print(my_list)               
