import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('out/grid')

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1)

yvals = np.unique(data[:,0])

for i, y in enumerate(yvals):
	if y > 7.9999 and y<8.001:
		print('y=',y)
		ind = data[:,0] == y
		F = data[ind, 2]
		T = data[ind, 1]
		plt.plot(10**F, 10.0**T)

#P = Prad
#y = np.arange(101)*0.01 * 15.0 + -3.0
#y = 10.0**y
y = 1e8
Trad = (3.0 * 2.45e14 * y / 7.5657e-15 ) ** 0.25
print('Trad=',Trad)
plt.plot((1e20,1e27),(Trad,Trad),"k:",lw=2)
#plt.plot(y, Trad, 'k--', lw=2, label=r'$P=aT^4/3$')

#plt.xlim((4e25,9e25))
#plt.ylim((1.1e9,1.6e9))
plt.ylabel(r'$T\ (\mathrm{K})$', fontsize=12)
plt.xlabel(r'$\mathrm{Flux}\ (\mathrm{erg\ cm^{-2}\ s^{-1}})$', fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.set_yscale('log')
ax.set_xscale('log')
#plt.legend()
plt.tight_layout()

#plt.show()
plt.savefig('TF.pdf',bbox_inches='tight')
