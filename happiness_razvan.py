import csv
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
words = {}
words_list = []

with open("2015.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]


for line in data_read : 
   k = 0 
   for cell in line :
      if len(words) < 12:
         words[cell] = []
         words_list.append(cell)
      else :
         my_list = words[words_list[k]]
         my_list.append(cell)
         words[cell] = my_list
         k = k + 1
        
df = pd.DataFrame(words,columns=words_list)  

words_list.remove("Happiness Score")  
words_list.remove("Country")
words_list.remove("Region")
words_list.remove("Happiness Rank")

X = df[words_list]
Y = df['Happiness Score']

regression = linear_model.LinearRegression()
regression.fit(X, Y)

#print('Intercept: \n', regression.intercept_)
#print('Coefficients: \n', regression.coef_) 

float_list = regression.coef_

k = 0
for float_number in float_list :
    print("Coefficient of " + words_list[k] + " is " + str(float_number))
    k = k + 1

k = 0
print("\n")
for line in data_read :
   m = 0
   happiness = 0.0
   if k > 0 :
      for cell in line :
          if m > 3 :
             happiness = happiness + float(float_list[m-4])*float(cell)
             #print(happiness) 
          m = m + 1
   print("Coeficientul de fericire actual este : " + str(happiness))        
   k = 1

