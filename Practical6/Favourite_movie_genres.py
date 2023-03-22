# Create a dictionary of movie genres and how many students for which this genre is their favourite
dictionary = {'Comedy' : 73, 'Action' : 42, 'Romance' : 38, 'Fantasy' : 28, 'Science-fiction' : 22, 'Horror' : 19, 'Crime' : 18, 'Documentary' : 12, 'History' : 8, 'War' : 7}
# Print the dictionary
print(dictionary)

# Import the matplotlib library
import matplotlib.pyplot as plt
# Set the labels and sizes parameters for the pie chart according to the data in dictionary
labels = list(dictionary.keys())
sizes = list(dictionary.values())
# Create the pie chart and display it
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()


# Ask the user for a movie genre
msg = input("Movie genre: ")
# print the number of students for which this genre is their favourite from the dictionary
dictionary[msg]
