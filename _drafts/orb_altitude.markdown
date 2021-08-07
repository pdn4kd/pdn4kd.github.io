---
layout: post
title:  "Orbital Mechanics: Best Altitudes"
date:   2018-10-01 00:00:00 -0500
categories: astrodynamics, Kerbal Space Program
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

As soon as a new KSP player attempts interplanetary travel (or even to the Mün), they will want to enter/exit orbit in the most efficient way possible. Does it make sense to try to do a braking burn far away when you're going slowly, or can the Oberth effect help you more close in? Without aerobraking, the answere is not completely intuitive, and ΔV saved can spell the difference between success and failure.

Planet gravitational parameter: $$\mu$$
Planet radius: $$r_1$$
Target orbital altitude (with respect to the planet's center): $$r_2$$

# Just barely getting into orbit
Spending as little ΔV as possible means capturing into what amounts to a parabola (in reality a very eccentric ellipse due the finite size of planetary [SOIs][SOI wiki]. 

# Okay, but what about circularizing?
In principle, an extreme ellipse is also the best orbit to do a transfer burn home in, provided you burn at periapsis. In reality, that may not be practical, so it's worth looking at circularization costs.

# And if I'm heading to an airless rock, where should I land?
Burning directly to/from a transfer orbit from/to a landing site isn't actually that absurd. Sure, it reduces flexability in where you can land, but it does surprisingly well in terms of ΔV. To wit:


[SOI wiki]: https://en.wikipedia.org/wiki/Sphere_of_influence_(astrodynamics)
