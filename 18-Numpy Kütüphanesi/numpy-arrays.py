import numpy as np

# result = np.array([1,3,5,7,9])

# result = np.arange(1,10)

# result = np.arange(10,100,3) #üçer üçer artış

# result = np.zeros(10)

# result = np.ones(10)

# result = np.linspace(0,100,5) #başlangıç bitiş aralarını eşit 5 parçaya böler

# result = np.linspace(0,5,5)

# result = np.random.randint(0,10)

# result = np.random.randint(20)

# result = np.random.randint(1,10,3)

# result = np.random.rand(5) #5 rastgele sayı 0 ve 1 arasında

# result = np.random.randn(5) #eksilerde dahil  5 rastgele sayı 0 ve 1 arasında

# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10) # 5 e 10 luk matris oluştur

# print(np_multi.sum(axis=1)) #satırlar toplamı

# print(np_multi.sum(axis=0)) #sütunlar toplamı

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)

# result = rnd_numbers.max()
# result = rnd_numbers.min()
# result = rnd_numbers.mean() #oluşan sayıların ortalaması
# result = rnd_numbers.argmax() #üretilen en büyük sayının index numarası
result = rnd_numbers.argmin() #üretilen en küçük sayının index numarası


print(result)