import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir("C:/Users/yh/IBI1_2022-23/Practical7")
# Importing the .csv file works
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
# Show the second column from every 100th row from the first 1000 rows (inclusive)
covid_data.iloc[0:1001:100,1]
# Use a Boolean to show “total cases” for all rows corresponding to Afghanistan
Afghanistan = covid_data["location"]=="Afghanistan"
covid_data.loc[Afghanistan, "total_cases"]


March_31st_data = covid_data.loc[covid_data["date"]=="2020-03-31",["date","location","new_cases","new_deaths"]]
new_data = March_31st_data.drop(index=(March_31st_data.loc[(March_31st_data['location']=='World')].index))
analysis = new_data.describe()
# Computed the mean number of new cases and new deaths on 31 March 2020
analysis.iloc[1,:]


# Create boxplot of new cases and new deaths on 31 March 2020
March_31st_cases = new_data.loc[:,"new_cases"]
March_31st_deaths = new_data.loc[:,"new_deaths"]
plt.title('The new cases on March 31st')
plt.boxplot(March_31st_cases, labels=["new cases"], patch_artist=True, showfliers=False)
plt.show()
plt.title('The new deaths on March 31st')
plt.boxplot(March_31st_deaths, labels=["new deaths"], patch_artist=True, showfliers=False)
plt.show()



# Plot both new cases and new deaths worldwide over time
world_dates = covid_data.loc[covid_data["location"]=="World","date"]
world_new_cases = covid_data.loc[covid_data["location"]=="World","new_cases"]
world_new_deaths = covid_data.loc[covid_data["location"]=="World","new_deaths"]
plt.title('The new cases and new deaths for the whole world over time')
plt.ylabel('number')
plt.xticks(range(0,len(world_dates),4),rotation=-90)
plt.plot(world_dates, world_new_cases, 'bo')
plt.plot(world_dates, world_new_deaths, 'ro')
plt.legend(['new cases','new deaths'])
plt.show()



# Plot both new cases and total cases over time in the UK (to answer the question stated in file question.txt)
UK_dates = covid_data.loc[covid_data["location"]=="United Kingdom","date"]
UK_new_cases = covid_data.loc[covid_data["location"]=="United Kingdom","new_cases"]
UK_total_cases = covid_data.loc[covid_data["location"]=="United Kingdom","total_cases"]
plt.title('The new cases and total cases over time in the UK')
plt.ylabel('number')
plt.xticks(range(0,len(UK_dates),4),rotation=-90)
plt.plot(UK_dates, UK_new_cases, 'bo')
plt.plot(UK_dates, UK_total_cases, 'co')
plt.legend(['new cases','total cases'])
plt.show()