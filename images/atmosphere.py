import numpy as np
from matplotlib import pyplot as plt

absorb1 = np.genfromtxt("extinction.csv", delimiter=',', names=True, dtype=None)
absorb2 = np.genfromtxt("maunakea.csv", delimiter=',', names=True, dtype=None)
#print(absorb1)#Band,Peak,FWHM,MagPerAirmass
#print(absorb2)#Wavelength,MagPerAirmass

xs = np.arange(3000,12000)
ys0 = [((3080/x)**4 + 0.09) for x in xs]
ys1 = [2.5*np.log10(np.e)*((3080/x)**4 + 0.09) for x in xs]
ys2 = [2.5*np.log10(np.e*0.8)*((3080/x)**4 + 0.09) for x in xs]
# τ = (3080 Å/λ)^4 + 0.09
# Intensity = exp(-τ*l), where l is the sec(z) airmass and altitude (exp(-h/8400 m))
# Δmag = -2.5*log10(Intensity) = 2.5*log10(e*l)* ((3080 Å/λ)^4 + 0.09)*)
# So Δmag/l is 2.5*log10(e*l)*τ

fig, ax = plt.subplots(2,1)
ax[0].plot(xs,ys0,label="Fit",color="black")
ax[1].plot(xs,ys1,label="Fit (1 atm)",color="#FF9999")
ax[1].plot(xs,ys2,label="Fit (0.5 atm)",color="#88BBFF")
ax[1].scatter(absorb1["Peak"],absorb1["MagPerAirmass"],label="TAMU",color="#800000")
ax[1].scatter(absorb2["Wavelength"],absorb2["MagPerAirmass"],label="Gemini",color="#0088FF")
#ax.set_title("Absorption vs Wavelength")
ax[0].set_xlabel("Wavelength (Ångströms)")
ax[1].set_xlabel("Wavelength (Ångströms)")
ax[0].set_ylabel("Opacity Coefficient (per Airmass)")
ax[1].set_ylabel("Absorption (Mag per Airmass)")
ax[0].set_xlim(3000,10000)
ax[1].set_xlim(3000,10000)
ax[0].set_ylim(0,1.4)
ax[1].set_ylim(0,1.4)
fig.set_size_inches(8,9)
fig.tight_layout()
ax[1].legend()
ax[0].legend()
#fig.savefig("atmoapprox_fit.png")


fig, bx = plt.subplots(2,1)
zenith_angle = np.linspace(0,1.05)
altitudes = np.linspace(0,20000,300)
airmass_alt0 = [np.exp(-alt/8500) for alt in altitudes]
airmass_alt1 = [np.exp(-alt/8000) for alt in altitudes]
airmass_alt2 = [np.exp(-alt/7500) for alt in altitudes]
airmass_alt3 = [np.exp(-alt/7000) for alt in altitudes]
airmass_angle = [1/np.cos(x) for x in zenith_angle]
θ = [180/np.pi*x for x in zenith_angle]
bx[0].plot(altitudes,airmass_alt0, label="8.5 km")
bx[0].plot(altitudes,airmass_alt1, label="8.0 km")
bx[0].plot(altitudes,airmass_alt2, label="7.5 km")
bx[0].plot(altitudes,airmass_alt3, label="7.0 km")
bx[0].legend()
bx[1].plot(θ,airmass_angle)
#fig.suptitle("Airmass vs Altitude and Angle From Zenith")
bx[0].set_title("Airmass vs Altitude vs Scale Height")
bx[0].set_xlim(0,np.max(altitudes))
bx[0].set_xlabel("Altitude (m)")
bx[0].set_ylim(0,1)
bx[0].set_ylabel("Airmass")
bx[1].set_title("Airmass vs Zenith Angle")
bx[1].set_xlim(0,60)
bx[1].set_ylim(1,2)
bx[1].set_xlabel("Zenith Angle (Degrees)")
bx[1].set_ylabel("Airmass")
fig.set_size_inches(8,9)
fig.tight_layout()
#fig.savefig("atmoapprox_atmosphere.png")


fig, cx = plt.subplots()
zenith_angle = np.linspace(0,1.309,75)
altitudes = np.linspace(0,12001,12001)
airmass_alt = [np.exp(-alt/8000) for alt in altitudes]
#airmass_alt = np.resize(airmass_alt,[50,1])
airmass_angle = [1/np.cos(x) for x in zenith_angle]
Z = np.outer(airmass_alt,airmass_angle)
levels = np.linspace(0,4,17)
contours = cx.contourf(Z, levels, cmap='cubehelix')
cx.set_title("Relative Airmass (Combined, 8 km scale height)")
#cx.set_xticks()
cx.set_xlabel("Zenith Angle (Degrees)")
cx.set_ylabel("Altitude (m)")
cbar = fig.colorbar(contours)
#cbar.set_ylabel("Airmass vs Zenith view at 0 m")
fig.set_size_inches(8,6)
fig.tight_layout()
#fig.savefig("atmoapprox_combined.png")
plt.show()
