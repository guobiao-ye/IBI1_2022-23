# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the number of data points, and the data itself of corresponding cost
N = 8
costs = [1, 8, 15, 7, 5, 14, 43, 40]
# Set up the plot
ind = np.arange(N)
width = 0.35
pl = plt.bar(ind, costs, width)
# Set the title and axis labels for the plot
plt.ylabel('costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('Los Angeles', 'Seoul', 'Barcelona', 'Atlanta', 'Sydney', 'Athens', 'Beijing', 'London'), rotation=45)
# Set the length and scale of the vertical axis
plt.yticks(np.arange(0, 51, 10))

# Display the plot
plt.show()
# Print the costs
print(costs)
