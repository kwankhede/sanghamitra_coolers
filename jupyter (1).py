#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("Sales.csv")
df.head()


# In[4]:


desert_counts = df[df["Model"] == "Desert"]["Size"].value_counts()
print(desert_counts)


# In[5]:


# Total sales of Desert
desert_counts = df[df["Model"] == "Desert"]["Size"].value_counts()

# Plotting a bar chart
plt.figure(figsize=(10, 6))
desert_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Desert Cooler')
plt.xlabel('Desert Model')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Adjust rotation for better visibility
plt.show()


# In[6]:


#Total sales of Ducts
duct_counts = df[df["Model"] == "Duct"]["Size"].value_counts()

# Plotting a bar chart
plt.figure(figsize=(10, 6))
duct_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Desert Cooler')
plt.xlabel('Desert Model')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Adjust rotation for better visibility
plt.show()


# In[15]:


data = pd.read_csv("Max sales.csv")
data.head()


# In[16]:


# Revenue of Coolers
plt.figure(figsize=(8, 8))
plt.pie(data['Total'], labels=data['Size'], autopct='%1.1f%%', startangle=90)
plt.title('Top Sizes by Total')
plt.show()


# In[ ]:




