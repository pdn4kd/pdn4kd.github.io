---
layout: post
title:  "Orbital Mechanics: Horizontal vs Vertical Ascents"
date:   2018-10-01 00:00:00 -0500
categories: astrodynamics, Kerbal Space Program
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

A common KSP newbie question is some form of "why do I want to go sideways instead of up?" The most common reason is that atmospheric drag doesn't matter as much as gravity drag, but sometimes the Oberth effect still means that sideways maneuvers are more efficient. Assume that you're on the surface of a perfectly spherical planet with no atmosphere, and have a rocket with infinite TWR...

Planet gravitational parameter: $$\mu$$
Planet radius: $$r_1$$
Target orbital altitude (with respect to the planet's center): $$r_2$$

# Just altitude?
Getting to an orbit at the surface:
$$\Delta v = \sqrt{\frac{\mu}{r_1}}$$

Altitude that you can reach with a given $$\Delta v$$ expendature:
-mu/(0.5v^2-mu/r1) = r2

Expendature for going straight up:
$$\Delta v = \sqrt{2\mu(\frac{1}{r_1}-\frac{1}{r_2}}$$
Incidentally, this means that if $$r_2 = 2 \cdot r_1$$, the cost is the same as getting into (a lower) orbit.

# Okay, but what about getting into an orbit at some altitude?


Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
