import time
from decimal import Decimal

def pal(x) : # <int>
	""" Return the palindrome of a int number x. """

	x = int(x)
	num = x
	m = 0

	while num > 0 :
		m = m*10 + num%10
		m = int(m)
		num = num // 10
		num = int(num)  
	return m # <int>

def ispal(x) : # <int>
	"""Palindrome detector.
	Return True if it's a palindrome, False otherwise."""

	x = int(x)
	num = x
	m = 0

	while num > 0 :
		m = m*10 + num%10
		m = int(m)
		num = num // 10
		num = int(num)
	
	if m == x :
		return True # <bool>
	else :
		return False # <bool>

def lychrel(x, detailed = False) : # <int>
	""" Function carrying out the sequences of operations 
	leading to the palindrome.
	- The intermediate stages of the operation are inserted in a 
	list until the palindrome is obtained. 
	- By default, only the result of intermediate operations is 
	added to the list, but a more detailed display of the 
	calculations is possible by setting 'detailed = True', 
	in this case, each addition and its result appear in tulps.
	- A duration in seconds is allocated to the calculation, 
	beyond this allotted time the process stops, meaning that 
	the number inserted is potentially a Lychrel number"""

	x = int(x)
	nbr = x # x = initial value, nbr = value to handle
	wd = 5 # Time allowed for calculation (sec)
	L = []
	start_time = time.time()
   
	while True :
		res = nbr + pal(nbr)
		
		# Time control (potential Lychrel number)
		exe_time = time.time()
		if exe_time >= start_time + wd :
			res = Decimal(res) #to print scientific notation
			stop = []
			stop.append("ITER. STOP")
			stop.append(wd)
			stop.append("{:.2e}".format(res))
			stop.append(x)
			L = []
			L.append(stop)
			break

		# It's a palindrome
		if ispal(res) == True :
			if detailed == True:
				L.append([nbr, pal(nbr), res])
			else:
				L.append(res)
			break

		# NOT a palindrome
		elif ispal(res) == False :
			if detailed == True:
				L.append([nbr, pal(nbr), res])
			else:
				L.append(res)

			nbr = res
			continue

	return L # <list>

if __name__ == "__main__" :
	print("192 (default output) : ", lychrel(192))
	print("192 (detailed output) : ", lychrel(192, detailed=True))
	print("196 :", lychrel(196))