n=1 # Creat variables n to store the number of regular hexagon sequences
h=0 # Creat variables h to store the number of dots required to make up n hexagons
while n!=6:
	h=2*n*(2*n-1)/2 # Use the formula to caculate the dots number for the nth hexagonal number
	print(h) # Print the dots number
	n=n+1 # Proceed to the calculation of the next graph and stop at the sixth start
