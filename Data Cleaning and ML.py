#Use of the zip function to combine lists

#This case is one str and one int
rank = list(range(1,4))
rank = map(str, rank)
film_title = ['The Godfather', 'Pulp Fiction', 'Parasite']

final = [x + ' ' + i for x, i in zip(rank, film_title)]

for x in final:
  print(x)

#Loop through previous list and append to new
film_title2 = []

for x in film_title:
  x = 'Title: ' + x
  film_title2.append(x)

print(film_title2)

#Create a function that takes in a str and returns with smart remark
def bs(str):
  print(str + ' is heckin bologna.')

bs('Coca cola')

#Create a function that takes in a int and returns plus 1
def plus_one(int):
  print(int + 1)

plus_one(56)

#Plotting with pandas and pyplot with manual data frame
from pandas import DataFrame
import matplotlib.pyplot as plt
plt.style.use('ggplot')
   
Data = {'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545]
       }
  
df = DataFrame(Data,columns=['Year','Stock_Index_Price'])
df.plot(x ='Year', y='Stock_Index_Price', kind = 'line', color='red')

plt.title('Stock Prices 2014-2020')
plt.show()

#Plotting with pandas and pyplot with CSV datafile
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
plt.style.use('ggplot')

Data = pd.read_excel(r'C:\Users\keith\Downloads\baa10k.xlsx')

df = DataFrame(Data,columns=['age','time_minutes'])
df = df.sample(n=30)
df.plot(x ='time_minutes', y='age', kind = 'scatter')
plt.title('10k Runtime Based on Age')

plt.show()

#Here are the different plot kind options:

"""
kind : str

‘line’ : line plot (default)
‘bar’ : vertical bar plot
‘barh’ : horizontal bar plot
‘hist’ : histogram
‘box’ : boxplot
‘kde’ : Kernel Density Estimation plot
‘density’ : same as ‘kde’
‘area’ : area plot
‘pie’ : pie plot
‘scatter’ : scatter plot
‘hexbin’ : hexbin plot
"""

#Histogram example
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
plt.style.use('ggplot')

Data = pd.read_excel(r'C:\Users\keith\Downloads\baa10k.xlsx')

df = DataFrame(Data,columns=['time_minutes'])
df.plot.hist(bins=12, alpha=0.5)
plt.title('10k Runtimes')

plt.show()

#Simple linear regression and predictive modeling
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.style.use('ggplot')

Data = pd.read_csv(r'C:\Users\keith\Downloads\mtcars.csv')

df = DataFrame(Data,columns=['mpg', 'wt'])
x = df['wt'].values.reshape(-1, 1)
y = df['mpg'].values.reshape(-1, 1)

linear_regressor = LinearRegression() 
linear_regressor.fit(x, y)  
prediction = linear_regressor.predict(x)  

plt.scatter(x, y, color='blue', alpha=.5)
plt.plot(x, prediction, color='red')
plt.title('Linear Regression of Vehicle MPG and Weight')
plt.xlabel('Weight (tons)')
plt.ylabel('MPG')

plt.show()

#Set new x for y prediction
x_new = [[4.5]]
fit = linear_regressor.fit(x, y)  

print(fit.predict(x_new))
