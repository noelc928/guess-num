import random
a = input('Please state the smallest number:')
b = input('Please state the largest number:')
r = random.randint(int(a),int(b))
count = 0
while True:
	count += 1
	print ('This is the', count, 'times you guess')
	g = input('Please guess the number: ')
	g = int(g)
	if g == r:
		print('Correct!!!')
		break
	elif g > r:
		print('It’s larger than answer')
	elif g < r:
		print('Its’ smaller than answer')