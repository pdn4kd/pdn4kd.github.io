---
layout: post
title:  "Phase Angles in Kerbal Space Program and Juno: New Origins"
date:   2025-08-01 00:00:02 -0400
tags: Games KSP JNO astrodynamics
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

A key part of an [efficient transfer](https://en.wikipedia.org/wiki/Hohmann_transfer_orbit) is launching at the right time. There are lists for these in some cases, but so far they've been rather incomplete. This aims to fix it.

If you're unsure on what a phase angle is, it's the angle between the body you're launching from and the one you're launching towards, as seen from whatever both are orbiting around. I'm using + when the target is ahead of you, and - when it's behind for reasons that will be apparent shortly.


## Derivation
These are relatively simple to calculate. From Kepler's 3rd law, $$T^2 ~ a^3$$

So the period of a transfer orbit is $$T_x ~ a^{3/2} = (\frac{a_1 + a_2}{2})^{3/2}$$

And the distance covered by the target orbit during 1/2 of the transfer orbit period (in fraction of the outer orbit's circle) is $$\frac{1/T_2}{2/T_x} = \frac{T_x /2}{T_2} = 1/2 (\frac{a_1/a_2 + 1}{2})^{3/2}$$

The transfer orbit will cover 180° or π radians in that time, so we want a launch angle that's said 180° minus the distance covered by the target planet. Or: $$θ = π(1-(\frac{a_1/a_2-1}{2})^{3/2}) = 180°(1-(\frac{a_1/a_2-1}{2})^{3/2})$$


# Tables
Some values are (as you can see) a bit silly, so ones that are modulo 360° are also provided. Even so, many inwards transfers don't really care about timing, as you spend so much in flight compared with the target that you can just tweak your orbit slightly to arrive. Outwards transfers eventually converge on $$ π(1-\frac{1}{2\sqrt{2}}) ~= 2.03 $$ radians, or ~116° for sufficiently distant orbits (though you rarely reach that).

The raw data / calculations are [here](/codeanddata/phaseanglesraw.ods).

## Kerbal Space Program (KSP) Planets

Note that Moho, Dres, and Eeloo all have meaningfully large inclinations and eccentricities, so actual transfers may vary significantly.

|From\To | Moho | Eve | Kerbin | Duna | Dres | Jool | Eeloo|
|-|-|-|-|-|-|-|-|
|Moho |  | 58.94| 76.05| 90.64| 103.7| 108.9| 110.7|
|Eve | -129.1|  | 36.07| 66.07| 92.04| 102.2| 105.7|
|Kerbin | -251.8| -54.13|  | 44.36| 82.06| 96.58| 101.4|
|Duna | -518.3| -168.7| -75.19|  | 62.21| 85.52| 93.19|
|Dres | -1469.9| -564.5| -329.7| -145.8|  | 51.95| 68.52|
|Jool | -3177.6| -1258.5| -768.7| -391.1| -99.83|  | 31.01|
|Eeloo | -4729.8| -1882.5| -1160.3| -607.1| -185.4| -43.49| |

Cleaned up a bit, with all angles below 180°:

|From\To | Moho | Eve | Kerbin | Duna | Dres | Jool | Eeloo|
|-|-|-|-|-|-|-|-|
|Moho |  | 58.94 | 76.05 | 90.64 | 103.7 | 108.9 | 110.7|
|Eve | -129.1|  | 36.07| 66.07| 92.04| 102.2| 105.7|
|Kerbin | 108.2 | -54.13|  | 44.36| 82.06| 96.58| 101.4|
|Duna | -158.3| -168.7 | -75.19|  | 62.21 | 85.52| 93.19|
|Dres | -29.86† | 155.5 | 30.32 | -145.8|  | 51.95| 68.52|
|Jool | 62.38† | -178.5†| -48.65†| -31.06| -99.83|  | 31.01|
|Eeloo | -49.75†| -82.54†| -80.33†| 112.9| 174.6| -43.49| |

†Sufficently large (>720°) that I'm assuming that there's a lot of leeway

## KSP Moons

Minmus has notable inclination, Bop and Pol have notable inclination and eccentricity.

| From\To | Mun | Minmus |
|-|-|-|
| Mun |  | 90.49|
| Minmus | -513.8|  |


| From\To | Laythe | Vall | Tylo | Bop | Pol |
|-|-|-|-|-|-|
| Laythe |  | 47.57| 74.94| 95.13| 101.4|
| Vall | -84.86|  | 47.57| 81.75| 92.14|
| Tylo | -240.3| -84.87|  | 59.20| 76.74|
| Bop | -692.2| -324.9| -130.4|  | 37.15|
| Pol | -1158.0| -567.8| -259.4| -56.60|  |

And with all angles within ±180°:

| From\To | Mun | Minmus |
|-|-|-|
| Mun |  | 90.49|
| Minmus | -153.8 |  |

| From\To | Laythe | Vall | Tylo | Bop | Pol |
|-|-|-|-|-|-|
| Laythe |  | 47.57 | 74.94 | 95.13| 101.4|
| Vall | -84.86|  | 47.57| 81.75| 92.14|
| Tylo | 119.7 | -84.87|  | 59.20| 76.74|
| Bop | 27.79 | 35.11 | -130.38|  | 37.15|
| Pol | -77.97†| 152.16 | 100.6 | -56.60|  |


## Juno: New Origins (JNO) Planets

Handrew's Comet has a great deal of eccentricity (as does Cladh, though it's so far out that you shouldn't be using Hohmann-type transfers if you want reasonable travel times.)

| From\To | Vulco | Sergeaa | Droo | Cylero | Handrew's Comet | Tydos | Urados | Cladh |
|-|-|-|-|-|-|-|-|-|
| Vulco |  | 55.14 | 82.19 | 95.40 | 108.3 | 110.2 | 114.7 | 116.3 |
| Sergeaa | -112.3 |  | 53.00 | 78.11 | 101.9 | 105.4 | 113.4 | 116.2 |
| Droo | -331.7 | -103.8 |  | 47.57 | 91.06 | 97.31 | 111.3 | 116.1 |
| Cylero | -705.2 | -275.4 | -84.86 |  | 74.94 | 85.36 | 108.3 | 116.0 |
| Handrew’s Comet | -2821.5 | -1216.2 | -531.5 | -240.3 |  | 31.01 | 95.49 | 115.50 |
| Tydos | -4200.3 | -1820.1 | -812.3 | -387.8 | -43.49 |  | 88.62 | 115.2 |
| Urados | -28598.3 | -12352.7 | -5605.6 | -2839.8 | -710.0 | -461.5 |  | 112.2 |
| Cladh | -3130545.0 | -1338297.6 | -599627.3 | -300316.0 | -75553.3 | -50518.3 | -7379.7 |  |

With more tractable angles:

| From\To | Vulco | Sergeaa | Droo | Cylero | Handrew's Comet | Tydos | Urados | Cladh |
|-|-|-|-|-|-|-|-|-|
| Vulco |  | 55.14| 82.19| 95.40| 108.3 | 110.2| 114.7| 116.3|
| Sergeaa | -112.3|  | 53.00| 78.11| 101.9 | 105.4| 113.4| 116.2|
| Droo | 28.30 | -103.8|  | 47.57| 91.06 | 97.31| 111.3| 116.1|
| Cylero | 14.82 | 84.64| -84.86|  | 74.94 | 85.36| 108.3| 116.0|
| Handrew’s Comet | 58.45† | -136.2† | -171.5 | 119.7 |  | 31.01 | 95.49 | 115.50 |
| Tydos | 119.7† | 20.09† | -92.34† | -27.83 | -43.49 |  | 88.62| 115.2|
| Urados | -158.3†| -112.7†| 154.4† | 40.23† | 10.00 | 101.5 |  | 112.2|
| Cladh | 14.98† | -177.6† | 132.7† | -76.04†| 46.67† | -118.3†| -179.7†|  |


## JNO Moons

TT is in a retrograde orbit (inclination 2.8 radians or ~160°), so is treated as 180° for this (flipping a sign so that the angle is 180° plus the distance the target planet travcels instead of minus). In reality its inclination is still large enough that this doesn't work well.

Herma has a large inclination (0.8 radians, or ~46°) and eccentricity (0.2), so transfers between it and Niobe won't really follow these.

While they're at an angle with respect to the rest of the system, all of Urados' moons are pretty much coplanar.

| From\To | Brigo | Luna | TT |
|-|-|-|-|
| Brigo |  | 47.57 | 282.0 |
| Luna | -84.86 |  | 307.2 |
| TT | 634.1 | 463.1 |  |

| From\To | Niobe | Herma |
|-|-|-|
| Niobe |  | 67.03|
| Herma | -175.0|  |

| From\To | Nebra | Miros | Orcus |
|-|-|-|-|
| Nebra |  | 66.51| 84.63|
| Miros | -171.6|  | 44.17|
| Orcus | -373.8| -74.65|  |

| From\To | Jastrus | Boreas | Taurus | Hypatchion |
|-|-|-|-|-|
| Jastrus |  | 105.7| 112.8| 113.7|
| Boreas | -1893.1|  | 81.48| 90.28|
| Taurus | -9350.2| -320.8|  | 31.33|
| Hypatchion | -14003.7| -507.5| -44.12|  |

And finally with smaller angles (constrained to ±180°):

| From\To | Brigo | Luna | TT |
|-|-|-|-|
| Brigo |  | 47.57 | -78.01 |
| Luna | -84.86 |  | -52.82 |
| TT | -85.91 | 103.1 |  |

| From\To | Niobe | Herma |
|-|-|-|
| Niobe |  | 67.03|
| Herma | -175.0|  |

| From\To | Nebra | Miros | Orcus |
|-|-|-|-|
| Nebra |  | 66.51 | 84.63 |
| Miros | -171.6 |  | 44.17 |
| Orcus | -13.84 | -74.65 |  |

| From\To | Jastrus | Boreas | Taurus | Hypatchion |
|-|-|-|-|-|
| Jastrus |  | 105.7 | 112.8 | 113.7 |
| Boreas | -93.14† |  | 81.48 | 90.28 |
| Taurus | 9.82† | 39.16 |  | 31.33 |
| Hypatchion | 36.26† | -147.5 | -44.12 |  |

# Why these tables?
It seemed to be a gap in information. [KSP has a web app for this](https://ksp.olex.biz/) (and a [porkchop plot calculator](https://alexmoon.github.io/ksp/)), but having the tables in one place is convenient. Also, there appears to be no equivalent in JNO.
