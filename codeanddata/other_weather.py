import numpy as np
from matplotlib import pyplot as plt
#Typ colors: "#EE000090" "#FFAA8890" "#0000EE90" "#88AAFF90" "#000000FF" "#AAAAAA90"
'''
All sites that have nominal weather:
CalarAlto1
CalarAlto2
CTIO
KPNO
LaSilla
Magellan
MaunaKea
MMT
SSO
Sutherland
WIYN
'''
weather = np.genfromtxt("SiteWeather_all.csv", delimiter=',', dtype=None, encoding=None, names=True)
fig, ax = plt.subplots()
ax.plot(weather['Day'], weather['MaunaKea'], linewidth=2, color="#EE000090", label="Mauna Kea")
ax.plot(weather['Day'], weather['WIYN'], linewidth=2, color="#FFAA8890", label="Kitt Peak")
ax.plot(weather['Day'], weather['CalarAlto2'], linewidth=2, color="#0000EE90", label="Calar Alto")
ax.plot(weather['Day'], weather['LaSilla'], linewidth=2, color="#88AAFF90", label="Las Campanas")
ax.plot(weather['Day'], weather['Sutherland'], linewidth=2, color="#000000FF", label="Sutherland")
ax.plot(weather['Day'], weather['SSO'], linewidth=2, color="#AAAAAA90", label="Siding Spring")
ax.set_xlabel("Day of Year")
ax.set_ylabel("Fraction of Clear Nights")
ax.set_title("Site Weather (Report)")
ax.set_xlim(1,365)
ax.set_ylim(0,1)
ax.legend(loc=0)
plt.tight_layout()
#fig.savefig("SiteWeather_pub.png", dpi=120, format="png")
#fig.savefig("SiteWeather_pub.pdf", dpi=120, format="pdf")

fig, bx = plt.subplots()
bx.plot(weather['Day'], weather['CTIO'], linewidth=2, color="#EE000090", label="CTIO")
bx.plot(weather['Day'], weather['LaSilla'], linewidth=2, color="#0000EE90", label="La Silla")
bx.plot(weather['Day'], weather['Magellan'], linewidth=2, color="#000000FF", label="Magellan")
bx.set_xlabel("Day of Year")
bx.set_ylabel("Fraction of Clear Nights")
bx.set_title("Site Weather (Chile)")
bx.set_xlim(1,365)
bx.set_ylim(0,1)
bx.legend(loc=0)
plt.tight_layout()
#fig.savefig("SiteWeather_cl.png", dpi=120, format="png")
#fig.savefig("SiteWeather_cl.pdf", dpi=120, format="pdf")
fig, dx = plt.subplots()
dx.plot(weather['Day'], weather['KPNO'], linewidth=2, color="#FFAA8890", label="KPNO")
dx.plot(weather['Day'], weather['MMT'], linewidth=2, color="#88AAFF90", label="MMT")
dx.plot(weather['Day'], weather['WIYN'], linewidth=2, color="#AAAAAA90", label="WIYN")
dx.set_xlabel("Day of Year")
dx.set_ylabel("Fraction of Clear Nights")
dx.set_title("Site Weather (Arizona)")
dx.set_xlim(1,365)
dx.set_ylim(0,1)
dx.legend(loc=0)
plt.tight_layout()
#fig.savefig("SiteWeather_az.png", dpi=120, format="png")
#fig.savefig("SiteWeather_az.pdf", dpi=120, format="pdf")
fig, cx = plt.subplots()
cx.plot(weather['Day'], weather['CalarAlto1'], linewidth=2, color="#000000FF", label="CalarAlto1")
cx.plot(weather['Day'], weather['CalarAlto2'], linewidth=2, color="#AAAAAA90", label="CalarAlto2")
cx.set_xlabel("Day of Year")
cx.set_ylabel("Fraction of Clear Nights")
cx.set_title("Site Weather (Spain)")
cx.set_xlim(1,365)
cx.set_ylim(0,1)
cx.legend(loc=0)
plt.tight_layout()
#fig.savefig("SiteWeather_es.png", dpi=120, format="png")
#fig.savefig("SiteWeather_es.pdf", dpi=120, format="pdf")

plt.show()
