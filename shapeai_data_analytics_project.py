# -*- coding: utf-8 -*-
"""ShapeAI Data-Analytics Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11M01pkeM_BPJh3M2ZcPspBtFIkpmHI48

Initializing the python libraries to the notebook
"""

import pandas as pd
import numpy as np

"""To initialize the train data set into our python program we need to use pandas to first read the csv and to perform operation on train.csv we use pandas-dataframe and creates an object of it."""

df = pd.DataFrame(pd.read_csv('/content/train_data_set/train.csv'))
df.head()

"""df.shape is used to get number of rows and columns present in the csv file or in a dataframe."""

df.shape

"""To check whether there are null values in our csv file, we use functions of dataframe such as null() and to count total number of null values in each row we use sum(), as shown in below code."""

df.isnull().sum()

"""Seperating out the columns which have more than 35% of the null values missing in the dataset."""

# df.isnull().sum() returms a pandas series with column name as the label index
# and total count of null values in the coulmn as it's value
# and we are storing only those columns which have more than 35% of the data missing

r = df.isnull().sum()

drop_col = r[r > (35/100 * df.shape[0])]
drop_col

"""so in above result "cabin" column was the one having empty / null values more than 35%.
Keeping cabin column is no use to us because null are more than data, so neglecting the column "cabin"
"""

drop_col.index

df.drop(drop_col.index, axis=1, inplace=True)
df.shape
df.isnull().sum()

df.fillna(df.mean(), inplace=True)
 df.isnull().sum()

"""Now a column "Embarked" is remained with two null values, beacuse of which Embarked contains string values fillna() was not able to calculate mean of string values."""

df['Embarked'].describe()

"""For the null rows of Embarked coluumn, we fill the NULL values with the most frequent value used in the column i.e.. "S"."""

df["Embarked"].fillna("S", inplace=True)

df.isnull().sum()     
# Now all the NULL values in our dataframe are been removed

df.corr()
# this above line of code returns the correlation between 
# every column with the every column

"""From the above result table, we can easily conclude 
1. the relation between Fare and Pclass i.e.. as per the Pclass the fare was different, such as Pclass1 with high fare, Pclass2 with less fare than Pclass1 and Pclass3 with lesser fare than both the other Pclass fares.

2. We also see the relation between the age and the Pclass which gives conclusion such as passenger which high age were in lower class Pclass3.
---

sibsp : Number of siblings / Spouse Abroad

parch : Number of parents / Childern Abroad

So we can make a new column down with the name family_size by combining these two columns.
"""

df['FamilySize'] = df['SibSp'] + df['Parch']
df.drop(['SibSp', 'Parch'], axis=1, inplace = True)
df.corr()

"""**From the above correlation we can conclude that :**
1. Between Pclass and Survived relation, we see that the less Pclass have high survive rate and high Pclass have less survive rate and the realtion with Survived with the Fare says that the passengers with high fare price has high survival ratio

concluding with above two different relation we can say that the Pclass with moderate fare price have high survival rate than other passengers.

2. Relation betn FamilySize and Survived, does not have much correlance with survival rate.

Lets check wether the person was alone or not and wether it affect the survival rate or not
"""

df['Alone'] = [0 if df['FamilySize'][i] > 0 else 1 for i in df.index]
df.head()

df.groupby(['Alone'])['Survived'].mean()

"""Frome above result we conclude that,
if the person was alone then there has less chance of survival rate

---
The reason might be the person who is travelling with his family might be belonging to rich class and might be prioritized over other.

"""

df[['Alone', 'Fare']].corr()

"""So we can see if the person is not alone, then he/she must be having high fare price and the survival rate of that person would also be high."""

df.groupby(['Sex'])['Survived'].mean()

"""It shows that the female passengers have more chances of the survival that the male passengers.

It shows women are prioritized over men.
"""

df.groupby(['Embarked'])['Survived'].mean()

"""We see that people having the embarkation port as "C" has high survival rate than others.

# New Section

**CONCLUSION**

---
*  Female passengers were prioritized over men
*  Passengers travelling with their family have higher survival rate.
*  Passengers who are borded the ship at Cherbourg, survived more in proportion then the others.
*  People with higher class or rich people have higher survival rate than others.
"""