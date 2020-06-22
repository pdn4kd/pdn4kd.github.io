import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker, cm

#generic portion of a sphere
θs = np.linspace(0,np.pi,200)
ys = [2*np.pi*(1-np.cos(θ)) for θ in θs]

def area(θ):
	'''takes input angle for a portion of a sphere (in degrees), and outputs the area (in degrees)'''
	return 2*180*180/np.pi*(1-np.cos(θ*np.pi/180))


fig, ax1=plt.subplots()
ax1.plot(θs, ys, linewidth=3, color="#000000")
ax1.set_xlim(0,np.pi)
ax1.set_ylim(0,4*np.pi)
ax1.set_xlabel("Angle From Pole (Radians)")
ax1.set_ylabel("Area on Sphere (Steradians)")
ax1.set_title("Basic Sphere")

ax2 = ax1.twinx()
ax2.set_ylim(0,180*180*4/np.pi)
ax2.set_ylabel("Area on Sphere (Square Degrees)")
ax3 = ax1.twiny()
ax3.set_xlim(0,360)
ax3.set_xticks(np.linspace(0,360,7))
ax3.set_xlabel("Angle From Pole (Degrees)")
#θsdeg = [θ*180/np.pi for θ in θs]
fig.set_size_inches(7.2, 5.4)
#fig.savefig("tlax.png", dpi=100, format="png")


#single measurement -- how much of the sky can we see?
θs = np.linspace(0,np.pi/2,200)
θsdeg = [θ*180/np.pi for θ in θs]
singleskydeg = [64800/np.pi*(1-np.cos(np.pi/2 - θ)) for θ in θs] #How much of the sky can we see for an elevation angle above the horizon?
singleskyfrac = [0.5 * (1-np.cos(np.pi/2 - θ)) for θ in θs] #How much of the sky can we see for an elevation angle above the horizon?
fig, bx1 = plt.subplots()
bx1.plot(θsdeg, singleskydeg, linewidth=3, color="#000000")
bx1.set_xlim(90,0)
bx1.set_ylim(0,20626.48)
bx1.set_xlabel("Elevation Above the Horizon (Degrees)")
bx1.set_ylabel("Area Covered (Square Degrees")

bx2 = bx1.twinx()
bx2.plot(θsdeg, singleskyfrac, linewidth=3, color="#000000")
bx2.set_ylabel("Area Covered (Fraction of Sky)")
bx2.set_ylim(0,0.5)

bx3 = bx1.twiny()
bx3.xaxis.set_tick_params(labeltop='on')
bx3.set_xlabel("Zenith Angle (Degrees)")
bx3.set_xlim(0,90)

bx1.set_title("Sky Available vs Telescope Pointing")
fig.set_size_inches(7.2, 5.4)
#fig.savefig("tlbx.png", dpi=100, format="png")


# Yearly sky-ish
N = 100
φsite = np.linspace(0,90,N) #Site latitude (North pole to equator) in distance from pole
θelevation = np.linspace(0,90,N) #telescope elevation
#θzenith = 90-θelevation
#θsite = 90+φsite # sky visible at site
#θsite = np.linspace(np.pi/2,np.pi,N) #yearly sky visible due to site latitude, things are mirrored on the other side of the equator, we can ignore that
#θzenith = np.linspace(0,np.pi/2,N) #telescope maximum zenith angle

X, Y = np.meshgrid(φsite, θelevation)
Z = area(180-X-Y)-area((Y-X + abs(Y-X))/2) #weird numbers to convert to sky visible at lattitude and elevation angle to zenith angle, as well as avoid double-counting the circumpolar environment.
steps = np.linspace(0,41252.96,11)

fig, cx = plt.subplots()
#cs = cx.contourf(X, Y, Z, locator=ticker.logLocator(), cmap=cm.cubehelix)
cs = cx.contourf(X, Y, Z, levels=steps, cmap=cm.cubehelix)
#cx.imshow(grid)
cbar = fig.colorbar(cs)
cx.set_xlabel("Site Latitude (Degrees From Equator)")
cx.set_ylabel("Telescope Minimum Elevation Above Horizon (Degrees)")
cx.set_title("Yearly Sky Available (Square Degrees)")
fig.set_size_inches(7.2, 5.4)
#fig.savefig("tlcx.png", dpi=100, format="png")


#circumpolar viewing zone
Z = area((X-Y + abs(X-Y))/2)
#Z = area(90-X-Y)
fig, dx = plt.subplots()
steps = np.linspace(0.001,20626.48,11)
cs = dx.contourf(X, Y, Z, levels=steps, cmap=cm.cubehelix)
cbar = fig.colorbar(cs)
dx.set_xlabel("Site Latitude (Degrees From Equator)")
dx.set_ylabel("Telescope Minimum Elevation Above Horizon (Degrees)")
dx.set_title("Circumpolar Viewing Area (Square Degrees)")
fig.set_size_inches(7.2, 5.4)
#fig.savefig("tldx.png", dpi=100, format="png")

'''
#few parts of circumpolar viewing zone
fig, ex = plt.subplots()
xs = np.linspace(0.90,N)
area0 = area(xs)
area20 = area((abs(xs-20)+xs-20)/2)
#area30
ex.plot(xs, area0, label="distance from pole in circumpolar region")
ex.plot(xs, area20, label="20 degrees from pole, increasing zenith angle")
ex.set_xlim(0,90)
ex.set_ylim(0,4*np.pi)
ex.set_xlabel("Degrees")
ex.set_ylabel("Area Coverage (degrees^2)")
ex.legend(loc=2)
#fig.savefig("tlex.png", dpi=100, format="png")
'''
plt.show()
