import numpy as np
from matplotlib import pyplot as plt

mass_ratio = np.linspace(1,40,200)
c = 299792458
photon = [1.0, "photon"]
fusion = [0.05, "typ fusion"]
ion = [0.00033, "optimistic HiPEP"] # Isp ~ 10,000 seconds
engines = [photon, fusion, ion]

# non-relativistic
fig, ax = plt.subplots()
for engine in engines:
	Δv = [engine[0]*np.log(mr) for mr in mass_ratio]
	ax.plot(mass_ratio, Δv, label=engine[1]+" (Ve = "+str(engine[0])+")")
ax.set_xlim(1,40)
ax.set_ylim(1e-4,4)
ax.set_yscale("log")
ax.set_title("Classical Rockets")
ax.set_xlabel("Mass Ratio (unitless)")
ax.set_ylabel("Δv (fraction of c)")
ax.legend()
fig.tight_layout()
#plt.savefig("rockets-non-relativistic.png")

# rapidity
fig, bx = plt.subplots()
for engine in engines:
	Δv = [engine[0]*np.log(mr) for mr in mass_ratio]
	bx.plot(mass_ratio, Δv, label=engine[1]+" (Ve = "+str(engine[0])+")")
bx.set_xlim(1,40)
bx.set_ylim(0,4)
bx.set_title("Relativistic Rockets (Rapidity)")
bx.set_xlabel("Mass Ratio (unitless)")
bx.set_ylabel("Rapidity (fraction of c)")
bx.legend()
fig.tight_layout()
#plt.savefig("rockets-rapidity.png")

# relativistic
fig, cx = plt.subplots()
for engine in engines:
	Δv = [np.tanh(engine[0]*np.log(mr)) for mr in mass_ratio]
	cx.plot(mass_ratio, Δv, label=engine[1]+" (Ve = "+str(engine[0])+")")
cx.set_xlim(1,40)
cx.set_ylim(0,1.004)
cx.set_title("Relativistic Rockets (Δv)")
cx.set_xlabel("Mass Ratio (unitless)")
cx.set_ylabel("Δv (fraction of c)")
cx.legend()
fig.tight_layout()
#plt.savefig("rockets-relativistic-lin.png")
fig, dx = plt.subplots()
for engine in engines:
	Δv = [np.tanh(engine[0]*np.log(mr)) for mr in mass_ratio]
	dx.plot(mass_ratio, Δv, label=engine[1]+" (Ve = "+str(engine[0])+")")
dx.set_xlim(1,40)
dx.set_yscale("log")
dx.set_ylim(1e-4,1.04)
dx.set_title("Relativistic Rockets (Δv)")
dx.set_xlabel("Mass Ratio (unitless)")
dx.set_ylabel("Δv (fraction of c)")
dx.legend()
fig.tight_layout()
#plt.savefig("rockets-relativistic.log.png")

# relativistic vs classical
fig, ex = plt.subplots()
for engine in engines:
	Δvr = [np.tanh(engine[0]*np.log(mr)) for mr in mass_ratio]
	Δvc = [engine[0]*np.log(mr) for mr in mass_ratio]
	ex.plot(mass_ratio, Δvr, linestyle='solid', label=engine[1]+" (Ve = "+str(engine[0])+")")
	ex.plot(mass_ratio, Δvc, linestyle='dashed', label=engine[1]+" (Ve = "+str(engine[0])+")")
ex.set_xlim(1,40)
ex.set_yscale("log")
ex.set_ylim(1e-4,10.04)
ex.set_title("Relativistic vs Classical Rockets (Δv)")
ex.set_xlabel("Mass Ratio (unitless)")
ex.set_ylabel("Δv (fraction of c)")
#ex.legend()
fig.tight_layout()
#plt.savefig("rockets-comparison.png")

plt.show()
