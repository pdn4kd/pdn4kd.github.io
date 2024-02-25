---
layout: post
title:  "Planet Detection I - A Quick Heuristic"
date:   2024-03-01 00:00:00 -0500
Tags: Astronomy research telescopes exoplanets
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


# Introduction
Assuming you have a bunch of [RV observations of a star](https://en.wikipedia.org/wiki/Doppler_spectroscopy), and want to find a planet, what can you find? Or alternatively, what portions of the parameter space can you plausibly eliminate if you don't find anything? Injection/Recovery tests are the gold standard, but there are ways that require way less compute and can simplify our noise concerns.

This is a quick extension / less formal writeup of what I did in the [EPRV technical report/my contribution to the EPRV final report](https://exoplanets.nasa.gov/exep/NNExplore/EPRV/). It also was used in [my first](https://ui.adsabs.harvard.edu/abs/2023AJ....165..151N/abstract), and will be used in my second first author papers. We're citing/using work first done by [Gaudi and Winn (2007)](https://ui.adsabs.harvard.edu/abs/2007ApJ...655..550G/abstract). 

# Basic Model
For a more or less arbitrary set of observation of a planet in an unknown circular orbit around some star, you can have a detection at:
$$SNR = \frac{K}{σ} \sqrt{\frac{N_{obs}}{2}}$$ 

Or you can describe the smallest signal K you can detect at an SNR you trust: $$K = σ \cdot SNR \sqrt{\frac{2}{N_{obs}}}$$

In these equations: SNR is the signal to noise ratio of the detection, K is the semi-amplitude of the planet, σ is the measurement uncertainty, and $$N_{obs}$$ is the number of observations. If you're confirming a knownish orbit, the 2 goes away. This also implicitly assumes an edge-on orbit, though in reality, an inclined circular orbit will be much the same. Just with K scaling with the sine of the inclination angle. (so within a factor of 2 if you're within 60° of edge-on)

In my work, we look at SNRs for K = 10 cm/s (because Earth induces a 9 cm/s reflex velocity on Sol), and Ks for SNR = 10 (which is a reasonably strong/trustworthy detection). These can be subject to degredations from ignored noise factors, so unless the results overperform the SNR = 10 and K = 10 cm/s combination, EPRV surveys will greatly struggle to produce good direct imaging terrestrial planets!

# Derivation
While [Gaudi and Winn](https://ui.adsabs.harvard.edu/abs/2007ApJ...655..550G/abstract) do not go into detail on the derivation of this (it's really a minor footnote in a bunch of other stuff in the paper), after corresponding with him and my advisor, here's a full version:

$$χ²$$ is a measure of goodness of fit. Specifically:

$$χ² = \left(\frac{data-model}{noise}\right)^2$$

And as $$data - model = signal$$, $$χ² = SNR²$$

For a circular orbit, the RV signal is 'just' a sine function.  If you assume uniformly sampled data over an integer number of orbital periods, you can just fold the time series and write the RV as a function of phase $$φ_i$$ of each measurement $$i$$ as:

 
$$RV(φ_i) = K \cdot sin(φ_i) + γ$$
 
Where γ is the barycentric velocity, which we can just assume is zero without loss of generality.
 
Assume all N measurements have equal uncertainty σ and are independent and Gaussian distributed, the χ² of a straight light fit (no signal) is:

$$χ²= \sum_i=1^N [K \cdot sin(φ_i)/σ]² = K²/σ² \cdot \sum_1^N [sin(φ_i)]²$$

As $$N \rightarrow \infty$$, we can covert the Reimann sum into a definite integral:

$$χ²= (K²/σ²) \cdot N \cdot (\frac{1}{2π}) \int_{φ=0}^{2π} sin²(φ)$$

The integral is equal to $$π$$, so the $$χ²$$ is:

$$χ²= \frac{K² N}{2σ²}$$

and the $$SNR = \sqrt(χ²) = \frac{K}{σ} \sqrt(\frac{N}{2})$$


Of course, the sampling isn't all that uniform due to observing seasons, TACs, etc, but since I'm assuming long dedicated surveys at multiple sites, this is less of an issue. We have so many observations packed into the observing period that most orbits should be well sampled. Even more so if the planets have orbits relatively far from one year. (Preferably shorter to avoid fencepost errors, but I'm looking at 10 year surveys, so up to perhaps 3 years is okay.)

More subtly, this $$χ²$$ is not exactly the pearson correlation coefficient, even though SNR² ~ χ².

# Extensions
So far, so good for a single instrument with all measurements at the same precision. But often in surveys (including the ones I'm simulating), we can have multiple heterogeneus instruments, and want to combine their obsevations. And indeed we can, and the equation still works out. In my first paper, we consider precision limits in terms of photon noise (from the star) and instrument noise.

For architectures I, IIa, IIb, V, and VI, this takes the form of:

$$SNR = \frac{K}{\sqrt{2}} \sqrt{\frac{N_{obs}}{\sigma_{inst}^2 + \sigma_γ^2}}$$

$$K = \frac{SNR \sqrt{2}}{\sqrt{\frac{N_{obs}}{\sigma_{inst}^2 + \sigma_γ^2}}}$$

While for architecture VIII:

$$SNR = \frac{K}{\sqrt{2}} \sqrt{\frac{Nobs_{small}}{\sigma_{inst}^2 + \sigma_{γ,small}^2} + \frac{Nobs_{large}}{\sigma_{inst}^2+\sigma_{γ,large}^2}}$$

$$K = \frac{SNR \sqrt{2}}{\sqrt{\frac{Nobs_{small}}{\sigma_{inst}^2 + \sigma_{γ,small}^2} + \frac{Nons_{large}}{\sigma_{inst}^2+\sigma_{γ,large}^2}}}$$

These last two equations are because this architecture observes to higher precision on the larger (but lower availability) telescopes than on the smaller ones. Architecture IIa *does not* use this, as the target precisions are the same on the large and small telescopes. All instruments are also identical within a given architecture.

All of the above are for a single site, but aside from the equations getting longer/messier, there's nothing preventing one including more inside the square root. We assume that all measurements have the same precision mainly because doing the RV calculation for every observation takes too long. (I'm pretty sure that this is due to bad coding on my part and would like to fix it eventually, but it's minor unless we're also simulating telluric or stellar noise, doing injection/recover with actual planet signals, etc)

While paper 1 only looked at instrument/photon noise, we can (and plan to) also include uncorrected tellurics. ie:

$$SNR = \frac{K}{\sqrt{2}} \sqrt{\frac{N_{obs}}{\sigma_{inst}^2 + \sigma_γ^2 + \sigma_\oplus^2}}$$

$$K = \frac{SNR \sqrt{2}}{\sqrt{\frac{N_{obs}}{\sigma_{inst}^2 + \sigma_γ^2 + \sigma_\oplus^2}}}$$

(These are reverting back to single telescope/site, as I'm focusing on different aspects than the "more telescopes with bigger glass at more sites" that we got in paper 1.)
