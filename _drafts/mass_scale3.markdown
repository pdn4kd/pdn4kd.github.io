---
layout: post
title:  "Interplanetary travel in other star systems 3"
date:   2025-07-01 00:00:00 -0400
tags: exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

[A long time ago][mass_scale2], I did a limited comparison of our solar system with scaled versions of itself and with Kepler-62. But there are far more systems, and far more places to visit within a star system.

How about the entirety (ish) of Sol, Kepler-62, TRAPPIST-1, and L98-59?
There are lots of other systems, but these should be adequately representational. It also is going to end up with a lot of table spam.

Again: 
For this particular case I am assuming that orbital trips consist of:
* Traveling from a planet's surface to a circular 200 km orbit takes 20% more ΔV than circular velocity. This 20% figure is a rather arbitrary (and possibly [pessimistic](/2021/08/08/orb_horizontal_vs_vertical)) way of considering atmospheric and gravity losses, but is at least consistent and should be vaguely accurate. The 200 km altitude is also arbitrary (if perhaps optimistic), but works as a parking orbit for Earth. Assuming thin atmospheres and/or low scale heights, it can be applied elsewhere.
* Hohmann transfers are performed to travelling between planets. Yes, this implies circular coplanar orbits. For the chosen systems, this is "good enough".
* Entering orbit from a transfer, and landing from a 200 km orbit are ambiguous. That is, they may be performed for free, or may cost the full amount of ΔV. They will also be ignored if considered impractical.
* Departing for home (however you choose to define that) is optional and should be considered seperately. We want to look over the full range of exploration options, and how many real world spacecraft have returned from interplanetary space?
* Gravity assists and travel times/Δv for eg: brachistochrones will be ignored.

All scaling used is the same [as that derived in the first post](), and all bodies are treated as being in coplanar circular orbits ([as done previously]()). (so eg: stars will be 2x/0.5x their mass, which will result in distances 4x/0.5x what they were before)

# Our solar system around "typical" A, G, and K stars #
(in progress)



# Our solar system with double/half mass planets
(tbd. maybe)

# Kepler-62
[Kepler-62 is a K2V star with 6 known planets orbiting it.][Kepler-62 wiki] Two of them (Kepler-62 e and Kepler-62 f) are a pair of super-earths with insolations that make them plausibly habitable. Taking them as being sort of like Earth and Mars in the above case:

|                 |Kepler-62(0.69 M$$_\odot$$) |e (4.5 M🜨) |f (2.5 M🜨) | 
|---------------------|--------------|---------------------|-----------|
|Mass             | 0.69 M$$_\odot$$ | 4.5 M🜨              | 2.5 M🜨    |
|Mass (kg)            | 1.372e30     | 2.688e25            | 1.493e25  |
|Radius (R🜨)          | N/A          | 1.61                | 1.41      |
|Radius (m)           | N/A          | 1.0268741e7         | 8.993121e6|
|Semi-Major Axis (au) | N/A          | 0.427               | 0.718     |
|Surface to 200 km orbit (m/s)| N/A        | 15707         | 12494     |
|Transfer to other body (m/s)| N/A         | 5857          | 4782      |

(body information from: https://www.science.org/doi/10.1126/science.1234702)

Here, the ΔV costs are actually significantly larger. The high planet masses mean that just getting off the surface costs ~2-3x as much as compared with Earth and Mars. This does help somewhat to reduce transfer costs, but those are still quite large. (Larger than the 0.5 M$$_{\odot}$$ case, as these two planets are proportionally somewhat farther apart than Earth and Mars.)
That a flyby of Kepler-62 e from Kepler-62 f costs more ΔV than a Mars orbiter from Earth, and a flyby from e to f is comparable to an Earth-Mars-Earth roundtrip (with aerocapture) is stark comment on just how hard spaceflight may be for some aliens.

The interior planets were ignored from their hellish conditions. Kepler-62 d is more massive than e at 5.5 M🜨, and sees more than double the insolation of Mercury. The innermost two planets are less massive, but with even more starlight...

Transfer windows and flight times:

# TRAPPIST-1
Ah, yes. That [infamous M8V system with 8 planets, 3 of which are in the habitable zone][trappist-1]. Looking at orbiting around or transferring between all of them:



(using orbit/mass data from: https://arxiv.org/abs/1802.01377)

Note that these planets are all fairly massive, with even the lightest being almost 3 times the mass of Mars, and the heaviest slightly more massive than Earth. Despite these masses, the shere closeness has some surprising effects on orbital speeds and spheres of influence. The outer-most are in somewhat familiar ranges, with h's orbital speed being comparable to Venus', and f's being comparable to Mercury's. The rest are impressive speedsters, with b pulling ~82 km/s.
Spheres of influence make Mercury look roomy, ranging from ~20 planetary radii for h to ~4 radii for b. Mind the tides. (for comparison, the moon is ~60 earth radii away)

Transfer orbit ΔVs range from somewhat worse than Mars to Earth through Earth to Mars to minor nightmares. The worst case being trying to get from the surface of b to a flyby of h at over 26 km/s.

Given that the star TRAPPIST-1 is so low mass, it's also worth looking at a hypothetical system that's a not so late M-dwarf. Say, 2x the mass:

# L98-59
A less well known M-dwarf system, but also with some rocky planets.

# Kepler-90
With 8 planets(!), one of which might be habitable (though could be venus-like if it has an atmosphere), this is at least promising.



# Overall
Apparently planetary masses and relative seperations matter a lot compared with distance to the star. All hail Oberth? This technically doesn't consider how much each extra m/s of ΔV or day of transit time actually matters, but that seems like the sort of detail better suited to an aerospace engineering project or worldbuilding for a specific SF setting. I wonder if [Project Rho][nyrath] has considered these for any planetary system other than our own?

It was surprisingly hard to find good exo-earth analogs. I know that we've found far more hot jupiters and neptunes, but still...

[Patched conics wiki]: https://en.wikipedia.org/wiki/Patched_conic_approximation
[braeunig]: http://www.braeunig.us/space/orbmech.htm
[Hohmann wiki]: https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
[bi-elliptic wiki]: https://en.wikipedia.org/wiki/Bi-elliptic_transfer
[Oberth wiki]: https://en.wikipedia.org/wiki/Oberth_effect
[SOI wiki]: https://en.wikipedia.org/wiki/Sphere_of_influence_(astrodynamics)
[Amazon]: https://www.amazon.com/Fundamentals-Astrodynamics-Dover-Aeronautical-Engineering/dp/0486600610/
[KSP]: http://www.kerbalspaceprogram.com
[nyrath]: https://www.project-rho.com
[kepler-62 wiki]: https://en.wikipedia.org/wiki/Kepler-62
[trappist-1]: http://trappist.one
[mass_scale2]: https://pdn4kd.github.io/2018/08/06/mass_scale2.html
[l98-59]: https://arxiv.org/abs/2507.09343
[kepler-90]: https://arxiv.org/abs/2507.13588
