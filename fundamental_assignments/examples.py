for i in users:
	print users[i]
	for a in users[i]:
		print a


for i in users:
	for key, value in enumerate(users[i]):
	print key
		enumerate will number each value starting from 0
	print key + 1 will number each value starting from 1