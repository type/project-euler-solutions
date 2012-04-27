#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(inList):
	"""Sum of the square of each number in inList"""
	sum = 0
	for x in inList:
		sum += x * x
	return sum

def squareOfSum(inList):
	"""Square of the sum of all numbers in inList"""
	n = inList[len(inList) -1]
	fullRangeValue = ((1 + n) * n )/ 2
	n = inList[0] - 1
	lowerRangeValue = ((1 + n) * n)/ 2
	sum = fullRangeValue - lowerRangeValue #in case the range didn't begin at 1
	return sum * sum

def differenceInSums(lowerBound, upperBound):
	"""Difference between the square of the sum and the sum of the squares for 
	values in the range between lowerBound and upperBound"""
	myList = range(lowerBound, upperBound + 1)
	return  (squareOfSum(myList) - sumOfSquares(myList))


print differenceInSums(1, 100)
