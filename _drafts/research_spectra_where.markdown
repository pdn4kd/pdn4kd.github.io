---
layout: post
title:  "My Research: What Wavelengths Should We Look in?"
date:   2017-10-01 00:00:00 -0400
tags: Exoplanets, Research, Spectra
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# What is RV info
We need features in spectra to even be able to spot a red/blue shift. So, absorption (or rarely emission) lines. In principle, the RV information in a given part of a spectrum is proportional to the slope of the spectrum there. More slope/features means more things that can be cross-correlated to find the radial velocity to greater precision.

# Temperature (and other things) vs RV info
More T means more light! (but at a varying range)
Lines available vary with temperature. In principle cooler is better (more lines), but it's complicated.

The lines in stellar atmospheres are also affected by rotation rates, surface gravity, and metallicity. A faster rotation rate spreads out the lines, reducing the precision of RV measurements. So does the higher pressure implied by higher surface gravity. Metallicity affects the number and depth of lines. As long as they are not saturated or blending together, more/deeper lines mean more precise radial velocity measurements.

# Earth's Atmosphere/Tellurics
Unfortunately, most telescopes are stuck at the bottom of a fluid layer. At the blue end you get Rayleigh scattering, cutting off basically all light in the near UV. This scattering also gives you lots of stray light from ground sources (light pollution), and the moon if it's up.

In NIR, this is the nightmare. Lots of line absorption (especially from water) that will give you all sorts of spurious readings, ruining you precision. As long as you don't go past Y-band, everything is okay, but at that point you're basically still in visible light. (And quite possibly using a visible CCD cooled to 253 K)

(ATRAN data of NIR in general, and iLocator in particular, showing the line problems. Even if the starlight available is good, those telluric lines... Hence going to space)

My research included generating a more or less accurate visible wavelength model. Using data from McDonell Observatory(link), and CFHT(link), I went with an estimate of the optical depth of the sky being: $$\tau = \frac{1}{cos(\theta)} \cdot ((\frac{\lambda}{3080 A})^4 + 0.09) \cdot exp(-\frac{altitude}{8400 m})$$. The 8400 m scale height is adjustable if desired.

(graph of the results)

# Temperature vs Wavelength
The brightest wavelength scales with $$\frac{1}{T}$$, but the typical range of stars spans only about a factor of 4 in temperature. The practical range is closer to a factor of 2, so any reasonably broad spectrograph can cover all of it.

# putting it all together
and now for some graphs


[Bottom 2013]: http://iopscience.iop.org/article/10.1086/670174
[Beatty 2015]: http://iopscience.iop.org/article/10.1086/684264
