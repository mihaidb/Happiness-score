import matplotlib
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
data2015 = pd.read_csv('2015.csv')
data2015.rename(columns ={'Happiness Score':'Happiness_Score', 'Economy (GDP per Capita)': 'Economy' , 'Health (Life Expectancy)':'Health', 'Happiness Rank':'Happiness_Rank' ,\
                          'Trust (Government Corruption)':'Trust', 'Dystopia Residual':'Dystopia' },inplace=True)
data2015.info() #shows us what is every column about and their data type
corr_df=data2015.corr() # creating the correlation map
f,ax = plt.subplots(figsize=(15,15))
sns.heatmap(corr_df,annot=True, linewidths=.5, fmt='.1f' , ax=ax)
plt.show() #correlation map

data2015.Economy.plot(kind='hist',bins=40,figsize=(10,10))   #a hysterezis for economy values
plt.title("Economy hysterezis")
plt.show()

newdata=data2015.head(10)
fig=plt.figure(figsize=(20,10))
plt.title('Top 10  happiest countries')
plt.plot(newdata['Country'],newdata['Happiness_Score'])
plt.show()

#Now we compare economy factor with the happiness score
data2015.Economy.plot(kind = 'line', color = 'blue',label = 'Economy',linewidth=1,alpha = 0.9,grid = True,linestyle = ':')
data2015.Happiness_Score.plot(color = 'red',label = 'Happiness_Score',linewidth=1, alpha = 0.9,grid = True,linestyle = '-.')
plt.legend(loc='upper right')
plt.xlabel('Economy')
plt.ylabel('Happiness')
plt.title('Relation between economy and Happiness score')
#Here we can see the relation between economy and happiness score. Countries with good economy are also happier.
plt.show() #relation between economy and happiness score.

#Now we define another column sum_of_factors which is the sum of all factors contributing to happiness and
#it is aproximately equal to happiness_score as shown
data2015['Sum_of_factors']=data2015['Economy']+data2015['Family']+data2015['Health']+data2015['Freedom']+ \
data2015['Trust']+ data2015['Dystopia']+data2015['Generosity']
data=data2015[['Country', 'Happiness_Score','Sum_of_factors']]
print(data.head(15))
