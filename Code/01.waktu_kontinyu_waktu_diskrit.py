import numpy as np
import matplotlib.pyplot as plt

# waktu kontinyu

A = 1
omega_1 = 2
omega_2 = 3
omega_3 = omega_1 + 2*np.pi

t = np.arange(0,10,0.01)
x1 = A*np.cos(omega_1*t)
x2 = A*np.cos(omega_2*t)
x3 = A*np.cos(omega_3*t)

plt.plot(x1)
plt.plot(x2)
plt.plot(x3)
plt.legend(['x1','x2','x3'])
plt.show()

# waktu diskrit

n = np.arange(0,20)
y1 = A*np.cos(omega_1*n)
y2 = A*np.cos(omega_2*n)
y3 = A*np.cos(omega_3*n)

plt.stem(y1)
plt.show()
plt.stem(y2)
plt.show()
plt.stem(y3)
plt.show()

# kompleks

C = 1
alpha1 = 1.5
alpha2 = 0.5
alpha3 = -0.5
alpha4 = -1.5
n = np.arange(1,20)
x1 = C*alpha1**n
x2 = C*alpha2**n
x3 = C*alpha3**n
x4 = C*alpha4**n