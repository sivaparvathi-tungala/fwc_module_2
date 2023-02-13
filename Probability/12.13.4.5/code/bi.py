import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
n = 2
p1 = 0.333
p2 = 0.166
k = np.arange(0, n+1)
binom_1 = binom.pmf(k,n,p1)
binom_2 = binom.pmf(k,n,p2)

print(binom_1)
print(binom_2)
#plt.plot(k,binom_1,color='blue')
#plt.plot(k,binom_2,color='green')
#plt.title("Binomial Distribution")
plt.stem(k,binom_1)

plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig1.pdf')
plt.show()
plt.close()

plt.stem(k,binom_2)
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$p_X(k)$')
plt.savefig('/home/user/Probability/12.13.4.5/code/bfig2.pdf')

plt.show()
