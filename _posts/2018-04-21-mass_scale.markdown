---
layout: post
title:  "Interplanetary travel in other star systems I"
date:   2018-04-22 18:30:00 -0400
tags: Exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Inspired by [a recent arxiv/scientific american article][arxiv] even if it's somewhat flawed. Interstellar travel with practical timescales implies speeds of at least a few percent c, far beyond the escape requirements any plausible star system or the capabilities of chemical rockets. And yet, dramatic effects on in-system travel are still possible.

# Derivation #
Theoretically, the luminosity of a main sequence star (especially one that is relatively sunlike) can be well approximated with a power law: $$L = M^x$$. Usually [x is around 4][stellar power laws], but things get messy once you get away from about 0.5 to 2 solar masses or if you want high precision. The literature [has][Mann 2015] [multiple][general parameters] [cases][m dwarf parameters] of messy polynomials for exponents.

Irradiation is of the form $$S \sim L/a^2$$, where a is the planet's semi-major axis. Here we want a constant S at around that of Earth's (ignoring that it can be a bit higher for bluer stars and a bit lower for redder stars}. So $$a \sim \sqrt{L/S} \sim \sqrt{L} = \sqrt{M^x}$$

Orbital periods are of the form $$T^2 \sim a^3/M$$ so $$T \sim \sqrt{a^3/M}$$. Substituting, $$T \sim \sqrt{M^{3x/2-1}} = M^{3x/4 - 1/2}$$

For a circular orbit, $$V \sim \sqrt{M/a} = \sqrt{M/M^x/2} = M^{1/2-x/4}$$  


# Our solar system around "typical" A and K stars #
For $$x = 4$$, so $$T \sim M^{2.5}$$ and $$V \sim M^{-0.5}$$

$$2^{2.5} = 5.657$$ $$2^{-0.5} = 0.707$$
$$0.5^{2.5} = 0.177$$ $$0.5^{-0.5} = 1.4142$$

What would our solar system analog around a 2 solar mass (early to mid A) or 0.5 solar mass (late K to early M) star be like? A year could range from over five and a half earth years to a little over two months. Perhaps not as extreme as around eg: TRAPPIST-1, but still rather non-trivial.

Orbital velocities would scale less dramatically from 70% of Earth's 30 km/s to 141%. But, given the exponential nature of the rocket equation, these are hiding deeper difficulties.

(rocket equation, and mass ratio of 20/traveling 3x exhaust velocity)

Next time, let's look at a simple Hohmann approximation of a Mars flyby under these conditions, and/or the more extreme case of going between the TRAPPIST-1 planets.



So for luminosity scaling faster than $$M^2$$, planets orbit faster around lower mass stars/transfer orbits require more ΔV. Year length (and therefore transfer times) will decrease for scaling faster than $$M^{2/3}$$. So interplanetary travel/space exploration for a civilization around a red dwarf would require larger rockets, but smaller life support systems than our own. The reverse would be true for a civilization around an A star. (Higher mass stars do not live long enough to be relevant.)



[arxiv]: https://arxiv.org/abs/1804.03698
[stellar power laws]: https://en.wikipedia.org/wiki/Mass%E2%80%93luminosity_relation
[general parameters]: http://adsabs.harvard.edu/abs/2008A%26A...489.1107B
[m dwarf parameters]: http://adsabs.harvard.edu/abs/2000A%26A...364..217D
[Mann 2015]: http://adsabs.harvard.edu/abs/2015ApJ...804...64M
