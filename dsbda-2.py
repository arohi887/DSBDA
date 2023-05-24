#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[25]:


df =pd.read_csv('SIT_Student_Information.csv')


# In[26]:


sorted_df = df.sort_values(by='Age')


# In[27]:


print(sorted_df)


# In[28]:


sorted_df = df.sort_values(by='Taluka')


# In[29]:


print(sorted_df)


# In[30]:


transposed_df = df.T


# In[31]:


print(transposed_df)


# In[32]:


df_shape = df.shape


# In[35]:


reshaped_df = df.Age


# In[37]:


print(df_shape)


# In[38]:



print(reshaped_df)


# In[ ]:




