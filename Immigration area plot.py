! pip3 install openpyxl
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

#To look at the first five items in dataset
df_can.head()

#Find number of entries in dataset
# print the dimensions of the dataframe
print(df_can.shape)

#Clean dataset to remove columns that are not informative for visualization (eg. Type, AREA, REG). 

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# let's view the first five elements and see how the dataframe was changed
df_can.head()

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

# view the first five elements and see how the dataframe was changed
df_can.head()

# examine the types of the column labels
all(isinstance(column, str) for column in df_can.columns)

df_can.columns = list(map(str, df_can.columns))

# let's check the column labels types now
all(isinstance(column, str) for column in df_can.columns)

df_can.set_index('Country', inplace=True)

# Let's view the first five elements and see how the dataframe was changed
df_can.head()

df_can['Total'] = df_can.sum(axis=1)

# let's view the first five elements and see how the dataframe was changed
df_can.head()

print('data dimensions:', df_can.shape) # dataframe has 38 columns instead of previous 37 

# create a list of years from 1980 - 2013 which will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')  # optional: for ggplot-like style

# check for latest version of Matplotlib
print('Matplotlib version: ', mpl.__version__) # >= 2.0.0

# Change the index values of df_top5 to type integer for plotting -- an area plot for Trend of Top 5 Countries
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='area',
             stacked=False,
             figsize=(20, 10))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


### Area Plot for Immigration Trend of 5 Countries with Lowest Immigration Rates

df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_least5 = df_can.tail(5)

# transpose the dataframe
df_least5 = df_least5[years].transpose()

df_least5.tail()

df_least5.index = df_least5.index.map(int)
df_least5.plot(kind='area', alpha=0.45, stacked=False, figsize=(20, 10))

plt.title('Immigration Trend of 5 Countries with Lowest Immigration Rates')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()
