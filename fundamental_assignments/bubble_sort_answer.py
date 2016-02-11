x = [10,2,65,8,1,7]  #give a list

def bubble_sort(my_list): #define the bubble sort function
    count = 0 #create a variable count
    swapped = True #create a true/false variable
    while swapped == True: #begin while loop
        swapped = False 
        num_elements = len(my_list) - count - 1 #as long as the number of elements in my_list is the length of the list
        for i in range(num_elements): #for loop num_elements = numbers in list i = index
            if my_list[i] > my_list[i+1]: #checks if the current index is lowest, if it is..
                temp = my_list[i] #creates temp placeholder containing number
                my_list[i] = my_list[i + 1] #switches compared numbers
                my_list[i + 1] = temp #uses temp to change number in list
                swapped = True #
    return my_list #returns new list
 
print bubble_sort(x) #prints your list with function you made