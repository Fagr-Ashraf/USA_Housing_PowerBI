#!/usr/bin/env python
# coding: utf-8

# # import Libraries

# In[221]:


# import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings('ignore')


# # data overview

# In[222]:


df=pd.read_csv('housing.csv')


# In[223]:


pd.set_option('display.max_columns', None)


# In[224]:


df.shape


# In[225]:


df.head()


# In[226]:


df.tail()


# In[227]:


print(df.columns.tolist())


# In[228]:


df.describe()


# # Checks Nulls and duplicates

# In[229]:


print(df.isnull().sum())


# In[230]:


df['long'].fillna(df['long'].mean(), inplace=True)
df['lat'].fillna(df['lat'].mean(), inplace=True)
df['laundry_options'].fillna(df['laundry_options'].mode()[0], inplace=True)
df['parking_options'].fillna(df['parking_options'].mode()[0], inplace=True)
print(df.isnull().sum())


# In[231]:


df.duplicated().sum()


# # Drop unNecessary

# In[232]:


df.drop(columns=['description','image_url','region_url','url','id'],inplace=True)


# In[233]:


df.head()


# In[234]:


df['region'].unique()


# In[235]:


df['region'].value_counts()


# In[236]:


df['region'] = df['region'].str.replace('/', '-')


# In[237]:


df['type'].unique()


# In[238]:


df['laundry_options'].unique()


# In[239]:


df['parking_options'].unique()


# In[240]:


df.select_dtypes(include=['object']).columns


# # Outliers

# In[241]:


df['lat'].max()


# In[242]:


df['lat'].min()


# In[243]:


df['long'].max()


# In[244]:


df['long'].min()


# In[245]:


sns.boxplot(x='lat', data=df)


# In[246]:


sns.boxplot(x='long', data=df)


# In[247]:


q1 = np.percentile(df['lat'], 25)
q3 = np.percentile(df['lat'], 75)
iqr = (q3 - q1) * 1.5
df['lat'] = np.where(df['lat'] < (q1 - iqr), q1 - iqr, df['lat'])
df['lat'] = np.where(df['lat'] > (q3 + iqr), q3 + iqr, df['lat'])


# In[248]:


q1 = np.percentile(df['long'], 25)
q3 = np.percentile(df['long'], 75)
iqr = (q3 - q1) * 1.5
df['long'] = np.where(df['long'] < (q1 - iqr), q1 - iqr, df['long'])
df['long'] = np.where(df['long'] > (q3 + iqr), q3 + iqr, df['long'])


# In[249]:


sns.boxplot(x='long', data=df)


# In[250]:


sns.boxplot(x='lat', data=df)


# In[251]:


df.head()


# # Mapping 

# In[252]:


df['cats_allowed'].unique()


# In[253]:


mapp={0:'No',1:'Yes'}
df['cats_allowed'] = df['cats_allowed'].map(mapp)
print(df['cats_allowed'].value_counts())


# In[254]:


df['dogs_allowed'].unique()


# In[255]:


mapp={0:'No',1:'Yes'}
df['dogs_allowed'] = df['dogs_allowed'].map(mapp)
print(df['dogs_allowed'].value_counts())


# In[256]:


df['smoking_allowed'].unique()


# In[257]:


mapp={0:'Not Allowed',1:'Allowed'}
df['smoking_allowed'] = df['smoking_allowed'].map(mapp)
print(df['smoking_allowed'].value_counts())


# In[258]:


df['wheelchair_access'].unique()


# In[259]:


mapp={0:'No',1:'Yes'}
df['wheelchair_access'] = df['wheelchair_access'].map(mapp)
print(df['wheelchair_access'].value_counts())


# In[260]:


df['electric_vehicle_charge'].unique()


# In[261]:


mapp={0:'No',1:'Yes'}
df['electric_vehicle_charge'] = df['electric_vehicle_charge'].map(mapp)
print(df['electric_vehicle_charge'].value_counts())


# In[262]:


df['comes_furnished'].unique()


# In[263]:


mapp={0:'No',1:'Yes'}
df['comes_furnished'] = df['comes_furnished'].map(mapp)
print(df['comes_furnished'].value_counts())


# In[264]:


df.head()


# In[267]:


df['laundry_options'].value_counts()


# In[269]:


df['state'].value_counts()


# In[271]:


df['region'].value_counts()


# In[ ]:


df.to_csv('preprocessed_data.csv', index=False)

