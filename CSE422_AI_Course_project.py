
Original file is located at
    https://colab.research.google.com/drive/1eyeVh4fveeVIupTUNxW1VXOCWjMyYoy1

Welcome to our CSE 422 Final Lab Project

# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
import numpy as np
import sklearn
from matplotlib import pyplot as plt
# %matplotlib inline
import matplotlib

"""Firstly we imported the necessary libraries such as pandas sklearn for our algorithm"""

from google.colab import files
uploaded = files.upload()

"""Here we have uploaded our dataset's csv file"""

df = pd.read_csv('COVID-19_Death_Counts_by_Sex__Age__and_State.csv')
df.head(2)

"""Here we assigned our uploaded dataset into a Table named df & we checked the first 3 Data entries of our table"""

df.shape

"""To check the the total number of columns & rows we used the .shape method"""

df.columns

"""Here we checked the names of each of the features"""

df['Pneumonia Deaths'].value_counts()

"""Bakhtriar's Part (Data Visualization) 

"""

x_data= range(0, df.shape[0])
print(x_data)#0-2661
fig=plt.figure() #object
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(x_data, df['COVID-19 Deaths'], marker='v', color='g')

columns = ['Total Deaths', 'Pneumonia, Influenza, or COVID-19 Deaths']
print(type(columns))

x_data= range(0, df.shape[0]) #row shape


fig=plt.figure()
fig, ax = plt.subplots(figsize=(20,15))

for c in columns:
  ax.plot(x_data, df[c])
ax.set_title('Covid dataset')

# create a figure and axis
fig, ax = plt.subplots(figsize=(20,10))
ax.scatter(df['Age group'], df['COVID-19 Deaths']) #showing scatter Age group against COVID-19 Deaths

# set a title and labels
ax.set_title('Covid Dataset')
ax.set_xlabel('Age group')
ax.set_ylabel('COVID-19 Deaths')

import seaborn as sns
co = df.corr() 
print(co)
sns.heatmap(co)

fig=plt.figure(figsize=(20,10))
fig, sns.barplot(data=df, x="Age group", y="Total Deaths", hue= "Sex")

fig=plt.figure(figsize=(20,10))

fig, sns.pairplot(df)

"""# Ibrahim Khan- 18201152 - Feature selection(Pre processing)

To preprocess our dataset , we have to check for missing data entries or entries which are NOt relevant to achieving our Goal. So we have to Select Features which are related to our goal & impute null data entries.

After Following the 'Feature selection tutorial' We checked for all the relevant features & found out that the 'Data as of' & 'FootNote' features are not related to our algorithm's output.

Here we are keeping data which are relevent and necessary for our desired outcome. so we will remove data which are useless to us and here 'date of as' and 'footnote' will be dropped. as date as of and footnote won't help us to get the desired result.
"""

df = df.drop(['Data as of', 'Footnote'], axis = 1)

df.head()

"""We can check for null data entries in our dataset using the isnull() function"""

df.isnull()

"""# Asef hassan Amiz- 16321088 - Imputing missing values (pre processing)

This displays a Truthtable where if any cell contains any null/missing entry then it returns True for that cell, else false,

However since it is a Huge dataset it will take a long time to see each and every table rows serially to scan for nulls,
Hence to detect null values more efficiently we will use the function -

.isnull().sum() which will show us the total number of null entries present under a single Column
"""

df.isnull().sum()

"""We can see that the Remaining columns after Feature selection still have many missing data entries under them,

So to solve this issue what we can do is drop the rows which include any null value in it.
"""

df = df[df['COVID-19 Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df = df[df['Total Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df = df[df['Pneumonia Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df = df[df['Pneumonia and COVID-19 Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df = df[df['Influenza Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df = df[df['Pneumonia, Influenza, or COVID-19 Deaths'].notnull()]
print("Shape  after removing null values: ", df.shape)

df.isnull().sum()

"""So now our dataset has no missing values in it anymore , and all the featueres rema

# Ibrahim Khan ID - Encoding Categorical Features (pre-processing)
"""

df.info()

from sklearn.preprocessing import LabelEncoder 
#importing lavelencoder from sklearn
enc = LabelEncoder()

df['Sex_enc'] = enc.fit_transform(df['Sex'])
#Encoding the sex column into a numeric values
Sex_enc = pd.get_dummies(df['Sex'])
print(df['Sex'].unique())
print(df['Sex_enc'].unique())

"""we have encoded a column by Labelencoder() method and stored the encoded values in a different column sex_enc . and then state column into state_enc and same goes for age group
Here, I have divided unique categories into dummy column and stored one_hot values in each coresponding column with just 1. 
"""

df['State_enc'] = enc.fit_transform(df['State'])
#transforming state column into state_enc column with encoded values
State_enc = pd.get_dummies(df['State'])
print(df['State'].unique())
print(df['State_enc'].unique())

df['Age group_enc'] = enc.fit_transform(df['Age group'])
#transforming state column into encoded
Age_group_enc = pd.get_dummies(df['Age group'])
print(df['Age group'].unique())
print(df['Age group_enc'].unique())

"""here, i am doing the same encoding and dummies for State and Age group columns."""

df.info()
df.head()

"""lastly i checked the info of the data in the dataset and printed first 5 rows to see the updated data.

MD. Omar Hasan Akash ID - 16301178- Machine Learning 
---
"""

df = pd.read_csv('COVID-19_Death_Counts_by_Sex__Age__and_State.csv', usecols=["COVID-19 Deaths", "Total Deaths", "Pneumonia Deaths", "Pneumonia and COVID-19 Deaths"])
df.head(2)

"""read the csv again and see the values. as a group project, everyone do their own part."""

df.shape

"""df.shape will give the entries information of the dataframe."""

df.isnull().sum()

"""finding the null values for each columns"""

print('NaN values: ', df.isnull().values.sum())

"""we tried to find the number of nan values.. here it shows 1001"""

print(df.iloc[40])

"""df.iloc is used to access data in specific row or columns, using iloc we can access values in specific row column entries"""

# Mean imputation
imputated_df = df.fillna(value=df.mean())
imputated_df.isnull().sum()

print(imputated_df.isnull().values.sum())

imputated_df.info()

imputated_df.describe()

print(imputated_df['COVID-19 Deaths'])

imputated_df.iloc[40]

from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split

X = np.array(imputated_df['COVID-19 Deaths']).reshape(-1, 1)
y = np.array(imputated_df['Total Deaths']).reshape(-1, 1)

"""I randomly picked up two columns which is Covid-19 deaths, and total deaths to apply linear regression, I can also take other columns but taking these two columns seem reasonable to me."""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

"""generating train and test sets, the test size 0.25 is chosen as an ideal, but it can also perform well on 1/3 or .33 values"""

regr = LinearRegression() 
  
regr.fit(X_train, y_train) 
print(regr.score(X_test, y_test))

y_pred = regr.predict(X_test) 
plt.scatter(X_test, y_test, color ='b') 
plt.plot(X_test, y_pred, color ='k')

"""The plotting hardly try to differentiate the two values, but for this kind of dataset it works well."""

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='plasma')

"""This is visualization how the large number of null values exist in our dataset. As a beginner it was challenging for us to identify the issue first, but we tried our best to apply our hands on skill to apply everything we have learned so far.

sns heatmap basically, map the nan values in every columns, the colors you see is the nan values.
"""
