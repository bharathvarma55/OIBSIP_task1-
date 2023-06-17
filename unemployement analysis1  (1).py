#!/usr/bin/env python
# coding: utf-8

#  

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_csv("C:/Users/Dell/Desktop/intern/oasis/umeployement/Unemployment in India.csv")
print(data)


# In[5]:


data1=pd.read_csv("C:/Users/Dell/Desktop/intern/oasis/umeployement/Unemployment_Rate_upto_11_2020.csv")
print(data1)


# In[7]:


data.isnull().sum()


# In[8]:


data.tail()


# In[9]:


data1.isnull().sum()


# In[10]:


data1.tail()


# In[11]:


data.shape


# In[12]:


data1.shape


# In[13]:


data.info()


# In[14]:


data1.info()


# In[15]:


data.describe()


# In[16]:


data1.describe()


# In[17]:


a=data.iloc[:,:-1].values
b=data.iloc[:,:-1].values


# In[18]:


from sklearn.model_selection import train_test_split
a_train,b_train,a_test,b_test=train_test_split(a,b,test_size=0.25,random_state=0)


# In[19]:


print(a_train)


# In[20]:


print(a_test)


# In[21]:


x=data1["Region"]
print(x)


# In[22]:


y=data1[" Estimated Unemployment Rate (%)"]
print(y)


# In[23]:


df=data1.iloc[:,-3]
print(df)


# In[24]:


import plotly.express as pex
import matplotlib as plt


# In[25]:


fig = pex.bar(data1,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemployment Rate (State Wise) using Bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[26]:


fig = pex.bar(data1,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemployment Rate (Region Wise) using Bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# In[27]:


fig = pex.histogram(data1,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemployment Rate (State Wise) using Bar Graph',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()

