---
layout: post
title:  "Scaling Stellar P-mode pulsations/oscillations"
date:   2024-04-22 13:40:00 -0400
tags: astronomy stars research exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Or, an example of what my research can look like, and solving a minor problem to make simulations more realistic.

## Stellar Pulsations
Stars are not just serene spheres sitting in the sky. For that matter, they're not just spinning spheres with [limb darkening](https://en.wikipedia.org/wiki/Limb_darkening) (despite [my implementation](https://github.com/pdn4kd/reimagined-palm-tree) of [Beatty and Gaudi 2015](dx.doi.org/10.1086/684264)). They wobble and oscillate, with all sorts of acoustic waves bouncing through their interiors.

## The P-mode Specifically
This is a "pressure" mode, and is the most important one in (more or less) sun-like stars. It's a huge hassle for us in the RV community (because it adds a spurious signal), and so we want to remove it. The simple version is to observe the star for a timescale that's comparable to the length of the oscillation, so it averages out. For the sun this is about 5 minutes, though it varies with stellar mass, radius, etc. Also, if you get it wrong, you get *reduced* RV precision.

In my (admittedly rather brief) initial search of the literature[^1][^2][^3][^4][^5], it looked like the vast majority of the work is in characterization details. While useful for modeling the stellar interior, those details are unrelated to what I want (removing the "noise"). However, the typical timescale for the p-mode appears to more or less match up with the dynamical timescale:

$$ τ_{dyn} = \sqrt{\frac{R^3}{GM}} = \sqrt{\frac{1}{G\rho}} $$

(Some older works apparently would divide the typical pulsation period by the dynamical timescale to show details in trends)

So I went with that. The p-mode compensation sets a minimum time (in seconds) of:

$$ τ_{pmode} = 300 \sqrt{\frac{R^3}{M}} $$

Where R and M are in solar units.


Immedately after running simulations with this, I found that some sources[^6][^7] took a more sophisticated approach, using effective temperature and surface gravity:

$$ ν_{max} = 3100 \ μHz \ \left(\frac{g}{g_{☉}}\right)^1 \ \left(\frac{T_{eff}}{T_{eff,☉}}\right)^{-0.5} $$

Where the effective temperature is in kelvins and the surface gravity is in cm/s. However, normally surface gravity is given in $$log_{10}(cm/s)$$, so I started with that.

My adopted values for solar surface gravity and effective temperature are: $$T_{eff,☉} = 5778 \ K$$ and $$log(g_{☉}) = 4.438067627303176 $$

Since my code works with a period instead of a frequency, I took one over this. (As an aside, one needs to be careful if using astropy's units here, and tell it to explicitly convert to Hz and/or seconds.)

![comparison](/images/comparison.png) A comparison of our two models, making the assumption that values scale such that (R,T as functions of M)


## Realistic Stars
Using the HWO target list (at least as of 2023-07-26) from the NASA Exoplanet archive, this gives relative distributions of mass, radius, and dynamical times of:

<img src="/images/pmodepdf_all_new.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the new (HWO) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution is relatively narrow, peaking around 1.0." width="49%"> <img src="/images/pmodecdf_all_new.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the same set of stars versus several properties (mass, radius, dynamical timescale). All are in solar units." width="49%">

For comparison, the 'old' (HabEx at the time) target list that I assembled in the late 2010s (and we've more or less deprecated) is:

<img src="/images/pmodepdf_all_old.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the old (HabEx) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution peaks around 1.0 and falls off rapidly, though there are a number of cases of stars that are substantially subsolar or supersolar." width="49%"> <img src="/images/pmodecdf_all_old.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the HabEx stars of the same properties and in the same units." width="49%">

And the [previous paper](https://doi.org/10.3847/1538-3881/acad07)/[technical report](https://exoplanets.nasa.gov/internal_resources/1950)  would have:

<img src="/images/pmodepdf_all_nasa.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the finalized HabEx/NN-EXPLORE list, showing several properties (mass, radius, dynamical timescale). All are in solar units. There are a quite a few stars that are substantially subsolar, as well as a few outliers at up to around 4x solar radius and 8x timescale." width="49%"> <img src="/images/pmodecdf_all_nasa.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of those same stars." width="49%">

(though we only ran fixed 5 minute and 10 minute minimums there)


As for the stars themselves, the lists vary in size and there's some overlap:

<img src="/images/mr_all.png" alt="Mass-Radius diagram for all stellar samples" title="A Mass-Radius diagram of all stars in all samples. There is a range of FGKM main sequence stars (with perhaps an A or two), as well as some subgiants and one actual giant." width="49%">
<img src="/images/mr_old.png" alt="M-R old." title="A Mass-Radius diagram of the stars in the 'old' target list. Mostly AFGK main sequence, though with a handful of subgiants and M-dwarfs." width="49%">
<img src="/images/mr_new.png" alt="M-R new." title="A Mass-Radius diagram of the stars in the 'new' target list. These are more constrainted to being FGK, with the possible subgiants still near the main sequence." width="49%">
<img src="/images/mr_nasa.png" alt="M-R previous." title="A Mass-Radius diagram of the stars used in the previous paper. While mostly FGK, there are a few subgiants and one actual giant (in radius if nothing else)." width="49%">

## The target lists with other method
The actual stellar properties show up a bit differently, but you can still see similar overall patterns (if possibly flipped around, depending on axis choice. This is also part of why we sometimes have 'backward' axes in astronomy.)

<img src="/images/gt_all.png" alt="Surface gravity - effective temperature diagram for all stellar samples" title="A graph of the stars in all 3 target lists, showing surface gravity on the x-axis and effective temperature on the y-axis. The axes are in a 'normal' format instead of using astronomer conventions. A somewhat blobby main sequence stretches from the top left to center right, with a sparse subgiant (if not red giant) branch reaching down to the bottom center." width="49%">
<img src="/images/gt_old.png" alt="G-T old." title="A graph of the stars in 'old' target list, showing surface gravity on the x-axis and effective temperature on the y-axis. The axes are in a 'normal' format instead of using astronomer conventions." width="49%">
<img src="/images/gt_new.png" alt="G-T new." title="A graph of the stars in 'old' target list, showing surface gravity on the x-axis and effective temperature on the y-axis. The axes are in a 'normal' format instead of using astronomer conventions." width="49%">
<img src="/images/gt_nasa.png" alt="G-T previous." title="A graph of the stars in 'old' target list, showing surface gravity on the x-axis and effective temperature on the y-axis. The axes are in a 'normal' format instead of using astronomer conventions." width="49%">

My first attempt (once units were fixed) at the actual scaling ended up with slightly odd results (from using the log instead of the actual surface gravity). While the baseline time is a bit different here (~322 seconds instead of 300), it's multiplied by... almost 1:

In our new target list:

<img src="/images/gmodepdf_all_new.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the new (HWO) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution is relatively narrow, peaking around 1.0." width="49%"> <img src="/images/gmodecdf_all_new.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the same set of stars versus several properties (mass, radius, dynamical timescale). All are in solar units." width="49%">

In the old target list:

<img src="/images/gmodepdf_all_old.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the old (HabEx) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution peaks around 1.0 and falls off rapidly, though there are a number of cases of stars that are substantially subsolar or supersolar." width="49%"> <img src="/images/gmodecdf_all_old.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the HabEx stars of the same properties and in the same units." width="49%">

And in the previous paper's target list:

<img src="/images/gmodepdf_all_nasa.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the finalized HabEx/NN-EXPLORE list, showing several properties (mass, radius, dynamical timescale). All are in solar units. There are a quite a few stars that are substantially subsolar, as well as a few outliers at up to around 4x solar radius and 8x timescale." width="49%"> <img src="/images/gmodecdf_all_nasa.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of those same stars." width="49%">

But all of this was assuming log(g). And the papers just listed g. So trying that (in new/old/previous target list order again):

<img src="/images/gemodepdf_all_new.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the new (HWO) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The distribution of temperatures remains extremely narrow, but that of surface gravities spans a factor of a few, resulting in a distribution more in line with the M-R results." width="49%"> <img src="/images/gemodecdf_all_new.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the same set of stars versus several properties (mass, radius, dynamical timescale). All are in solar units." width="49%">

<img src="/images/gemodepdf_all_old.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the old (HabEx) list, showing several properties (mass, radius, dynamical timescale). All are in solar units. The temperature distribution is quite narrow/close to solar values, though surface gravities (and as a result the actual timescales) range from about 1/5 to 5x that of solar." width="49%"> <img src="/images/gemodecdf_all_old.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of the HabEx stars of the same properties and in the same units." width="49%">

<img src="/images/gemodepdf_all_nasa.png" alt="Mass/Radius/dynamical time PDF." title="A PDF (Probability Distribution Function) / histogram of stars from the finalized HabEx/NN-EXPLORE list, showing several properties (mass, radius, dynamical timescale). All are in solar units. " width="49%"> <img src="/images/gemodecdf_all_nasa.png" alt="Mass/Radius/dynamical time CDF." title="A CDF (Cumulative Distribution Function) of those same stars." width="49%">

That certainly *looks* closer.

## Actual Exposure Times

The details of the model are in my previous work (and Beatty 2015), but we do an estimate of stellar RV information based off model spectra that are scaled based on the star's effective temperature, surface gravity, metallicity, macroturbulence (if available), and rotational velocity. All of which can have a rather larger effect than this bit of noise, depending on the telescope, instrument, star, and desired precision. But we can control for those with what amounts to a grid of simulations and/or choosing nominal instruments.

### Exposure times with the HWO target list

While we only have a few telescope/instrument/sensitivty combinations that are "canonical" (directly based on some actual instruments and probably extrapolations), simulations of combinations of all of them are computationally quite cheap. Looking at the CDFs (Cumulative Distribution FUnctions) of their exposure times. Using a visible light spectrograph nominally modeled on NEID:

<img src="/images/expcdf_neid5_noncanonical_hwo.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neid5_noncanonical_hwo.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neidp_noncanonical_hwo.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_neidg_noncanonical_hwo.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_neide_noncanonical_hwo.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">

And on a near-IR spectrograph nominally modeled on iLocator:

<img src="/images/expcdf_ilocator5_noncanonical_hwo.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocator5_noncanonical_hwo.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocatorp_noncanonical_hwo.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_ilocatorg_noncanonical_hwo.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_ilocatore_noncanonical_hwo.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">

(While I'm using a 3.5 m telescope based off of the WIYN and an 11.88 m telescope that's the combined LBT's mirrors, there are also simulations for a single mirror "half-LBT", with an 8.4 m aperture. But these graphs are already quite cluttered...)

Given our previous 5/10 minute floors, a variable length minimum observation time rarely has an effect. Indeed, we're only obseving short enough for it to matter with the combination of a large telescope and little care about photon noise!

### Exposure times with the old/unsued ('EPRV') target list:
With the Neid analogue:

<img src="/images/expcdf_neid5_noncanonical_eprv.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neid5_noncanonical_eprv.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neidp_noncanonical_eprv.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_neidg_noncanonical_eprv.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_neide_noncanonical_eprv.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">

And the iLocator analogue:

<img src="/images/expcdf_ilocator5_noncanonical_eprv.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocator5_noncanonical_eprv.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocatorp_noncanonical_eprv.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_ilocatorg_noncanonical_eprv.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_ilocatore_noncanonical_eprv.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">

### Exposure times with the previous paper ('HabEx') target list:
Neid:

<img src="/images/expcdf_neid5_noncanonical_habex.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neid5_noncanonical_habex.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_neidp_noncanonical_habex.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_neidg_noncanonical_habex.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_neide_noncanonical_habex.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">

iLocator:

<img src="/images/expcdf_ilocator5_noncanonical_habex.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 5-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocator5_noncanonical_habex.png" alt="Exposure time CDF (5 min)" title="A CDF (cumulative distribution function) of exposure times for a fixed 10-minute p-mode oscillation." width="32%">
<img src="/images/expcdf_ilocatorp_noncanonical_habex.png" alt="Exposure time CDF (p min)" title="A CDF of exposure times for a variable p-mode time scaled off of the dynamical timescale (mass and radius)." width="32%">
<img src="/images/expcdf_ilocatorg_noncanonical_habex.png" alt="Exposure time CDF (g min)" title="An exptime CDF where the minimum p-mode time is scaled off of the log of the surface gravity and the effective temperature" width="32%">
<img src="/images/expcdf_ilocatore_noncanonical_habex.png" alt="Exposure time CDF (e min)" title="An exptime CDF where the minimum p-mode time is scaled off of the surface gravity and effective temperature." width="32%">


## Conclusions

Actual details in terms of observations/precision, etc will be discussed in the paper (in prep). That said, perhaps this can make a case that we can finally kill p-mode oscillations as a noise source once and for all. Which "just" leaves things like granulation, spots/plages (and the associated magnetic activity cycles), flares, etc. (Which admittedly can have *larger* effects than what I'm mitigating here)

And, uh, I'm still mostly ignoring Earth's atmosphere here. (Just [general absorption with no microtellurics]({% post_url 2023-11-30-atmosphere %}))

Once the paper is up, I'll also want to put up these target lists. Stay tuned for more...

[^1]: An Introduction to Modern Astrophysics (Carroll & Ostlie) (aka: The Big Orange Book)
[^2]: An Introduction to the Theory of Stellar Structure (Prialnik)
[^3]: Understanding Stellar Evolution (Henry J G L M Lamers & Emily M Levesque)
[^4]: [Christensen–Dalsgaard 2014](https://users-phys.au.dk/~jcd/oscilnotes/)
[^5]: [Aets et al 2014](https://ui.adsabs.harvard.edu/abs/2010aste.book.....A/abstract)
[^6]: [Luhn et al 2023](https://ui.adsabs.harvard.edu/abs/2023AJ....165...98L/abstract)
[^7]: [Chaplin et al 2019](https://ui.adsabs.harvard.edu/abs/2019AJ....157..163C/abstract)
