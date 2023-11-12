---
layout: post
title:  "Scaling Stellar P-mode pulsations/oscillations"
date:   2023-12-01 00:00:00 -0500
categories: astronomy stars research exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Stellar Pulsations
Stars are not just serene spheres sitting in the sky. For that matter, they're not just spinning spheres with [limb darkening](https://en.wikipedia.org/wiki/Limb_darkening) (despite [my implementation](https://github.com/pdn4kd/reimagined-palm-tree) of [Beatty and Gaudi 2015](dx.doi.org/10.1086/684264)). They wobble and oscillate, with all sorts of acoustic waves bouncing through their interiors.

# The P-mode specifically
This is a "pressure" mode, and is the most important one in more or less sun-like stars. It's a huge hassle for us in the RV community (because it adds a spurious signal), and so we want to remove it. The simple version is to observe the star for a timescale that's comparable to the length of the oscillation, so it averages out. For the sun this is about 5 minutes, though it varies with stellar mass, radius, etc. Also, if you get it wrong, you get *reduced* RV precision.

In my (admittedly rather brief) search of the literature [^1][^2][^3][^4][^5] it looks like the vast majority of the work is in characterization details that, while useful for modeling the stellar interior, are unrelated to what I want (removing the "noise"). But the typical timescale for the p-mode appears to more or less match up with the dynamical timescale:

$$ τ_{dyn} = \sqrt{\frac{R^3}{GM}} = \sqrt{\frac{1}{G\rho}} $$

(Some older works apparently would divide the typical pulsation period by the dynamical timescale to show details in trends)

So I went with that. The p-mode compensation sets a minimum time (in seconds) of:

$$ 300 \sqrt{\frac{R^3}{M}} $$

Where R and M are in units of the sun.


# Realistic stars
Using the HWO target list (at least as of 2023-07-26) from the NASA Exoplanet archive, this gives relative distributions of mass, radius, and dynamical times of:

<img src="/images/pmodepdf_all_new.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the new (HWO) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution is relatively narrow, peaking around 1.0." width="49%"> <img src="/images/pmodecdf_all_new.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the same set of stars versus several properties (mass, radius, dynamical timescale). All are in solar units." width="49%">

For comparison, the 'old' target list that I assembled in the late 2010s (and we've more or less deprecated) is:

<img src="/images/pmodepdf_all_old.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the old (HabEx) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution peaks around 1.0 and falls off rapidly, though there are a number of cases of stars that are substantially subsolar or supersolar." width="49%"> <img src="/images/pmodecdf_all_old.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the HabEx stars of the same properties and in the same units." width="49%">

And the [previous paper](https://doi.org/10.3847/1538-3881/acad07)/[technical report](https://exoplanets.nasa.gov/internal_resources/1950)  would have:

<img src="/images/pmodepdf_all_nasa.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the finalized HabEx/NN-EXPLORE list, showing several properties (mass, radius, dynamical timescale). All are in solar units. There are a quite a few stars that are substantially subsolar, as well as a few outliers at up to around 4x solar radius and 8x timescale." width="49%"> <img src="/images/pmodecdf_all_nasa.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of those same stars." width="49%">

(though we only ran fixed 5 minute and 10 minute minimums there)


As for the stars themselves, the lists vary in size and there's some overlap:

<img src="/images/mr_all.png" alt="Mass-Radius diagram for all stellar samples" title="A Mass-Radius diagram of all stars in all samples. There is a range of FGKM main sequence stars (with perhaps an A or two), as well as some subgiants and one actual giant." width="49%">
<img src="/images/mr_old.png" alt="M-R old." title="A Mass-Radius diagram of the stars in the 'old' target list. Mostly AFGK main sequence, though with a handful of subgiants and M-dwarfs." width="49%">
<img src="/images/mr_new.png" alt="M-R new." title="A Mass-Radius diagram of the stars in the 'new' target list. These are more constrainted to being FGK, with the possible subgiants still near the main sequence." width="49%">
<img src="/images/mr_nasa.png" alt="M-R previous." title="A Mass-Radius diagram of the stars used in the previous paper. While mostly FGK, there are a few subgiants and one actual giant (in radius if nothing else)." width="49%">

How much this messes with exposure times and the difficulties in compensation are being considered in my next paper (in prep). I plan to throw the target lists up here once it's been published.

[^1]: An Introduction to Modern Astrophysics (Carroll & Ostlie) (aka: The Big Orange Book)
[^2]: An Introduction to the Theory of Stellar Structure (Prialnik)
[^3]: Understanding Stellar Evolution (Henry J G L M Lamers & Emily M Levesque)
[^4]: Christensen–Dalsgaard 2014: https://users-phys.au.dk/~jcd/oscilnotes/
[^5]: Aets et al 2014: https://ui.adsabs.harvard.edu/abs/2010aste.book.....A/abstract
