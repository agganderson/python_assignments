#Part 1

x = [1, 4, 6, 8]

def draw_stars_1(x_list):
	for star in x_list:
		output = ''
		for i in range(star):
			output += '*'
		print output

draw_stars_1(x)


#Part 2

second = [2,8,"harry",9,5,"edith","akmu"]

def draw_stars_2(second_list):
	for star in second_list:
		output = ''
		if type(star) is int:
			for i in range(star):
				output += '*'
			print output
		elif type(star) is str:
			first_letter = star[0].lower()
			for i in range(len(star)):
				output += first_letter
			print output

draw_stars_2(second)

