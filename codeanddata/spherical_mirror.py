'''plotting example spherical telescopes targeting λ/4 and λ/5 at 550 nm'''
import numpy as np
from matplotlib import pyplot as plt


diameters = np.linspace(0,300,1000) # mm
λ = 550e-9 #target wavelength
f4s = [(diameter**4/(0.25*2048e3*λ))**(1/3) for diameter in diameters]
f5s = [(diameter**4/(0.2*2048e3*λ))**(1/3) for diameter in diameters]
fl4s = [(diameter/(0.25*2048e3*λ))**(1/3) for diameter in diameters]
fl5s = [(diameter/(0.2*2058e3*λ))**(1/3) for diameter in diameters]



fig, ax = plt.subplots(2,sharex=True)

ax[0].plot(diameters,f4s,label="λ/4")
ax[0].plot(diameters,f5s,label="λ/5")
ax[1].plot(diameters,fl4s,label="λ/4")
ax[1].plot(diameters,fl5s,label="λ/5")
ax[0].set_xlim(0,max(diameters))
ax[0].set_ylim(0,3500)
ax[1].set_ylim(0,11)

ax[0].set_title("Acceptable Spherical Mirrors")
ax[1].set_xlabel("Diameter (mm)")
ax[0].set_ylabel("Focal Length (mm)")
ax[1].set_ylabel("Focal Ratio")

ax[0].legend(loc=0)
ax[1].legend(loc=0)
fig.set_size_inches(8, 10)
fig.tight_layout()
plt.show()
#plt.savefig("acceptable_spherical_mirrors.png")
