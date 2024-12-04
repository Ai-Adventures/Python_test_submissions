#!/usr/bin/env python
# coding: utf-8

# In[286]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[287]:


df=pd.read_csv(r'E:\MY C DATA\Documents\MASTERS\SUNY BUFFALO\STUDY MATERIAL\INTRO TO ML ASIF IMRAN\adult.data.csv')


# In[288]:


df


# In[289]:


indx=["age","job_type","fnlwgt","edu_level","education_num","marital_status","job_title","relationship","race","sex",
      "capital-gain","capital-loss","hours-per-week","continent","income"]


# In[290]:


len(indx)


# In[291]:


df.columns=indx 


# In[292]:


df


# # DATA CLEANING
# 

# In[293]:


df.drop(["relationship"],axis=1,inplace=True)


# In[294]:


df


# ## Dropping Duplicates

# In[295]:


df.duplicated().sum()


# In[296]:


df.drop_duplicates(inplace=True)


# ## Job_type column

# In[297]:


df.dtypes


# In[298]:


df['job_type'].value_counts()


# In[299]:


df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# In[300]:


df['job_type'].replace(['?','Without-pay','Never-worked'], np.nan, inplace=True)
replace_dict_job_type={"Local-gov":"government","State-gov":"government",'Federal-gov':"government",'Self-emp-not-inc':"selfemployed","Self-emp-inc":"selfemployed"}
df['job_type']=df['job_type'].replace(replace_dict_job_type)
df['job_type'].value_counts()


# In[301]:


df


# ## Fnlwgt column

# In[302]:


df['fnlwgt'].dtypes
df['fnlwgt'].value_counts()


# ## Edu_level column

# In[303]:


df['edu_level'].value_counts()


# In[304]:


replace_dict={"11th":"school","10th":"school","1st-4th":"school","5th-6th":"school","12th":"school","7th-8th":"school","9th":"school",'Preschool':"school",'Prof-school':'postgraduate','Doctorate':'postgraduate','Bachelors':'undergraduate','HS-grad':'undergraduate','Assoc-voc':'undergraduate','Assoc-acdm':'undergraduate','Some-college':'undergraduate'}
df['edu_level']=df['edu_level'].replace(replace_dict)
df['edu_level'].value_counts()


# ## Education_num
# 

# In[305]:


df['education_num'].value_counts()


# In[306]:


df['education_num'].dtypes


# ## Marital_status column

# In[307]:



replace_dict_job_type={"Married-civ-spouse":"married","Married-spouse-absent":"married",'Married-AF-spouse':'married','Never-married':'single','Divorced':'previously married','Separated':'previously married','Widowed':'previously married'}
df['marital_status']=df['marital_status'].replace(replace_dict_job_type)
df['marital_status'].value_counts()


# ## Job_title column

# In[308]:


df['job_title'].value_counts()
occupation_grouping = {
    'Prof-specialty': 'Professional',
    'Exec-managerial': 'Management',
    'Tech-support': 'Technical',
    'Craft-repair': 'Craft/Repair',
    'Machine-op-inspct': 'Machine Operations',
    'Adm-clerical': 'Clerical',
    'Sales': 'Sales',
    'Other-service': 'Service',
    'Priv-house-serv': 'Household Services',
    'Protective-serv': 'Protective Services',
    'Handlers-cleaners': 'Manual Labor',
    'Transport-moving': 'Manual Labor',
    'Farming-fishing': 'Agriculture',
    'Armed-Forces': 'Military'}
df['job_title']=df['job_title'].replace(occupation_grouping)
df['job_title'].value_counts()


# ## Race column

# In[309]:


df['race'].value_counts()


# ## Sex column

# In[310]:


df['sex'].value_counts()


# ## Capital-gain column

# In[311]:


df['capital-gain'].dtypes


# In[312]:


df['capital-gain'].unique()


# ## Capital-loss column

# In[313]:


df['capital-loss'].dtypes


# In[314]:


df['capital-loss'].unique()


# ## Hours-per-week

# In[315]:


df['hours-per-week'].dtypes


# In[316]:


df['hours-per-week'].unique()


# In[ ]:





# ## Continent column

# In[317]:



df['continent'].value_counts()


# In[318]:


df['continent'].replace(['?'], np.nan, inplace=True)
continent_grouping = {
    'United-States': 'North America',
    'Canada': 'North America',
    'Mexico': 'North America',
    'Puerto-Rico': 'North America',
    'Outlying-US(Guam-USVI-etc)': 'North America',
    
    'Cuba': 'Central/South America & Caribbean',
    'El-Salvador': 'Central/South America & Caribbean',
    'Jamaica': 'Central/South America & Caribbean',
    'Dominican-Republic': 'Central/South America & Caribbean',
    'Columbia': 'Central/South America & Caribbean',
    'Guatemala': 'Central/South America & Caribbean',
    'Haiti': 'Central/South America & Caribbean',
    'Nicaragua': 'Central/South America & Caribbean',
    'Trinadad&Tobago': 'Central/South America & Caribbean',
    'Honduras': 'Central/South America & Caribbean',
    'Ecuador': 'Central/South America & Caribbean',
    'Peru': 'Central/South America & Caribbean',
    
    'Germany': 'Europe',
    'England': 'Europe',
    'Italy': 'Europe',
    'Poland': 'Europe',
    'France': 'Europe',
    'Greece': 'Europe',
    'Ireland': 'Europe',
    'Scotland': 'Europe',
    'Hungary': 'Europe',
    'Portugal': 'Europe',
    'Yugoslavia': 'Europe',
    'Holand-Netherlands': 'Europe',
    
    'Philippines': 'Asia',
    'India': 'Asia',
    'China': 'Asia',
    'Vietnam': 'Asia',
    'Japan': 'Asia',
    'Taiwan': 'Asia',
    'Cambodia': 'Asia',
    'Laos': 'Asia',
    'Thailand': 'Asia',
    'Iran': 'Asia',
    'Hong': 'Asia'}

df['continent']=df['continent'].replace(continent_grouping)   
df['continent'].value_counts()


# In[319]:


df.isnull().sum()


# In[320]:


df.dropna(inplace=True)


# In[321]:


df.isnull().sum()


# In[322]:


df["age"].unique()


# In[323]:


len(list(df["age"].unique()))


# In[324]:


df["job_type"].unique()


# In[325]:


df["edu_level"].unique()


# In[326]:


df["marital_status"].unique()


# In[327]:


df["job_title"].unique()


# In[328]:


df["race"].unique()


# In[329]:


df["sex"].unique()


# In[330]:


df["continent"].unique()


# In[331]:


df["income"].unique()
df['income'] = df['income'].replace({'<=50K': 0, '>50K': 1})


# In[332]:


df


# # DATA VISUALIZATION

# ## Distribution of the people and income

# In[333]:


income_count=df[['income']]
income_count.value_counts()


# In[334]:


income_count=income_count.groupby(['income']).size().reset_index(name='number_of_people')


# In[335]:


plt.figure(figsize=(10, 6))
sns.barplot(data=income_count, x='income', y='number_of_people', hue='number_of_people', palette='viridis')


# ## Distribution of the population in the dataset by age

# In[336]:


df1=df[['age']]


# In[337]:


df1


# In[338]:


df1=df1.groupby(['age']).size().reset_index(name='Population')


# In[339]:


df1


# In[340]:


df2=df1.nlargest(10,'Population').sort_values(by='Population',ascending=False)


# In[341]:


plt.figure(figsize=(20, 10))
sns.barplot(data=df2, x='age', y='Population', palette='viridis')


# ## Distribution of income by gender

# In[342]:


df3=df[['sex',"income"]]


# In[343]:


df3


# In[344]:


df['Income_Above_50K'] = df['income'].map({1: True, 0: False})
df['Income_Above_50K']


# In[345]:


grouped_count = df.groupby(['sex', 'Income_Above_50K']).size().reset_index(name='Count')


# In[346]:


grouped_count


# In[347]:


plt.figure(figsize=(12, 6))
sns.barplot(data=grouped_count, x='sex', y='Count', hue='Income_Above_50K', palette='magma')


# In[348]:


df


# In[349]:


df.drop(['Income_Above_50K'],axis=1,inplace=True)


# In[ ]:





# # ENCODING AND APPLYING LOGISTIC REGRESSION

# In[350]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])


# In[351]:


from sklearn.model_selection import train_test_split
X = df.drop('income', axis=1)  
y = df['income']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.001, random_state=42)


# In[352]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10, 100],'penalty': ['l1', 'l2'],'solver': ['liblinear']  }
log_reg = LogisticRegression(max_iter=1000)
grid_search = GridSearchCV(log_reg, param_grid, cv=2, scoring='accuracy')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_accuracy = grid_search.best_score_
print(f"Best Hyperparameters: {best_params}")
print(f"Best Cross-Validation Accuracy: {best_accuracy * 100:.2f}%")


# In[353]:


from sklearn.metrics import accuracy_score
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Set Accuracy: {accuracy * 100:.2f}%")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




