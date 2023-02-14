import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from math import comb

n = 2
p1 = 1/3
p2 = 1/6
q1 = 1-p1
q2 = 1-p2
k = np.arange(0, n+1)
#Practical
binom_1 = binom.pmf(k,n,p1)
binom_2 = binom.pmf(k,n,p2)

print(binom_1)
print(binom_2)

#Theoritical
b1 = []
b2 = []
for i in k:
    C = comb(n,i)
    b1.append(C*(p1**i)*(q1**(n-i)))
    b2.append(C*(p2**i)*(q2**(n-i)))
print(b1)
print(b2)

plt.stem(k,binom_1,'b',markerfmt='bo',use_line_collection=True)
plt.stem(k,b1,'--y',markerfmt='yo',use_line_collection=True)
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.legend(['Practical','Theoritical'])
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig1.pdf')
plt.show()
plt.close()

plt.stem(k,binom_2,'b',markerfmt='bo',use_line_collection=True)
plt.stem(k,b2,'--y',markerfmt='yo',use_line_collection=True)
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.legend(['Practical','Theoritical'])
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig2.pdf')
plt.show()
