import numpy as np 

numbers1 = np.random.randint(10,100,6)

numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result =  numbers1 - 10
result = numbers1 * numbers2
result = numbers1 * 10
result = numbers1 / numbers2
result = numbers1 / 10

result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

multinumbers1 = numbers1.reshape(2,3)
multinumbers2 = numbers2.reshape(2,3)

print(multinumbers1)
print(multinumbers2)

result = np.vstack((multinumbers1,multinumbers2)) #iki matrisi dikey olarak birleştirir üst üste görünürler
result = np.hstack((multinumbers1,multinumbers2))#iki matrisi yatay olarak birleştirir yan yana görünürler

result = numbers1 >= 5 #bütün elemanların 5 den büyük olup olmadığına bakar
result = numbers1 % 2 == 0 

print(numbers1[result])

print(result)