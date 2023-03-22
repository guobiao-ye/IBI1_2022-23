# Creat variable n to store the number of generations
n=1
# Creat variable i to store the number of rabbits
i=2

# Repeat
while i<100:
	# The total number of rabbits in the next generation is calculated by adding the number of rabbits born
	i=i+i/2*2
	# Calculate for the next generation and stop when the total number of rabbits is greater than or equal to 100
	n=n+1

# Print the number of generations
print (n)
