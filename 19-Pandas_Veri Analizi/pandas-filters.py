import pandas as pd
import numpy as np

data= np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data , columns = ["Columns1","Columns2","Columns3","Columns4","Columns5"] )

result = df
result = df.columns
result = df.head() #5 veri
result = df.head(10)
result = df.tail() #son 5 beş kayıt
result = df.tail(10)
result = df['Columns1'].head()
result = df.Columns1.head()
result = df[['Columns1','Columns2']]
result = df[['Columns1','Columns2']].head()
result = df[['Columns1','Columns2']].tail()
result = df[5:15][['Columns1','Columns2']].head()
result = df[5:15][['Columns1','Columns2']].tail()

result = df > 50
result = df[df > 50]
result = df[df % 2 == 0]
result = df['Columns1'] > 50
result = df[df['Columns1'] > 50] [['Columns1','Columns2']]
result = df[ (df['Columns1'] > 50) & (df['Columns2'] > 50) ]
result = df[ (df['Columns1'] > 50) & (df['Columns2'] < 70) ] [['Columns1']]
result = df[ (df['Columns1'] > 50) | (df['Columns2'] < 70) ] [['Columns1' ,'Columns2']]
result = df.query("Columns1 >= 50 & Columns1 % 2 == 0")
result = df.query("Columns1 >= 50 & Columns1 % 2 == 0") [['Columns1']]
result = df.query("Columns1 >= 50 | Columns1 % 2 == 0") [['Columns1']]


print(result)