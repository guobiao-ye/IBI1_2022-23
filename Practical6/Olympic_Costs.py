import matplotlib.pyplot as plt
import numpy as np

N = 8
costs = [1, 8, 15, 7, 5, 14, 43, 40]
ind = np.arange(N)
width = 0.35
pl = plt.bar(ind, costs, width)
plt.ylabel('costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('Los Angeles', 'Seoul', 'Barcelona', 'Atlanta', 'Sydney', 'Athens', 'Beijing', 'London'), rotation=45)
plt.yticks(np.arange(0, 51, 10))

plt.show()
print(costs)
