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

How about the entirety (ish) of Sol, Kepler-62, TRAPPIST-1, L98-59, and Kepler90?
There are lots of other systems, but these should be adequately representational. It also is going to end up with a lot of table spam.

For this particular case I am looking at trips that consist of:
* Traveling from a planet's surface to a circular 200 km orbit. All three of the orbital speed at that altitude, an idealized 2 burn trasfer from the surface, and 20% more ΔV than circular velocity. This 20% figure is a rather arbitrary (and possibly [pessimistic](/2021/08/08/orb_horizontal_vs_vertical)) way of considering atmospheric and gravity losses, but is at least consistent and should be vaguely accurate. The 200 km altitude is also arbitrary (if perhaps optimistic), but works as a parking orbit for Earth. Assuming thin atmospheres and/or low scale heights, it can be applied elsewhere. I'll try to note planets where this is silly (eg: gas giants)
* Hohmann transfers are performed to travelling between planets. Yes, this implies circular coplanar orbits. For the chosen systems, this is usually "good enough".
* I include the Oberth effect in the typical patched conic way (orbit goes from the nominal SOI edge to 200 km altitude).
* Typical transfer and wait times are considered, but overall Δv is *not* added up. Just note that starting a transfer from body x to body y is the same as ending one from body y to body x (assuming no aerobraking).
* Gravity assists and travel times/Δv for eg: brachistochrones are also being ignored. Things are complicated and messy enough even in the simple case.

All scaling used is the same [as that derived in the first post](mass_scale1), and all bodies are treated as being in coplanar circular orbits ([as done previously](mass_scale2)). (so eg: stars will be 2x/0.5x their mass, which will result in distances 4x/0.5x what they were before)

[The raw spreadsheet(s), including some systems that were ultimately ignored](/codeanddata/interplanetary_scaling3.ods)

# Our solar system around "typical" A, G, and K stars #
(in progress, but given how different other systems seem to be, maybe a bad example)[^1]

# Our solar system with double/half mass planets
(tbd. maybe)

# Kepler-62
[Kepler-62 is a K2V star with 6 known planets orbiting it.][Kepler-62 wiki] Two of them (Kepler-62 e and Kepler-62 f) are a pair of super-earths with insolations that make them plausibly habitable. The masses are generally poorly measured, with only maximum estimates.[^2] As such, I am using plausible values found via ???


# TRAPPIST-1
Ah, yes. That [infamous M8V system with 8 planets, 3 of which are in the habitable zone][trappist-1].[^3]


Note that these planets are all fairly massive, with even the lightest being almost 3 times the mass of Mars, and the heaviest slightly more massive than Earth. Despite these masses, the shere closeness has some surprising effects on orbital speeds and spheres of influence. The outer-most are in somewhat familiar ranges, with h's orbital speed being comparable to Venus', and f's being comparable to Mercury's. The rest are impressive speedsters, with b pulling ~82 km/s.
Spheres of influence make Mercury look roomy, ranging from ~20 planetary radii for h to ~4 radii for b. Mind the tides. (for comparison, the moon is ~60 earth radii away)

Transfer orbit ΔVs range from somewhat worse than Mars to Earth through Earth to Mars to minor nightmares. The worst case being trying to get from the surface of b to a flyby of h at over 26 km/s.

Given that the star TRAPPIST-1 is so low mass, it's also worth looking at a hypothetical system that's a not so late M-dwarf. Say, 2x the mass:

# L98-59
A less well known M-dwarf system, but also with some rocky planets.[^4] At ~4x the mass of TRAPPIST-1, it also helps to fill in the details of various systems.

# Kepler-90
With 8 planets(!), one of which might be habitable (though could be venus-like if it has an atmosphere), this is at least promising.[^5] The host star is also sun-like (1.2 $$M_🜨$$).



# Overall
Apparently planetary masses and relative seperations matter a lot compared with distance to the star. All hail Oberth? This technically doesn't consider how much each extra m/s of ΔV or day of transit time actually matters, but that seems like the sort of detail better suited to an aerospace engineering project or worldbuilding for a specific SF setting. I wonder if [Project Rho][nyrath] has considered these for any planetary system other than our own?

It was surprisingly hard to find good exo-earth analogs. I know that we've found far more hot jupiters and neptunes, but still...

# Data Sources
[^1]: Wikipedia, as the solar system bodies are generally known well to high precision.
[^2]: For Kepler-62, the 2013 discovery paper is used: https://www.science.org/doi/10.1126/science.1234702
[^3]: [A 2018 update on the masses of the TRAPPIST-1 planets](https://arxiv.org/abs/1802.01377), and [a 2017 study of TRAPPIST-1 with Spitzer data](https://academic.oup.com/mnras/article/475/3/3577/4795334) for their periods and the star's properties.
[^4]: The 2025 discovery of a 5th planet around L98-59: https://arxiv.org/abs/2507.09343
[^5]: Kepler-90 uses a 2025 study for the masses of g and h: https://arxiv.org/abs/2507.13588


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
[mass_scale1]: https://pdn4kd.github.io/2018/04/27/mass_scale1.html
[mass_scale2]: https://pdn4kd.github.io/2018/08/06/mass_scale2.html
[l98-59]: https://arxiv.org/abs/2507.09343
[kepler-90]: https://arxiv.org/abs/2507.13588
