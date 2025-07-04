import numpy as np
from matplotlib import pyplot as plt
#Typ colors: "#EE000090" "#FFAA8890" "#0000EE90" "#88AAFF90" "#000000FF" "#AAAAAA90"

weather = np.genfromtxt("SiteWeather.csv", delimiter=',', dtype=None, encoding=None, names=True)
fig, ax = plt.subplots()
ax.plot(weather['Day'], weather['Mauna_Kea'], linewidth=2, color="#EE000090", label="Mauna Kea")
ax.plot(weather['Day'], weather['Kitt_Peak'], linewidth=2, color="#FFAA8890", label="Kitt Peak")
ax.plot(weather['Day'], weather['Calar_Alto'], linewidth=2, color="#0000EE90", label="Calar Alto")
ax.plot(weather['Day'], weather['Las_Campanas'], linewidth=2, color="#88AAFF90", label="Las Campanas")
ax.plot(weather['Day'], weather['Sutherland'], linewidth=2, color="#000000FF", label="Sutherland")
ax.plot(weather['Day'], weather['Siding_Spring'], linewidth=2, color="#AAAAAA90", label="Siding Spring")
ax.set_xlabel("Day of Year")
ax.set_ylabel("Fraction of Clear Nights")
ax.set_title("Site Weather")
ax.set_xlim(1,365)
ax.set_ylim(0,1)
ax.legend(loc=0)
plt.tight_layout()
#fig.savefig("SiteWeather.png", dpi=100, format="png")
#fig.savefig("SiteWeather.pdf", dpi=100, format="pdf")
plt.show()
