---
layout: post
title:  "Interplanetary travel in other star systems 2"
date:   2018-05-31 00:00:00 -0400
tags: Exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# A Patchy Analysis Method
[Patched conics][Patched conics wiki] allow one to approximate orbital maneuvers with an reasonable degree of accuracy by "patching together" a series of Keplerian orbits. Especially cases where only one body dominates at a time, as is typical of the [Hohmann][Hohmann wiki] and [bi-elliptic][bi-elliptic wiki] transfers.

# Our solar system around "typical" A, G, and K stars #
This uses the scaling derived in the previous post. Earth and Mars are treated as being in coplanar circular orbits, which is close enough to correct for getting a rough estimate. Their orbits are also assumed to scale in sync.
(tables)
Surprisingly, it turns out that the [Oberth effect][Oberth wiki] completely dominates, washing out the differences caused by the varying orbits. The most extreme sub-case (returning to Earth from Mars) is only a bit more than 10% larger for the 0.5 $$M_{sun}$$ late K/early M version of Sol than for the 2 $$M_{sun}$$ earl to mid A version!

# Kepler-62
Kepler-62 is a K2V star with 6 known planets orbiting it. Two of them (Kepler-62 e and Kepler-62 f) are a pair of super-earths with insolations that make them plausibly habitable. Taking them as being sort of like Earth and Mars in the above case:
(table)
Here, the ΔV costs are actually significantly larger. The high planet masses mean that just getting off the surface costs ~2-3x as much as compared with Earth and Mars. This does help somewhat to reduce transfer costs, but those are still quite large. (Larger than the 0.5 $$M_{sun}$$ case, as these two planets are proportionally somewhat farther apart than Earth and Mars.)
That a flyby of Kepler-62 e from Kepler-62 f costs more ΔV than a Mars orbiter from Earth, and a flyby from e to f is comparable to an Earth-Mars-Earth roundtrip (with aerocapture) is stark comment on just how hard spaceflight may be for some aliens.


# TRAPPIST-1
This is that infamous M8V system with 8 planets, 3 of which are in the habitable zone. Looking at orbiting around or transferring between all of them:

# Overall
It was surprisingly hard to find good exo-earth analogs. I know that we've found far more hot jupiters and neptunes, but still...

[Patched conics wiki]: https://en.wikipedia.org/wiki/Patched_conic_approximation
[braeunig]: http://www.braeunig.us/space/orbmech.htm
[Hohmann wiki]: https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
[bi-elliptic wiki]: https://en.wikipedia.org/wiki/Bi-elliptic_transfer
[Oberth wiki]: https://en.wikipedia.org/wiki/Oberth_effect
