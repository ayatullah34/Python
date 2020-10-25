import matplotlib.pyplot as plt 
import numpy as np 

""" x = [1,2,3,4]
y = [1,4,9,16]

# plt.plot(x,y, color ='red' , linewidth = '5' )
# plt.plot(x,y, '--g')
plt.plot(x,y, 'o--r')
plt.axis([0,6,0,20])

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel('y label')
 """

""" 
x = np.linspace(0,2,100)

plt.plot(x , x , label = 'linear')
plt.plot(x , x**2 , label = 'quadratic')
plt.plot(x , x**3 , label = 'cubic')

plt.xlabel("x label")
plt.ylabel("y label")
plt.title('simple plot')

plt.legend()

plt.show()

 """
 
""" 
x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)

axs[0].plot(x,x,color='yellow')
axs[0].set_title("linear")

axs[1].plot(x,x**2,color='red')
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color='black')
axs[2].set_title("cubic")

plt.tight_layout()
plt.show()
 """

x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot(x,x,color='yellow')
axs[0,0].set_title("linear")

axs[0,1].plot(x,x**2,color='red')
axs[0,1].set_title("quadratic")

axs[1,0].plot(x,x**3,color='black')
axs[1,0].set_title("cubic")

axs[1,1].plot(x,x**4,color='blue')
axs[1,1].set_title("rectangle")

plt.tight_layout()
plt.show()