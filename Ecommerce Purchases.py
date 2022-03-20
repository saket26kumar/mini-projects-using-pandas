#!/usr/bin/env python
# coding: utf-8

# # Mini Project 1-                                                                                                     Here I Extracted the data from datasheet where I used the some pandas functions like (head,tail, mean,value_counts,min,max,split,using of lambda, indexing, using of and, or)

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("C:/Users/kssak/Downloads/archive/Ecommerce Purchases")
df


# ### 1. top 10 data
# ### 2. last 10 data
# ### 3. check type of data
# 

# In[3]:


df.head(10)


# In[4]:


df.tail(10)


# In[5]:


df.dtypes


# ### check null value in dataset

# In[6]:


df.isnull() #isnull gives the value in true and false


# In[7]:


df.isnull().sum() #sum()used here to get total number of null values


# ### how many rows and column in dataset

# In[8]:


df.shape


# In[9]:


len(df.columns)


# In[10]:


len(df)


# In[11]:


df.info()


# ### Highest lowest and average price

# In[12]:


df.head()


# In[13]:


df["Purchase Price"]  #it will give individual columns value


# In[14]:


df["Purchase Price"].max()


# In[15]:


df["Purchase Price"].min()


# In[16]:


df["Purchase Price"].mean()


# ### how many poeple have french language as 'fr' as their laungauge

# In[17]:


df.columns


# In[18]:


df["Language"]=="fr"  #it will give the boolean value for count need to pass data frame


# In[19]:


df[df["Language"]=="fr"]


# In[20]:


len(df[df["Language"]=="fr"])


# In[21]:


df[df["Language"]=="fr"].count()


# ### job title contains engineer

# In[22]:


df.head()


# In[23]:


df["Job"]  #it is a string


# In[24]:


df[df["Job"].str.contains("engineer")]


# In[25]:


len(df[df["Job"].str.contains("engineer")])


# In[26]:


len(df[df["Job"].str.contains("engineer",case=False)]) #it will all the values.


# ### How many People have Mastercard as their Credit Card Provider and made a purchase above 50?

# In[27]:


df.columns


# In[28]:


df[(df["CC Provider"]=="Mastercard") & (df["Purchase Price"]>50)]


# In[29]:


len(df[(df["CC Provider"]=="Mastercard") & (df["Purchase Price"]>50)])


# ###  Find the email of the person with the following Credit Card Number: 4664825258997302

# In[30]:


df.columns


# In[31]:


df[df["Credit Card"]==4664825258997302]["Email"]


# ### How many people purchase during the AM and how many people purchase during PM?

# In[32]:


df.columns


# In[33]:


df["AM or PM"].value_counts()


# ### How many people have a credit card that expires in 2020?

# In[34]:


df.columns


# In[35]:


df['CC Exp Date']


# In[36]:


def fun():
    count=0
    for date in df['CC Exp Date']:
        if date.split("/")[1]=="20":
            count=count+1
    print(count)
                                           #we can create own function or use the lambda function


# In[37]:


fun()


# In[38]:


len(df[df['CC Exp Date'].apply(lambda x:x[3:]=="20")])


# ###  What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
# 

# In[39]:


list=[]
for Email in df['Email']:
    list.append(Email.split("@")[1])


# In[40]:


df["temp"]=list


# In[41]:


df["temp"].value_counts().head()


# In[42]:


df['Email']


# In[43]:


df['Email'].apply(lambda x:x.split("@")[1]).value_counts().head()


# In[ ]:




