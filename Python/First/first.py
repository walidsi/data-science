# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import datetime as dt
import re
import os
import sys
import numpy as np
import pandas as pd
#sets up pandas table display
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.expand_frame_repr', False) # do not wrap dataframe colums
pd.set_option('display.notebook_repr_html', True)
# Plot
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


print("Hello World!", "Love you!")

print(1)

# set
drinks_set = set(["Tea", "Coffee", "Soda", "Alcohol"])
print(drinks_set)
print(sorted(drinks_set))

# dictionary
birthdays_dict = {"Walid": 1971, 
                  "Hatem": 1976, 
                  "Rehab": 1977, 
                  "Dad": 1937, 
                  "Mom": 1948, 
                  "Farida": 2011, 
                  "Malak": 2013}

print(birthdays_dict["Walid"])
print(sorted(birthdays_dict))

first_list = ["Walid", "Hatem", "Rehab", "Farida", "Malak"]
print(first_list)
first_list.sort()
print(first_list)

# sets
first_set = set([1, 2, 3, 4, 5])
second_set = {4, 5, 6, 7, 8}

print(first_set.intersection(second_set))
print(first_set.union(second_set))
print(first_set.difference(second_set))

# data frame aka table
data = {'album': ['Thriller', 'Back in Black', 'The Dark Side of The Moon'],
        'year': [1982, 1980, 1973],
        'sales': [46.0, 26.1, 24.2]}

df = pd.DataFrame(data)
print(df)
print(df[1:2])
df['genre'] = ['pop, rock, R&B', 'hard rock', 'progressive rock']
print(df)

# date and time
today = dt.date.today()
print(today)
print(today.ctime())

now = dt.datetime.now()
print(now)

# strings
str = "This is a test string"
print(str.upper())
print(str.lower())
print(str.replace(" ", "-"))
print(str)
word_list = str.split()
print(word_list)

# Regular expressions
Email_text = "doej@example.com jadoe@sample.ca qsus@example.br joes@sample.com"
pattern = r'([A-Z0-9.-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
match = regex.match('abc@pattern.com')
match.groups()
search_string = regex.findall(Email_text)
print(pattern, regex, match, match.groups(), search_string)

# read file as text
print(os.getcwd())
myfile = open('Book1.csv')
file_contents = myfile.read()
myfile.close()
#print(file_contents)


# read csv file .. for some reason it needs to be a text file in UTF-8 format !!!
csvsample = pd.read_csv('Book1.csv')
print(csvsample)

matrix1 = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
print('matrix1 = \n', matrix1)
matrix1[:,1:] = 100 # set column 1 and and all following columns to 100
print('matrix1 with columns 1 and up set to 100 \n', matrix1)
size_tuple = matrix1.shape # tuple containing array rows and columns
print(len(size_tuple))
# get number of rows and columns in  array
for x in size_tuple:
    print(x)

matrix2 = np.matrix([[2,3], [5,6], [8,9]])

print('matrix2 = \n', matrix2)
print('matrix2 tranpose view = \n', matrix2.transpose())
matrix3 = matrix1 * matrix2
print('matrix3 = \n', matrix3)

matrix3 = matrix1.T * matrix2
print(matrix3, '\n')

# array3

array11 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('array11 = \n', array11)

array22 = np.array([[2,3], [5,6], [8,9]])

print('array22 = \n', array22)
print('array22 tranpose view = \n', array22.transpose())
print('array22 again = \n', array22, '\nnotice it is the same')

array33 = np.dot(array11, array22)

print('array33 = \n', array33)

# vectors
vector1 = np.matrix([1, 2, 3])
print('vector1 = \n', vector1)
vector2 = vector1.transpose()
print('vector2 = \n', vector2, '\nvector1 = \n', vector1)
print(vector2)

print('hello')


# Plot

# read csv file .. for some reason it needs to be a text file in UTF-8 format !!!
csvsample = pd.read_csv('World_Info.csv')
print(csvsample)

gdp_cap = csvsample['GDP Per Capita']
life_exp = csvsample['Life Expentancy']
pop = csvsample['Population']
col = csvsample['Continent']

# Scatter plot
plt.figure('GDP per Capita [in USD]')
plt.scatter(x = gdp_cap, 
            y = life_exp, 
            s = np.array(pop) * 2, 
            c = col, 
            alpha = 0.8)

# Previous customizations
plt.ion()
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
plt.pause(1)

# random coin tosses of 10 times each, simulated 10000 times
np.random.seed(123)
final_tails = [0]
for y in range(10000):
    tails = [0]
    for x in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
        #print(coin, tails)
    final_tails.append(tails[-1])
#print(final_tails)

bins = np.arange(12) - 0.5
print(bins)
plt.figure('Histogram')
plt.hist(final_tails,bins = bins, rwidth=0.8)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.show()
plt.pause(1)

np.random.seed(123)
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)
print(np_aw)
# Plot np_aw and show
plt.figure('Random Walk')
plt.plot(np_aw)
plt.show()
plt.pause(1)
# Clear the figure
#plt.clf()



# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
print(np_aw_t)
# Plot np_aw_t and show
plt.figure('Better Random Walk')
plt.plot(np_aw_t)
plt.xlabel('Dice Throws')
plt.ylabel('Steps accomplished')
plt.show()
plt.pause(1)




pd.DataFrame()
