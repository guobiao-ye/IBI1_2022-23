# Creat variables n to store the number of regular hexagon sequences
n=1
# Creat variables h to store the number of dots required to make up n hexagons
h=0

# Repeat
while n!=6:
	# Use the formula to caculate the dots number for the nth hexagonal number
	h=2*n*(2*n-1)/2
	# Print the dots number
	print(h)
	# Proceed to the calculation of the next graph and stop at the sixth start
	n=n+1
