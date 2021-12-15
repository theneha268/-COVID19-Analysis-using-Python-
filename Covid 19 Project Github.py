#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[ ]:


# Reading the COVID dataset 

covid_df=pd.read_csv("C:\Users\Dell\Downloads\Project.csv")


# In[ ]:


covid_df.head()


# In[ ]:


#Removing ambiguous date

covid_df=covid_df[covid_df['Date']!='01-01-1970']


# In[ ]:


covid_df.head()


# In[ ]:


#To get data Overview 

covid_df.describe()


# In[ ]:


#Filtering data 

covid_df=covid_df[covid_df['Region']!='World']


# In[ ]:


#Dropping unwanted column 

covid_df.drop(["S. No."],axis=1,inplace=True)


# In[ ]:


#Renaming columns 

covid_df.rename(columns={'Cured/Discharged':'Cured'},inplace=True)


# In[ ]:


covid_df.rename(columns={'Confirmed Cases':'Confirmed'},inplace=True)


# In[ ]:


#To make index continuous 

covid_df.reset_index()


# In[ ]:


#To convert date to date time values from string entries 

covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%d-%m-%Y')


# In[ ]:


covid_df.head()


# In[ ]:


#To create new column from existing columns 

covid_df['Active_Cases']=covid_df['Confirmed']-covid_df['Cured']-covid_df['Death']


# In[ ]:


#To get bottom values  

covid_df.tail()


# In[ ]:


# Creating pivot table

statewise=pd.pivot_table(covid_df,values=["Confirmed","Death","Cured"],index="Region",aggfunc=max)


# In[ ]:


#Adding a new column based on existing ones 

statewise["Recovery Rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[ ]:


statewise["Mortality Rate"]=statewise["Death"]*100/statewise["Confirmed"]


# In[ ]:


#Sorting values based on a column 

statewise=statewise.sort_values(by="Confirmed",ascending=False)


# In[ ]:


#To assign colour gradient to the result for better understanding  
statewise.style.background_gradient(axis=0)


# In[ ]:


#Top 10 Active Cases States

top_10_active_cases=covid_df.groupby(by= 'Region').max()[["Active_Cases","Date"]].sort_values(by=["Active_Cases"],ascending=False).reset_index()


# In[ ]:


#Plotting Bar Plot for Top 10 States

top_10_active_cases=covid_df.groupby(by= 'Region').max()[["Active_Cases","Date"]].sort_values(by=["Active_Cases"],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 States with most Active Cases in India",size=14)
ax=sns.barplot(data=top_10_active_cases[top_10_active_cases["Region"]!="India"].iloc[:10],y="Active_Cases",x="Region",linewidth=2,edgecolor="Red")
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[ ]:


#Top 10 States with Highest Deaths

top_deaths=covid_df.groupby(by= 'Region').max()[["Death","Date"]].sort_values(by=["Death"],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 States with most Deaths in India",size=20)
ax1=sns.barplot(data=top_deaths[top_deaths["Region"]!="India"].iloc[:12],y="Death",x="Region",linewidth=3,edgecolor="Blue")
plt.xlabel("States")
plt.ylabel("Total Deaths")
plt.show()


# In[ ]:


# Watching Growth Trend

fig=plt.figure(figsize=(12,6))

ax=sns.lineplot(data=covid_df[covid_df['Region'].isin(['Maharashtra','Kerala','Karnataka','Tamil Nadu','Uttar Pradesh'])],x='Date',y='Active_Cases',hue='Region')

ax.set_title("Top 5 Affected States in India",size=16)


# # Vaccine Data Statewise

# In[ ]:


vaccine_df=pd.read_csv("C:\Users\Dell\Downloads\covid_vaccine_statewise(1).csv")


# In[ ]:


vaccine_df.head()


# In[ ]:


vaccine_df.info()


# In[ ]:


vaccine_df.rename(columns={"Updated On" : 'Vaccine_Date'},inplace=True)


# In[ ]:


#Calculating Nulls in our Data

vaccine_df.isnull().sum()


# In[ ]:


vaccination = vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis=1)


# In[ ]:


vaccination.head()


# In[ ]:


# Male vs Female Vaccination (Making Pie Chart)

male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=['Male','Female'],values=[male,female],title="Male and Female Vaccination")


# In[ ]:


# Remove rows where Region is India

vaccine=vaccine_df[vaccine_df.State!='India']


# In[ ]:


vaccine.head()


# In[ ]:


#Rename Columns

vaccine.rename(columns={"Total Individuals Vaccinated":"Total"},inplace=True)
vaccine.head()


# In[ ]:


#Most Vaccinated States

max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values("Total",ascending=False)[:5]
max_vac


# In[ ]:


#Top 5 Vaccinated States in India

fig=plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India",size=20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index,linewidth=2,edgecolor="Red")
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




