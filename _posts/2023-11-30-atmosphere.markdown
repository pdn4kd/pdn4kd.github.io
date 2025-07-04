---
layout: post
title:  "A fast and simple atmospheric absorption approximation"
date:   2023-11-30 00:00:00 -0500
Tags: Astronomy research telescopes atmosphere notes
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


# Why
While site selection matters both in terms of [geometry]({% post_url 2020-06-22-telescope_location %}) for observations, and [weather]({% post_url 2025-07-04-telescope_weather.markdown %}), even on clear nights, the atmosphere will continue to get in the way. Unfortunately a lot of models tend to be fairly complex and not plug and play (eg: [HITRAN](https://hitran.org/) and [US standard atmosphere](https://ntrs.nasa.gov/api/citations/19770009539/downloads/19770009539.pdf?attachment=true)). Worse still, a lot of fancier models are, uh, very proprietary and/or have limited wavelength/frequency coverage. Hence this, which I used my contributions to: the [EPRV technical report](https://exoplanets.nasa.gov/internal_resources/1950) (part of the [EPRV working group report](https://exoplanets.nasa.gov/exep/NNExplore/EPRV/)), [HabEx final report](https://ui.adsabs.harvard.edu/abs/2020arXiv200106683G/abstract), and my [first](https://doi.org/10.3847/1538-3881/acad07), and second first author papers.

# Equations
on site airmass/path length: $$l = \frac{1}{cos(θ_{zenith})}$$

airmass in atmospheres: $$a = exp(\frac{-altitude}{8400 m})$$

atmospheric opacity at a given wavelength: $$κ = (\frac{λ}{3080 Å})^4 + 0.09$$

transmission through the total air at that wavelength: $$exp(-κ \cdot l \cdot a) = exp(-τ \cdot l)$$

# Graphs

![A graph](/images/atmoapprox_fit.png "Two graphs of atmospheric opacity (Top: raw opacity, Bottom: in magnitudes/airmass) from 3000 Å to 10000 Å. The bottom graph also shows the raw data that this was fit to. Since eg: particulates and water vapor are handwaved, there is no way to perfectly reconcile the Hawaii and Texas datasets."
![Airmass vs Altitude.](/images/atmoapprox_atmosphere.png "Top: Airmass as a function of altitude, showing the exponential fall-off for several different scale heights. The fall-off is slow enough to only get to about a factor of 2 at commercial aircraft altitudes. Bottom: Airmass as a function of angle. Airmass increases slowly initially, but then goes off towards infinity near the horizon.")
![A graph](/images/atmoapprox_combined.png "A filled in contour plot of atmospheric absorption as a function of both angle and altitude.")

# Assumptions, utility, and other comments
The equation is calibrated to have one (1) optical depth at 6080 Å. In practice, this models both rayleigh scattering and a baseline of other scattering/absorption and particulates. It does not follow 'real' particulate scattering, which tends to have a much lower scale height (especially in/near optical), and is not line-by line. This is "good enough" for circa 3500-9500 Å, and adequate for ~3000-10'000 Å, despite not including ozone lines or that one big absorption line in the red. The lack of eg: water kills it in the IR proper, though. I'd like to eventually replace it with something more precise, and will take suggestions.

Aerosols in particular [can vary vary enormously over time](https://ui.adsabs.harvard.edu/abs/2020E%26ES..537a2008M/abstract) and by location. I've seen some models based off of the US Standard Atmosphere that include seasonal and/or latitudinal components for that reason. I'd probably get stuck with something empirical and per-site for them (as well as water vapor), though a more detailed model would be nice.

# Sources / How
A pair of listings of emperical observations were hand-fit for the wavelength-dependent absorption:
http://www.gemini.edu/sciops/telescopes-and-sites/observing-condition-constraints/extinction
https://adsabs.harvard.edu/abs/1994IAPPP..57...12S

While not directly used, [Hayes & Latham (1975)](https://ui.adsabs.harvard.edu/abs/1975ApJ...197..593H/abstract), looks at multiple broadband and line absorption sources. Their categorization helped with organizing this, and I'd love to put together something that includes a few more lines.

If you want to recreate this, the graphs were generated with [atmosphere.py](/codeanddata/atmosphere.py), which also used [extinction.csv](/codeanddata/extinction.csv) and [mauneakea.csv](/codeanddata/maunakea.csv) as data sources.
