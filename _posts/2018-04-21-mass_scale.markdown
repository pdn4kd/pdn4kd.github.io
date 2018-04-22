---
layout: post
title:  "Interplanetary travel in other star systems"
date:   2018-04-21 17:51:44 -0400
tags: Exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Inspired by [a recent arxiv/scientific american post][arxiv] even if it's not a very good article. Interstellar travel with practical timescales implies speeds of at least a few percent c, far beyond the escape requirements any plausible star system or the capabilities of chemical rockets. And yet, dramatic effects on in-system travel are still possible.


The luminosity of a main sequence star (especially one that is relatively sunlike) can be approximated with a power law: $$L = M^x$$. Usually, x is around 4.

Irradiation is of the form $$S \sim L/a^2$$, where a is the planet's semi-major axis. Here we want a constant S at around that of Earth's (ignoring that it can be a bit higher for bluer stars and a bit lower for redder stars}. So $$a \sim \sqrt{L/S} \sim \sqrt{L} = \sqrt{M^x}$$

Orbital periods are of the form $$T^2 \sim a^3/M$$ so $$T \sim \sqrt{a^3/M}$$. Substituting, $$T \sim \sqrt{M^{3x/2-1}} = M^{3x/4 - 1/2}$$

For a circular orbit, $$V \sim \sqrt{M/a} = \sqrt{M/M^x/2} = M^{1/2-x/4}$$


So for luminosity scaling faster than $$M^2$$, planets orbit faster around lower mass stars/transfer orbits require more ΔV. Year length (and therefore transfer times) will decrease for scaling faster than $$M^{2/3}$$. So interplanetary travel/space exploration for a civilization around a red dwarf would require larger rockets, but smaller life support systems than our own. The reverse would be true for a civilization around an A star. (Higher mass stars do not live long enough to be relevant.)

In the 


[arxiv]: https://arxiv.org/abs/1804.03698
