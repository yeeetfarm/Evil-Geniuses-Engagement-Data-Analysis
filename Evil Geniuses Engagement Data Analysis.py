#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[47]:


#Read in .csv file from social_data.xlsx
social_data=pd.read_csv('C:/Users/jakey/OneDrive/Documents/personal projects/evil geniuses/social_data.xlsx - Data.csv',parse_dates=['Published Date'],index_col=['Published Date'])
#Sort dataset by chronological date
social_data=social_data.sort_index()
social_data


# In[48]:


#Question 1
#Typical engagment rate=total engagements/total impressions
np.mean(social_data['Total Engagements']/social_data['Total Impressions'])


# Commentary:  
# I calculate the typical engagement rate by dividing the "Total Engagements" column by the "Total Impressions" column. This gives me 3479 rows of information, one row per "Published Date" provided. In order to get the typical engagement rate expected, I take the mean of the column of quotients which gives me about a 40% typical engagement rate expected from the 3 months of data provided.

# In[49]:


social_data['Engagement Rate']=social_data['Total Engagements']/social_data['Total Impressions']
social_data['Engagement Rate']=social_data['Engagement Rate'].fillna(0)
rows_greater_than_or_equal_15=len(social_data[social_data['Engagement Rate']>=.15])
rows_greater_than_or_equal_15/len(social_data)


# Commentary:  
# To calculate the likelihood that we can achieve a 15% engagement rate, I create a new column in the "social_data" dataframe called "Engagement Rate" which is the quotient of "Total Engagements" divided by "Total Impressions," or the engagement rate for each row. I create a subset of the social_data dataframe where the "Engagement Rate" is greater than or equal to .15 and call the length of this subset "rows_greater_than_or_equal_15". I find the length of it to be 226. This means there are 226 days where the engagement rate was greater than or equal to 15%. I divide 226 by the length of the "social_data" dataframe, which is 3479, to get the likelihood of an engagement rate of 15% or higher. This likelihood value is about 6.5%.

# In[50]:


#Question 2
social_data['Day of the Week']=social_data.index.day_name()
social_data['Time']=social_data.index.time
social_data


# In[51]:


#Day of the week vs engagement rates
social_data.groupby('Day of the Week')['Engagement Rate'].sum().plot(kind='bar',xlabel='Day of the Week',ylabel='Engagement Rate Sum',title='Day of the Week vs Engagement Rate')


# In[52]:


social_data.groupby('Day of the Week')['Engagement Rate'].sum()


# Commentary:  
# The histogram above shows that day of the week does affect engagement rates because Friday's engagement rate is drastically higher than the other days of the week. This means Evil Geniuses should try to post on their social accounts on Friday to get the most engagement rate.

# In[58]:


social_data['Hour']=social_data.index.hour
social_data.groupby('Hour')['Engagement Rate'].sum()


# In[59]:


social_data.groupby('Hour')['Engagement Rate'].sum().plot(kind='bar',xlabel='Hour',ylabel='Engagement Rate',title='Hour of the Day vs Engagement Rate')


# Commentary:  
# The above histogram shows time does affect engagement rates as well. The 12 o'clock hour has a significantly higher engagement rate than all the other hours of the day. With this data in mind, the best time to post social media activity would be Friday around 12 pm.

# In[60]:


#Question 3
#Game titles
#Use .value_counts() to see the different game titles first
social_data['Account'].value_counts()


# Commentary:  
# I notice there are repeating "General" Account categories with 2 separate counts. After analyzing, I realize there are different inputs for the "General" account which are "General" and "General " with a space at the end. The function counts these separately so I will account for this.

# In[61]:


social_data['Account']=social_data['Account'].replace('General ','General')
social_data.groupby('Account')['Engagement Rate'].sum()


# In[64]:


social_data.groupby('Account')['Engagement Rate'].sum().plot(kind='bar',xlabel='Account',ylabel='Engagement Rate',title='Account vs Engagement Rate')


# Commentary:  
# The "General" game title is doing the best in terms of social performance. If Evil Geniuses is solely focused on profits in the short term, they should prioritize posts related to the "General" category. However, if Evil Geniuses wants to grow as an organization in the long term, they should seek to grow engagement in the other accounts like DOTA2, CSGO, Valorant, and Content Creators to diversify engagement and profit. For example, Evil Geniuses could host a giveaway in Valorant and have Evil Geniuses' pro players promote it will which bring more attention to Evil Geniuses' Valorant account and perhaps viewers will stay if the giveaways are consistent or they come to like something about the players or team.

# In[17]:


#Question 4
#Media
social_data['Media Type'].value_counts()


# In[65]:


social_data.groupby('Media Type')['Engagement Rate'].sum()


# In[66]:


social_data.groupby('Media Type')['Engagement Rate'].sum().plot(kind='bar',xlabel='Media Type',ylabel='Engagement Rate',title='Media Type vs Engagement Rate')


# Commentary:  
# The "Photo" media type performs the best.

# In[26]:


#Question 5
#Campaign
social_data['Campaign Name'].value_counts()


# In[67]:


social_data.groupby('Campaign Name')['Engagement Rate'].sum()


# In[68]:


social_data.groupby('Campaign Name')['Engagement Rate'].sum().plot(kind='bar',xlabel='Campaign Type',ylabel='Engagement Rate',title='Campaign Type vs Engagement Rate')


# Commentary:  
# The 'N/A' campaign type is the best performing campaign.

# In[36]:


#Question 6
#Account
social_data['Account Type'].value_counts()


# In[69]:


social_data.groupby('Account Type')['Engagement Rate'].sum()


# In[70]:


social_data.groupby('Account Type')['Engagement Rate'].sum().plot(kind='bar',xlabel='Account Type',ylabel='Engagement Rate',title='Account Type vs Engagement Rate')


# Commentary:  
# The Facebook page account type has the highest engagement rate.

# Commentary:  
# Based on my discoveries, I would advise the following posting strategy: weigh the more popular variable types more but don't neglect the unpopular variable types.  
# Continue to be consistent with the most highly engaged variables to maximize profit and keep them at high engagement rates. Specifically, continue to post photos of the "General" game type under the "N/A" campaign on Facebook on Fridays at 12 pm.
# At the same time, if Evil Geniuses wants to grow its organization name as a whole, it needs to diversify its social media channels' discoveries. So while the most highly engaged variables should be utilized more often to maximize funds, the other social channels, games, and campaigns also need to have activity to try to grow. This is not only for Evil Geniuses to grow in all aspects but what if something bad suddenly happens to Facebook or the "General" game category? Then Evil Geniuses won't have other sources of popularity or funds to rely on. By maintaining and seeking to grow the less popular categories, Evil Geniuses can hedge against this possible risk.

# Question 7  
# Commentary:  
# As we see from the data, solely posting won't grow the other variables because they are not getting much engagement to begin with. Thus the social media team needs to have activity outside just posting to bring engagment to the other accounts. For example, host a Valorant giveaway on Instagram or Twitter because these are all less popular variables. Just by word of mouth and reposting, more and more people will see and become engaged with these accounts. In addition, because the "General" game is doing so well but social media accounts, besides Facebook, are not, perhaps the social media team could post about the "General" game category to these other social accounts to attract users who may not use Facebook but use other social media. 
