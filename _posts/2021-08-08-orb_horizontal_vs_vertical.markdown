---
layout: post
title:  "Orbital Mechanics: Horizontal vs Vertical Ascents"
date:   2021-08-08 00:00:00 -0400
tags: astrodynamics KSP
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

A common KSP newbie question is some form of "why do I want to go sideways instead of up?" The most common reason is that atmospheric drag doesn't matter as much as gravity drag, but sometimes the Oberth effect still means that sideways maneuvers are more efficient. Assume that you're on the surface of a perfectly spherical planet with no atmosphere, and have a rocket with infinite TWR...

# Definition of terms
Planet gravitational parameter: $$μ$$

Planet radius: $$r_1$$

Target orbital altitude (with respect to the planet's center): $$r_2$$

Energy of an orbit in a few different ways: $$E = \frac{v^2}{2}-\frac{μ}{r} = \frac{μ}{r_1+r_2}$$ (where $$v$$ is current speed, $$r$$ is current altitude, $$r_1$$ is periapsis, and $$r_2$$ is apoapsis)

# Vertical Ascent
Altitude that you can reach with a given $$\Delta v$$ expenditure:
$$\frac{1}{r_2} = \frac{v^2}{2μ} - \frac{1}{r_1}$$ or $$r_2 = \frac{-2μ r_1}{v^2 r_1 - μ}$$

Expenditure for going straight up:
$$\Delta v = \sqrt{2μ(\frac{1}{r_1}-\frac{1}{r_2})}$$

For comparison, getting to a circular orbit at the surface is
$$\Delta v = \sqrt{\frac{μ}{r_1}}$$. This means that if $$r_2 = 2 r_1$$, the cost is the same as getting into a surface skimming orbit. At apoapsis, your speed is 0, so circularizing is the same as the velocity of a circular orbit. 

So for getting into a circular orbit by vertically burning and then circularizing: $$Δv = \sqrt{2μ(\frac{1}{r_1}-\frac{1}{r_2})} + \sqrt{\frac{μ}{r_2}}$$

# Horizontal Ascent
If for some reason, you want to get to the altitude by going sidewise: $$v = \sqrt{2μ(\frac{1}{r_1}-\frac{1}{r_1+r_2})}$$

At apoapsis, your speed is: $$\sqrt{2μ(\frac{1}{r_2}-\frac{1}{r_1+r_2})}$$

And given that non-zero speed, circularization Δv is: $$\sqrt{\frac{μ}{r_2}} - \sqrt{2μ(\frac{1}{r_2}-\frac{1}{r_1+r_2})}$$

Finally total cost is: $$Δv = \sqrt{2μ(\frac{1}{r_1}-\frac{1}{r_1+r_2})} + \sqrt{\frac{μ}{r_2}} - \sqrt{2μ(\frac{1}{r_2}-\frac{1}{r_1+r_2})}$$

# Comparison and Conclusion
These Δv costs of getting to a given altitude, circularizing, and overall for getting to orbit can be graphed generically with a few assumptions. Setting the planet's gravitational parameter and radius to 1, they look like:

![Horziontal vs vertical ascent components.](/images/ascents.png "Graph of Δv vs apoapsis for horizontal vs vertical ascents into a circular orbit at a given altitude. Δv has been normalized so that a circular orbit at 1 planetary radius is 1.0 and escape is √2 or about 1.4.")

(With this normalization, a circular orbit at the surface is 1, and escape is √2 or ~1.4.

That is, if you can avoid gravity and drag losses, vertical is always better for a given altitude but horizontal is always better for getting an orbit. The difference decreases with more distant orbits, though, and reaches 0 at infinite altitude / escape.

That both methods have maximally expensive altitudes for getting into orbit is somewhat surprising, though presumably related to the way initial ascent costs increase while circularization decreases. For the horizontal case in particular, I suspect that this is reinventing the Hohmann transfer.

Finally, these also work in reverse, so the best way (if possible) to deorbit on an airless body is to lower your periapsis to the surface, and then do a horizontal suicide burn. At typical KSP speeds and TWRs, this is quite plausible.
