import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data , index = ['a','c','e','f','h'] , columns = ['column1','column2','column3'])

df = df.reindex( ['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4'] = newColumn

result = df
result = df.drop(['column1','column2'],axis = 1)
result = df.drop(['a','b','h'],axis = 0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df['column1'].isnull().sum()
result = df
result = df[df['column1'].isnull()]
result = df[df['column1'].isnull()]['column1']
result = df[df['column1'].notnull()]['column1']

result = df.dropna() # axis = 0 => satıra göre (içinde null olanları siler) 
result = df.dropna(axis=1) # axis = 1 => sütuna göre
result = df.dropna(how = "any") # herhangibir kolonda null varsa siler
result = df.dropna(how = "all") # bütün kolonlarda null varsa siler
result = df.dropna(subset= ['column1','column2'] , how = 'all' ) # bir ve ikide null olmaz sonuç basıldığında
result = df.dropna(subset= ['column1','column2'] , how = 'any' )
result = df.dropna(thresh = 2) # 2 tane normal veri varsa silmez
result = df.dropna(thresh = 4)

result = df.fillna(value = 'no input') #olmayan değerler yerine 'not input yazılır' 
result = df.fillna(value = 1)

result = df.sum() #her kolondaki toplam sayı
result = df.sum().sum()
result = df.size
result = df.isnull().sum() 
result = df.isnull().sum().sum()

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value = ortalama(df))

print(result)