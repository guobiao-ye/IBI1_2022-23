# Store the longitude of Edinburgh in a variable called a
a = -3.19
# Store the longitude of Los Angeles in a variable called b
b = -118.24
# Store the longitude of Haining in a variable called c
c = 116.39
# Calculate the longitude distance that Rob travelled to Los Angeles as the difference between a and b. Store this value in a variable called d
d = a-b
# Calculate the longitude distance that Rob travelled to Haining as the difference between and a c. Store this value in a variable called e
e = a-c

# Judge whether Rob travelled further to Los Angeles or Haining
if abs(d) > abs(e):
	print("Los Angeles")
elif abs(d) == abs(e):
	print("As far away")
elif abs(d) < abs(e):
        print("Haining")

# Create variable X to store Boolean variables True
X = True
# Create variable Y to store Boolean variables False
Y = False
# Creat W to encode the Boolean variables “X an Y"
W = X and Y
# Creat Z to encode the Boolean variables “X or Y"
Z = X or Y

# Print the value of W and Z separately
print("The value of W is " , W)
print("The value of Z is " , Z)
