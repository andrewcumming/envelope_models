import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('out/grid')

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1)

Fvals = np.unique(data[:,2])

for i, F in enumerate(Fvals):
	if i % 20 == 0:
		print('F=',F)
		ind = data[:,2] == F
		y = data[ind, 0]
		T = data[ind, 1]
		plt.plot(10**y, 10.0**T)

# P = Prad
y = np.arange(101)*0.01 * 15.0 + -3.0
y = 10.0**y
Trad = (3.0 * 2.45e14 * y / 7.5657e-15 ) ** 0.25
plt.plot(y, Trad, 'k--', lw=2, label=r'$P=aT^4/3$')

#plt.xlim((1e3,3e5))
#plt.ylim((1e8,2e9))
plt.ylabel(r'$T\ (\mathrm{K})$', fontsize=12)
plt.xlabel(r'$\mathrm{Column\ depth}\ (\mathrm{g\ cm^{-2}})$', fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
ax.set_yscale('log')
ax.set_xscale('log')
plt.legend()
plt.tight_layout()

#plt.show()
plt.savefig('prof.pdf',bbox_inches='tight')
