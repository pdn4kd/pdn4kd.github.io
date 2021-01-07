---
layout: post
title:  "Fν, Fλ, Janskys, AB magnitudes, Vega magnitudes, and calcuations between them"
date:   2020-10-28 13:00:00 -0400
Tags: Astronomy, research, units
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

While there are other magnitude systems ([SDSS uses maggies and asinh magnitudes](http://www.sdss.org/dr12/algorithms/magnitudes/)), fluxes and two kinds of Pogson magnitudes are sufficient to cover a lot.


# Janskys (Jy)
The [Jansky]() is, while not technically an SI unit, the closest thing to a One True Flux Unit we have, and the conversions aren't terrible (compare with rad to gray, and sievert to rem). It's possible that the pluralization should be Janskies, but given that it's named after a person, I have doubts.

1 Jansky == 1e-26 W/m²/Hz (MKS), or 1e-23 ergs/s/cm²/Hz (CGS)

That is, the Jansky is an $$F_ν$$ type unit (flux per unit frequency or per unit bandwidth). What are effectively variants of it that directly list power per area per frequency with a different scaling factor show up quite frequently in the literature (often as kJy, though not named that).

The related $$F_λ$$ is in the form of power per area per wavelength. This often leands to slightly clunky-looking things like W/m²/nm or W/m²/Å. $$F_λ$$ units are more common in the visible/NIR where I work than $$F_ν$$, though this is flipped for radio astronomers. The way I've written these here with the greek subscripts is also the preferred IAU method.


# Fν and Fλ usage
To get power back, you'll need to sum up the power per unit wavelength/frequency over the relevant wavelength/frequency band. If this sounds sort of like a Riemann sum, you're correct. In practice, you can often assume that the power in a band is flat (especially if it's narrow), and just multiply by that.

Similiarly, if you have overall flux from a source in some band and want these units, just divide by the wavelength/frequency bad.


# AB magnitudes
The Jansky is functionally closely related to [AB magnitudes](https://en.wikipedia.org/wiki/AB_magnitude). The AB magnitude system (eg: [Oke & Gunn 1983](https://ui.adsabs.harvard.edu/abs/1983ApJ...266..713O/abstract)), is a direct conversion between flux and magnitude, with that flux being constant in all filters.

$$m_{AB} = -2.5\cdot log_{10}(flux_{Jy}) + 8.90 \approx -2.5\cdot log_{10}(\frac{flux_{Jy}}{3630.78 Jy})$$

$$flux_{Jy} = 10^{-0.4 \cdot (m_{AB} - 8.90)} = 10^{0.4\cdot m_{AB}}$$

The origional sources (and wikipedia) tend to show 48.6 instead of 8.9. This is because they are using CGS units (ergs/s/cm²/Hz) for flux instead of Jy. You may also see something slightly different for the magnitude figures ([eg: 48.574](https://arxiv.org/pdf/astro-ph/0502120.pdf)) or zero-point number of Janskys (eg: 3720 Jy). These are based on slightly different calibrations, often related to measurements of the brightness of Vega or generally trying to make sure that in V-band, AB mags and Vega mags are the same.
For completeness:

$$m_{AB} = -2.5\cdot log_{10}(flux_{CGS}) - 48.6$$

$$flux_{CGS} = 10^{-0.4 \cdot (m_{AB} + 48.6)}$$

$$m_{AB} = -2.5\cdot log_{10}(flux_{MKS}) - 56.1$$

$$flux_{MKS} = 10^{-0.4 \cdot (m_{AB} + 56.1)}$$


# Vega magnitudes
These were originally based on the flux of Vega in a given magnitude bin (first V, then others as photography, photoelectric detectors, CCDs, etc developed). "Vega" however you define it, is usually the same magnitude (typically 0.03, though sometimes 0 or something else) in as many bands as possible (ideally all). This means that flux varies quite a bit with the band in question, especially as you move away from Johnson B, V, and R.

Also, "Vega" because sometimes α-Lyr itself is the standard, sometimes an average of several A0V stars is, sometimes a blackbody (anywhere from 9000 K to 11000 K), and sometimes an atmospheric model (eg: Kurucz) is used. You'll need to check a given paper or dataset's methods for what their zero-points are.
This also leads to fun things like [the Sun's V-band magnitude being different (but still within error bars) between the AB and Vega systems](https://arxiv.org/abs/1804.07788).

In general, you can convert a flux into a vega mag with $$-2.5 \cdot log_{10}(\frac{flux_{Jy}}{flux_{Vega}})$$ if you know the Vega flux in that band. (I'm assuming that both are in Jy, but it doesn't matter as long as the units are the same for both)


# Bandwidth and wavelength range
For all of this, I am assuming that one can work with known "end points" (really the FWHM) of a given passband, and that one can treat the flux as being constant across the entire range, then 0 outside of it. This tends to be good enough, though often one just knows the cenerpoint and wavelength range, and wants to do the relevant conversions in as few steps as possible.

Assuming that you know either the max and min wavelengths ($$λ_2$$ and $$λ_1$$), or peak wavelength and FWHM (λ and Δλ) and want the bandwidth (Δν):


$$Δν = ν_1 - ν_2 = \frac{c}{λ_1} - \frac{c}{λ_2} = \frac{c \cdot (λ_2-λ_1)}{λ_1 λ_2} = \frac{c \cdot Δλ}{λ^2 - Δλ^2/4}$$


# A (silly) example

You measure a power/area of 130 W/m² in [V band (λeff = 5448 Å, FWHM = 840 Å per Bessel 2005)](https://doi.org/10.1146/annurev.astro.41.082801.100251), and want the magnitude:

Δν ~= 85.352 THz

flux ~= 1.523e-12 W/m²/Hz = 1.523e14 Jy

AB mag ~= -26.56

Vega mag (using a zero-point of 3720 Jy) ~= -26.53

(Yes, this is of a certain star whose bolometric flux is ~1361 W/m²)
