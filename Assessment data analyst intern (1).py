#!/usr/bin/env python
# coding: utf-8

# In[166]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# reading the excel file to perform various task

# In[167]:



df = pd.read_excel("C:/Users/Mayank Mehta/Desktop/Assessment Data Analyst Intern.xlsx")


# In[168]:


df.rename(columns={"Average maximum heart rate in beats per minute":"Avg heart rate"},inplace=True)
df.drop('Obs',axis=1,inplace=True)


# In[169]:


df


# In[170]:


df.describe()


# here X is a predictor variable and Y is a target variable

# In[171]:


x = df[['Age']]
y = df[['Avg heart rate']]


# Here is the linearRegression for ave and Avg heart rate

# In[172]:


lm=LinearRegression()
model=lm.fit(x,y)


# Now the model has the linear regression of both age and AG heart rate we can find the following R2 and Y_hat from value

# In[179]:


print('R2=',model.score(x,y))


# In[180]:


Y_hat=model.predict(x)
print('Y_hat=',Y_hat)


# here is the visual of the Age and avg heart rate

# In[181]:


plt.scatter(x,y)
plt.title("age vs Avg heart rate")
plt.xlabel('Age')
plt.ylabel('Avg heart rate')
plt.plot(X,Y_hat,color='red')
plt.show()


# here we can see that the straight line shiwn in the grapgh lets the average value for the average age group those points are the point where the red line passes

# In[ ]:




