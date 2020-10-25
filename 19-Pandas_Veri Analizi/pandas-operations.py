import pandas as pd
import numpy as numpy

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x*x

result = df
result = df['Column2'].unique() #tekrarlayan elemanları bir kez yazar
result = df['Column2'].nunique() #tekrarları bir kez sayarak eleman sayısını verir.
result = df['Column2'].value_counts() #hangi elemanın kaç kez tekrarlandığın verir
result = df['Column1'] * 2
result = df['Column1'].apply(kareal)#apply ile fonkisyon verilir
result = df['Column1'].apply(kareal2)
result = df['Column1'].apply(lambda x: x*x)
result = df['Column3'].apply(len)
df['Column4'] = df['Column3'].apply(len)

# print(df)

result = len(df.columns)
result = len(df.index)

result = df.sort_values('Column2')

result = df.sort_values('Column2',ascending = False)

# print(result)


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index='Ay',columns = 'Kategori',values='Gelir')

print(df)
