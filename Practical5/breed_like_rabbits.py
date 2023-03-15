n=1 # Creat variable n to store the number of generations
i=2 # Creat variable i to store the number of rabbits
while i<100:
	i=i+i/2*2 # The total number of rabbits in the next generation is calculated by adding the number of rabbits born.
	n=n+1 # Calculate for the next generation and stop when the total number of rabbits is greater than or equal to 100
print (n) # Print the number of generations
