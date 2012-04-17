#Find the largest palindrome made from the product of two 3-digit numbers


def testPalindrome(n):
	"""Tests if a number is a palindrome"""
	reg = str(n)
	rev = reg[::-1]
	if reg == rev:
		return True

#Unused but works; string technique is faster than parsing out digits
def intToList(a):
	"""Converts an integer into its individual digits"""
	ints = []
	while a != 0:
		ints.insert(0, a % 10)
		a = a / 10
	return ints

def findHighestPal(left=999, right=999):
	max = 0
	for i in xrange(100, left):
		for j in xrange(100, right):
			val = i * j
			if testPalindrome(val):
				if val > max:
					max = val
	print max

findHighestPal()
