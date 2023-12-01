import numpy as np
from matplotlib import pyplot as plt

mass_ratio = np.linspace(1,40,200)
c = 299792458
photon = [1.0, "photon"]
fusion = [0.05, "typ fusion"]
ion = [0.00033, "optimistic HiPEP"] # Isp ~ 10,000 seconds
engines = [photon, fusion, ion]

#generic case of hyperbolic excess vs escape
vi = np.linspace(1,4,1000)
vh = [np.sqrt(v**2-1) for v in vi]

fig, ax = plt.subplots()
ax.plot(vi,vh, label="Actual Velocity")
ax.plot(vi,vi, linestyle='dashed', label="Ignoring Gravity")
ax.plot(vi,vi-1, linestyle='dashed', label="Ignoring Gravity and Periapsis Velocity")
ax.set_xlim(1,4)
ax.set_ylim(0,4)
ax.set_title("Oberth Effect on Escape Velocity (Generic)")
ax.set_xlabel("Periapsis Velocity (multiple of escape velocity)")
ax.set_ylabel("Hyperbolic Excess Velocity (multiple of escape velocity)")
ax.legend()
fig.tight_layout()
#plt.savefig("oberthg.png")
'''
#solar-skimming rocket
vesc = 618 #sun escape
vperi = np.linspace(618,3000,1000)
vhyp = [np.sqrt(vp**2-vesc**2) for vp in vperi]

fig, bx = plt.subplots()
bx.plot(vperi,vhyp, label="Actual Velocity")
bx.plot(vperi,vperi, linestyle='dashed', label="Ignoring Gravity")
bx.set_xlim(500,3000)
bx.set_ylim(0,3000)
bx.set_title("Oberth Effect on Escape Velocity (Sun-skimmer)")
bx.set_xlabel("Periapsis Velocity (km/s)")
bx.set_ylabel("Hyperbolic Excess Velocity (km/s)")
bx.legend()
fig.tight_layout()
#plt.savefig("oberths.png")
'''
#plotting an escape from 1 au
Δv1 = np.linspace(13,3000,1000)
Δv2 = np.linspace(29,3000,1000)
μ = 1.3271244e+11
r1 = 149597870.700
r2 = 695700.000
#earth
v_circ1 = np.sqrt(μ/r1)
v_esc1 = np.sqrt(2*μ/r1)
v_hyp1 = [np.sqrt((dv + v_circ1)**2 - v_esc1**2) for dv in Δv1]
#sun
v_ap = np.sqrt(2*μ*(1/r1 - 1/(r1+r2)))
v_pe = np.sqrt(v_ap**2 + 2*μ*(1/r2-1/r1))# = np.sqrt(2*μ*(1/r2 - 1/(r1+r2)))
v_esc2 = np.sqrt(2*μ/r2)
v_hyp2 = [np.sqrt( (v_pe + dv-(v_circ1-v_ap))**2 - v_esc2**2) for dv in Δv2]
'''
#sun
r3 = 695700000.0*2
v_ap3 = np.sqrt(2*μ*(1/r1 - 1/(r1+r3)))
v_pe3 = np.sqrt(v_ap3**2 + 2*μ*(1/r3-1/r1))# = np.sqrt(2*μ*(1/r3 - 1/(r1+r3)))
v_esc3 = np.sqrt(2*μ/r3)
v_hyp3 = [np.sqrt( (v_pe3 + dv-(v_circ1-v_ap3))**2 - v_esc3**2) for dv in Δv2]
#venus
r3 = r1*0.7
Δv3 = np.linspace(26e3,3000e3,1000)
v_ap3 = np.sqrt(2*μ*(1/r1 - 1/(r1+r3)))
v_pe3 = np.sqrt(v_ap**2 + 2*μ*(1/r3-1/r1))# = np.sqrt(2*μ*(1/r3 - 1/(r1+r3)))
v_esc3 = np.sqrt(2*μ/r3)
v_hyp3 = [np.sqrt( (v_pe3 + dv-(v_circ1-v_ap3))**2 - v_esc3**2) for dv in Δv3]
#mercury
r4 = r1*0.49
Δv4 = np.linspace(26e3,3000e3,1000)
v_ap4 = np.sqrt(2*μ*(1/r1 - 1/(r1+r4)))
v_pe4 = np.sqrt(v_ap**2 + 2*μ*(1/r4-1/r1))# = np.sqrt(2*μ*(1/r4 - 1/(r1+r4)))
v_esc4 = np.sqrt(2*μ/r4)
v_hyp4 = [np.sqrt( (v_pe4 + dv-(v_circ1-v_ap4))**2 - v_esc4**2) for dv in Δv4]
'''

fig, cx = plt.subplots()
cx.plot(Δv1,v_hyp1,label="escape from 1 au")
cx.plot(Δv2,v_hyp2,label="escape after dropping to 1 r☉")
#cx.plot(Δv2,v_hyp3,label="escape after dropping to 2 r☉")
#cx.plot(Δv3,v_hyp3,label="escape after dropping to 0.7 au (venus)")
#cx.plot(Δv4,v_hyp4,label="escape after dropping to 0.39 au (mercury)")
cx.set_title("Oberth Effect for Sundiving")
cx.set_xlim(0,3000)
cx.set_ylim(0,3500)
cx.set_xlabel("Available Δv (km/s)")
cx.set_ylabel("Hyperbolic Excess Velocity (km/s)")
cx.legend()
fig.tight_layout()
#plt.savefig("oberthreal.png")

plt.show()
