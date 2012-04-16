#Sum of even-valued terms of the Fibonacci sequence < 4million

i, j = 1, 2 #first two useful terms
sum = 0

while j < 4000000:
	i, j = j, i + j
	if i % 2 == 0:
		sum += i

print sum
