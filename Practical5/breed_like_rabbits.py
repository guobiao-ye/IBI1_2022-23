n=1 #n is the number of generations
i=2 #i is the number of rabbits
while i<100:
	i=i+i/2*2 #The total number of rabbits in the next generation is calculated by adding the number of rabbits born.
	n=n+1
print (n)
