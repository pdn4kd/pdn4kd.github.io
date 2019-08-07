---
layout: post
title:  "Interplanetary travel in other star systems 3"
date:   2019-07-01 00:00:00 -0400
tags: Exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

[Previously][mass_scale2], there was a limited comparison of our solar system with Kepler-62. But there are far more systems, and far more places to visit within a star system.

How about the entirety (ish) of Sol, Kepler-62, and TRAPPIST-1?

Again: 
For this particular case I am assuming that orbital trips consist of:
* Traveling from a planet's surface to a circular 200 km orbit takes 20% more ΔV than circular velocity. This 20% figure is a rather arbitrary (and possibly pessimistic) way of considering atmospheric and gravity losses, but is at least consistent and should be vaguely accurate. The 200 km altitude is also arbitrary (if perhaps optimistic), but works as a parking orbit for Earth. Assuming thin atmospheres and/or low scale heights, it can be applied elsewhere.
* Hohmann transfers are performed to travelling between planets. Yes, this implies circular coplanar orbits.
* Entering orbit from a transfer, and landing from a 200 km orbit are ambiguous. That is, they may be performed for free, or may cost the full amount of ΔV. They will also be ignored if considered impractical.
* Departing for home (however you choose to define that) is optional and should be considered seperately. We want to look over the full range of exploration options, and how many real world spacecraft have returned from interplanetary space?

# Our solar system around "typical" A, G, and K stars #
This uses the scaling derived in the previous post. Earth and Mars are treated as being in coplanar circular orbits, which is close enough to correct for getting a rough estimate. Their orbits are also assumed to scale in sync.

First, a quick review of the stars/planets involved.

|                     |Sol-G (normal) |Earth                |Mars       |
|---------------------|---------------|---------------------|-----------|
|Mass (kg)            |1.98847542E+030|5.97236473041977E+024|6.4171E+023|
|Radius (m)           |N/A            |6.3781E+006          |3.3895E+006|
|Semi-Major Axis (au) |N/A            |1                    |1.52       |

|            |Sol-A (2.0 M$$_\odot$$) |Earth                |Mars       |
|---------------------|---------------|---------------------|-----------|
|Mass (kg)            |3.97695084E+030|5.97236473041977E+024|6.4171E+023|
|Radius (m)           |N/A            |6.3781E+006          |3.3895E+006|
|Semi-Major Axis (au) |N/A            |4                    |6.08       |

|          |Sol-K (0.5 M$$_\odot$$) |Earth                |Mars       |
|---------------------|-------------|---------------------|-----------|
|Mass (kg)            |9.9423771e+29|5.97236473041977E+024|6.4171E+023|
|Radius (m)           |N/A          |6.3781E+006          |3.3895E+006|
|Semi-Major Axis (au) |N/A          |0.5                  |0.76       |


Now to mix and match orbital maneuvers (rounded to the nearest m/s).

|Star|Earth Surface to Orbit|LEO to Mars Transfer|Mars Surface to Orbit|LMO to Earth Transfer|Round Trip
|----|-------|------|------|------|-------|
Sol-G | 9341 | 3569 | 4145 | 2083 | 19139 |
Sol-A | 9341 | 3405 | 4145 | 1770 | 18671 |
Sol-K | 9341 | 3866 | 4145 | 2654 | 20007 |

Surprisingly, it turns out that the [Oberth effect][Oberth wiki] completely dominates transfers, washing out the differences caused by the varying orbits. These are further washed out if there is any need for expending propellant for descent/ascent, as these are unchanged. Even the most extreme sub-case (returning to Earth from Mars) is only a bit more than 10% larger for the 0.5 M$$_{\odot}$$ late K/early M version of Sol than for the 2 M$$_{\odot}$$ early to mid A version!

If anything, the residents of a solar system analog around a K-type star benefit the most. Interplanetary travel is only modestly more expensive than around an A or F star, and launch windows are up to twice as frequent.

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

Here, the ΔV costs are actually significantly larger. The high planet masses mean that just getting off the surface costs ~2-3x as much as compared with Earth and Mars. This does help somewhat to reduce transfer costs, but those are still quite large. (Larger than the 0.5 M$$_{\odot}$$ case, as these two planets are proportionally somewhat farther apart than Earth and Mars.)
That a flyby of Kepler-62 e from Kepler-62 f costs more ΔV than a Mars orbiter from Earth, and a flyby from e to f is comparable to an Earth-Mars-Earth roundtrip (with aerocapture) is stark comment on just how hard spaceflight may be for some aliens.

The interior planets were ignored from their hellish conditions. Kepler-62 d is more massive than e at 5.5 M🜨, and sees more than double the insolation of Mercury. The innermost two planets are less massive, but with even more starlight...

Transfer windows and flight times:

# TRAPPIST-1
Ah, yes. That [infamous M8V system with 8 planets, 3 of which are in the habitable zone][trappist-1]. Looking at orbiting around or transferring between all of them:

Note that these planets are all fairly massive, with even the lightest being almost 3 times the mass of Mars, and the heaviest slightly more massive than Earth. Despite these masses, the shere closeness has some surprising effects on orbital speeds and spheres of influence. The outer-most are in somewhat familiar ranges, with h's orbital speed being comparable to Venus', and f's being comparable to Mercury's. The rest are impressive speedsters, with b pulling ~82 km/s.
Spheres of influence make Mercury look roomy, ranging from ~20 planetary radii for h to ~4 radii for b. Mind the tides. (for comparison, the moon is ~60 earth radii away)

Transfer orbit ΔVs range from somewhat worse than Mars to Earth through Earth to Mars to minor nightmares. The worst case being trying to get from the surface of b to a flyby of h at over 26 km/s.

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
