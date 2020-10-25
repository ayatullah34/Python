import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1] #soldan başlıyor
result = numbers[0:3]
result = numbers[3:] 
result = numbers[::] #tüm liste
result = numbers[::-1] #tersten liste yazma

numbers2 = np.array([ [0,5,10],[15,20,25],[50,75,85] ])
# print(numbers2)

result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2] #1.satırın 2.indexindeki eleman
result = numbers2[2,1]
result = numbers2[:,2] #tüm satırlardaki 2.elemanlar
result = numbers2[:,0]
result = numbers2[:,0:2] # tüm satırlar seçilip o satırlardi 0 ile 2. index arasındaki elemanlar gelir
result = numbers2[-1,:] #son satırdaki tüm elemanlar
result = numbers2[:2,:2] 

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 #referans
arr2 = arr1.copy() # referans olmaz

print(arr1)
print(arr2)

arr2[0] = 20

print(arr1)
print(arr2)

