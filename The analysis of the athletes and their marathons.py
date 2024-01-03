#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


pip install pandas


# In[4]:


pip install seaborn


# In[5]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[6]:


df.head(10)


# In[7]:


df.shape


# In[8]:


df.dtypes


# In[9]:


# To clean data
# Analyzing USA Races, 50k or 50Mi, 2020


# In[10]:


#Step 1  show 50Mi or 50k
#50km
#50mi


# In[11]:


df[df['Event distance/length'] == '50km']


# In[12]:


df[df['Event distance/length'] == '50mi']


# In[13]:


#combining 50k/50mi with isin


# In[14]:


df[(df['Event distance/length'].isin(['50mi','50km'])) & (df['Year of event'] == 2020)]


# In[15]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[16]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


# In[17]:


#COMBINE ALL THE FILTERS TOGETHER


# In[18]:


df[(df['Event distance/length'].isin(['50mi','50km'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[19]:


df2 = df[(df['Event distance/length'].isin(['50mi','50km'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[20]:


df2.head(10)


# In[21]:


df2.shape


# In[22]:


#removing USA from event name


# In[23]:


df2['Event name'].str.split('(').str.get(0)


# In[24]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[25]:


df2.head()


# In[26]:


#to clean up athelete age


# In[27]:


df2['athelete_age'] = 2020 - df2['Athlete year of birth']


# In[28]:


#remove h from athelete performance


# In[29]:


df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[30]:


df2.head(5)


# In[31]:


#drop columns: Athelete club, athelete country, athelete year of birth, athelete age category


# In[34]:


df2 = df2.drop(['Athlete club','Athlete country','Athlete year of birth','Athlete age category'], axis = 1)


# In[35]:


df2.head()


# In[36]:


#clean up null values


# In[37]:


df2.isna().sum()


# In[38]:


df2[df2['athelete_age'].isna() == 1]


# In[39]:


df2 = df2.dropna()


# In[40]:


df2.shape


# In[41]:


#checking for dupes


# In[42]:


df2[df2.duplicated() == True]


# In[43]:


#reset index


# In[44]:


df2.reset_index(drop = True)


# In[45]:


#fix types


# In[46]:


df2.dtypes


# In[47]:


df2['athelete_age'] = df2['athelete_age'].astype(int)


# In[48]:


df2.shape


# In[50]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[51]:


df2.dtypes


# In[52]:


df2.head()


# In[53]:


#rename columns


# In[54]:


#Year of event                  int64
#Event dates                   object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed        float64
#Athlete ID                     int64
#athelete_age                   int32


# In[55]:


df2 = df2.rename(columns = 
                 {'Year of event': 'Year', 'Event dates':'race_day', 'Event name':'race_name', 
                  'Event distance/length': 'race_length', 'Event number of finishers': 'race_number_of_finishers',
                  'Athlete performance':'Athlete_performance','Athlete gender':'Athlete_gender', 
                  'Athlete average speed':'Athlete_average_speed','Athlete ID':'Athlete_ID','athelete_age':'Athelete_age'
  
})


# In[56]:


df2.head()


# In[57]:


#reorder columns


# In[58]:


df2.dtypes


# In[59]:


df3 = df2[['race_day','race_name','race_length','race_number_of_finishers','Athlete_ID','Athlete_gender','Athelete_age',
          'Athlete_performance','Athlete_average_speed']]


# In[60]:


df3.head()


# In[61]:


# find 2 race that an athlete ran in 2020 - Sarasota | Everglades


# In[63]:


df3[df3['race_name'] == 'Everglades 50 Mile Ultra Run ']


# In[64]:


#222509


# In[65]:


df3[df3['Athlete_ID'] == 222509]


# In[66]:


#charts and graphs


# In[72]:


sns.histplot(df3, x = 'race_length')


# In[69]:


sns.histplot(df3, x = 'race_length', hue = 'Athlete_gender')


# In[70]:


sns.displot(df3[df3['race_length'] == '50mi']['Athlete_average_speed'])


# In[77]:


sns.violinplot(data=df3, x='race_length', y='Athlete_average_speed', hue='Athlete_gender', split=True, inner='quart', linewidth=1)


# In[82]:


sns.lmplot(data = df3, x = 'Athelete_age', y='Athlete_average_speed', hue = 'Athlete_gender')


# In[83]:


# Things which we can find out from the data


# In[ ]:


#race_day                     
#race_name                    
#race_length                  
#race_number_of_finishers     
#Athlete_performance          
#Athlete_gender               
#Athlete_average_speed       
#Athlete_ID                  
#Athelete_age    


# In[84]:


#Difference in speed for the 50k,50mi male to female


# In[85]:


df3.groupby(['race_length', 'Athlete_gender'])['Athlete_average_speed'].mean()


# In[ ]:


#what age groups are the best in the 50m race (20 + races min) (show 15)


# In[87]:


df3.query('race_length == "50mi"').groupby('Athelete_age')['Athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending = True).query('count>19')


# In[ ]:


#what age groups are the best in the 50m race (10 + races min) (show 20)


# In[88]:


df3.query('race_length == "50mi"').groupby('Athelete_age')['Athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending = True).query('count>9')


# In[90]:


# Seasons for the data -> Slower in, summer than winter?

#spring 3-5
#Summer 6-8
#fall 9-11
#winter 12-2

#split between two decimals


# 

# In[91]:


df3['race_month'] = df3['race_day'].str.split('.').str.get(1).astype(int)


# In[93]:


df3['race_season'] = df3['race_month'].apply(lambda x: 'Winter' if x > 11 else 'Fall' if x > 8 else 'Summer' if x > 5 else 'Spring' if x > 2 else 'Winter')


# In[94]:


df3.head(25)


# In[96]:


df3.groupby('race_season')['Athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending = False)


# In[97]:


#50 miler only


# In[99]:


df3.query('race_length == "50mi"').groupby('race_season')['Athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending = False)


# In[ ]:




