x = [23,4,12,1,31,14]

def selection_sort(my_list):
    len_list = len(my_list)
    for i in range(len_list):
        min_index = i
        for j in range(i+1,len_list):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print selection_sort(x)