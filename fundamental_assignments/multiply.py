#answer

a = [3,5,6,1,8]
def multiply(arr):
	for i in range(len(arr)):
		arr[i] = arr[i] * 5
	return arr
b = multiply(a)
print b


