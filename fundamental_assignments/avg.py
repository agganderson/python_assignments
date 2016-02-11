# a = [1, 2, 5, 10, 255, 3]
# b = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
# print b/len(a)

# OR 

a = [1,2,5,10,255,3]
sum = 0
for num in a:
    sum += num

print sum/len(a)