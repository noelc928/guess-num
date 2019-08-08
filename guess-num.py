import random
r = random.randint(1,100)
while True:
	g = input('Please guess the number: ')
	g = int(g)
	if g == r:
		print('Correct!!!')
		break
	elif g > r:
		print('It’s larger than answer')
	elif g < r:
		print('Its’ smaller than answer')
