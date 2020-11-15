#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1

import pandas as pd
print(pd.__version__)


# In[4]:


# Question 2
import numpy as np

arr = np.array(["Apple" , "Mango" , "Orange" , "Grapes"])
a = pd.Series(arr)
print(a)


# In[27]:


#Question 3


a = pd.Series({'Roll Number': ['20CSE29', '20CSE49', '20CSE36', '20CSE44'],
               'Name': ['Amelia', 'Sam', 'Dean', 'Jessica'],
               'Marks In Percentage': [97, 90, 70, 82], 
               'Grade': ['A', 'A', 'C', 'B'], 
               'Subject': ['Physics', 'Physics', 'Physics', 'Physics']}) 

df = pd.DataFrame(a)
df['index'] = df.index 
df


# In[30]:


# Question 4

import seaborn as sbn

sbn.get_dataset_names()
data =sbn.load_dataset('mpg')

data


# In[34]:


# Question 5

data['origin'].unique()


# In[38]:


# Question 6

x = data["origin"] == "usa"
data[x]


# In[ ]:




