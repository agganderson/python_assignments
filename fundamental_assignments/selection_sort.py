x = []

def selection_sort(my_list):
	count = 0
	swap = True
	while swap == True:
		swap = False
		number_list = len(my_list) - count - 1
		for i in range(number_list):
			if my_list[i] > my_list[i + 1]:
				temp = my_list[i]
				my_list[i] = my_list[i + 1]
				my_list[i + 1] = temp
				swap = True
		return my_list
print selection_sort(x)