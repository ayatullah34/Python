import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , orange = s2)
# df = pd.DataFrame(data)

# print(df)

data = [['ahmet',50],['ali',60],['veli',30],['çınar',66]]
dict = {'Name': ['ahmet','ali','veli','çınar'] , 'Grade': [50,60,30,66]}
dict_list = [
                 {'Name': 'ahmet', 'Grade': 50 },
                 {'Name': 'ali' , 'Grade': 30},
                 {'Name': 'veli' , 'Grade': 20},
                 {'Name': 'ayşe' , 'Grade': 70}
            ]

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
df = pd.DataFrame(data,columns=['name','grade'],index = [1,2,3,4],dtype=float)

df = pd.DataFrame(dict)
df = pd.DataFrame(dict, index = ['212','232','246','255'])
df = pd.DataFrame(dict_list)

print(df)
