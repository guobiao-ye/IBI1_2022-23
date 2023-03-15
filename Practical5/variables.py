a = -3.19 # Store the longitude of Edinburgh in a variable called a
b = -118.24 # Store the longitude of Los Angeles in a variable called b
c = 116.39 # Store the longitude of Haining in a variable called c
d = a-b # Calculate the longitude distance that Rob travelled to Los Angeles as the difference between a and b. Store this value in a variable called d
e = a-c # Calculate the longitude distance that Rob travelled to Haining as the difference between and a c. Store this value in a variable called e
if abs(d) > abs(e):
	print("Los Angeles")
elif abs(d) == abs(e):
	print("As far away")
elif abs(d) < abs(e):
        print("Haining")
# Describing whether Rob travelled further to Los Angeles or Haining

X = True # Create variable X to store Boolean variables True
Y = False # Create variable Y to store Boolean variables False
W = X and Y # Creat W to encode the Boolean variables “X an Y"
Z = X or Y # Creat Z to encode the Boolean variables “X or Y"
print("The value of W is " , W)
print("The value of Z is " , Z)
# Print the value of W and Z separately
