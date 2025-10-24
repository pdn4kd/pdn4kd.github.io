---
layout: post
title:  "Spherical Abberation in a Spherical Mirror"
date:   2025-10-24 12:30:00 -0400
tags: astronomy telescopes
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# How bad are those spherical mirrors, and how much does it matter in a given telescope?

There's an equation floating around in a few different forms (eg: [Cloudy Nights, which sources it from Texerau](https://www.cloudynights.com/forums/topic/142920-maximum-aperture-and-f-ratio-for-spherical-mirrors/). You'll generally find a form like:

$$e = 22 D/f = 22 D^4/F^3$$

Where D is the diameter in inches, f is the focal ratio in inches, F is the focal length in inches, and e is error in fractions of a wave. You might also see 0.866 or the like if the diameter is in mm.

But where is this from, and what does it mean?

# Deriving the equation(s)
(Information is taken from https://www.telescope-optics.net/index.htm)

Mirrors that aren't parabolic will have spherical abberation, and the amount is well defined by their geometry.

The primary spherical abberation coefficient is $$s = \frac{n(K+1)}{4R^3}$$

The peak aberration is $$S = sd^4 = \frac{n(K+1)D^4}{64R^3} = \frac{n(K+1)D}{512f^3}$$

Here, n is the index of refraction (~1 in air, 1 in vacuum), K is the conic constant (0 for a sphere, -1 for a parabola), R is the radius of curvature, D is the diameter, and f is the focal ratio f = F/D (focal length F = 2R for a sphere). 

Amount of abberation varies with distance d, so the maximum is at the radius = D/2.

Not shown is that there's also a 'defocus' term, and defocus can be used to partially compensate for spherical aberration. So the error at the best focus is better than the what the value of S suggets by a factor of 4. This technically moves the focus point a bit, but it won't be by enough to matter.

The peak aberration, also sometimes written as P-V is the worst case, not the average over the whole mirror. RMS error (which is often more useful) is smaller by a factor of $$1.5 \sqrt{5}$$.

So we can call the compensated RMS error $$W_e = \frac{D}{3072 \sqrt{5}} f^3 = \frac{D^4}{3072 \sqrt{5}} F^3$$, in units of length. 

Alternatively, P-V would be $$W_e = \frac{D^4}{2048 \cdot f^3}$$. Since both are in units of length, you need to divide that error by a target wavelength (eg: 550 nm, though I suspect that it was derived with 562 nm).

Higher order spherical aberrations also exist, and compensating properly for them is different, but also out of scope (pun intended). That's for something with much greater curvature than a spherical mirror newtonian that's usefully slow.

# What does this look like?

# Graphically

Here I'm graphing out the necessary focal lengths and focal ratios for various diameters at either the Rayleigh Criterion (λ/4), or with a tiny bit a headroom (λ/5). The reason for those old telescopes being so silly long quickly becomes apparent.

![Spherical Mirrors Graph](/images/acceptable_spherical_mirrors.png/ "The graph for the earlier derived functions. Both choices of error follow similar patterns, and drive home why large telescopes require parabolization to avoid being unweildy.")

## Comparing a few existing scopes

|Name|Diameter (mm)|Focal Length (mm)|P-V error at 550 nm|
|-|-|-|-|
|(various)|76|700|0.086|
|(various|114|900|0.206|
|Astromaster|114|500|1.200|
|Powerseeker|127|500|1.848|
|Astromaster|130|650|0.923|
|Skyscanner BL135|135|1100|0.222|

And that's why spherical optics can be fine, but you shouldn't get a pseudo bird-jones (they're using 2x barlows to poorly compensate for the errors).

Aiming for a conservative ~λ/5 (leaving room for other errors), a number of good dobs which I will not be building: 130/1100 mm, 140/1200 mm, and 150/1300 mm.

# Strehl ratio
This also gets thrown around a lot as a figure of merit, though it's not quite the same thing as eg: encircled energy. 

It uses the RMS error, and is roughly $$e^{(-2πσ)^2} ≈ 1 - (2πσ)^2 + \frac{(2πσ)^4}{2!} + ... $$

So Peak λ/4 (Rayleigh Criterion) ≈ RMS λ/14 ≈ Strehl of 0.8.

# Conclusions
This gives a rule of thumb for telescope quality, and shows that yes, those long spherical mirrors are fine. The ratios involved do mean that once you get out of small telescopes they become annoyingly long, though.

And finally if you want a canned equation for any telescope with typically shown parameters:

$error = $0.88778 \frac{D^4}{F^3}$$, where D is the Diameter (mm), F is the focal length (mm), and error is the amount in fractions of λ at 550 nm.
