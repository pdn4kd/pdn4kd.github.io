---
layout: post
title:  "Juno cannot be repurposed to flyby 3I/ATLAS"
date:   2025-07-31 15:30:00 -0400
tags: spaceflight rants
---
<script type="text/javascript" async
   src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


[a recent paper by Avi Loeb's group claims that it is practical to use the Juno spacecraft to execute a flyby of the interstellar comet 3I/ATLAS](https://www.arxiv.org/abs/2507.21402). It makes multiple basic errors showing a lack of research.

# The main engine may not be available
Given valve problems[^2], the engine has not been used since October 2016. Notably this involved cancelling a major maneuver to change the craft's orbit to a shorter period one and this has had knock-on effects in terms of science returns and mission duration.

The RCS engines cannot use the oxidizer and have much lower Isp. My cursory searches did not reveal the models, so this effect will be neglected. I also did not see any way to eg: dump the oxidizer to gain back performance, though as we will see this won't matter. The RCS thrusters also have lower TWR, though I haven't done any calculations as to if the burn times would be too long to make the described mission practical. At a minimum, it would have to be substantially altered from the apparently impulsive burns.

# The maneuver exceeds the craft's remaining Δv
Loeb et al use a mass ratio based on the entire fuel and oxidizer loads at the start of the mission[^0], and an assumed Isp of 340 s.

This is how they arrived at $$340 * 9.8 * ln(\frac{3625}{1593}) = 2740 \ m/s$$, sufficient for the 2675.5 m/s mission shown in table 3 of their paper.

Sources vary on the exact performance of the LEROS 1b engine used by Juno between 316 and 318 s. I'm going with a source from the manufacturer that lists 317 s.[^1] Like them, I am ignoring any considerations of mixture ratio (0.8-0.9 does not match up well with 1280 kg of fuel and 752 kg of oxidizer), and underestimating the usage from correction burns done with RCS.

With this, the initial ΔV is actually at best $$317 * 9.8 * ln(\frac{3625}{1593}) = 2556 \ m/s$$

In the interim Juno has performed a number of maneuvers. Appendix C[^2] shows 11 RCS maneuvers totalling to 22.3 m/s, and 1 main engine at 541.65 m/s. Incorrectly treating the RCS monopropellant usage as part of the main engine's (much higher Isp) bipropellant usage to avoid having to trakc the masses in detail, this would leave a Δv budget of around 1992 m/s. In reality, it must be less.

# Now what
A more hypothetical paper, discussing why it may make sense to park a comet interceptor in an eccentric Jupiter orbit (with Juno purely as a stand-in), could have had a good point. The Δv requirement from this orbit isn't all *that* large, and certainly within the capabilities of a dedicated craft. That typed, I am not a dynamicist, and have not looked at the trade-offs vs keeping a craft on stand-by on Earth, in orbit around ESL-2, etc.

At the same time, I'm left wondering if this paper was inspired by [a previous one](https://arxiv.org/abs/2507.12213) making extremely questionable assumptions from an insufficient Oberth effect.

# Sources
[^0]: [eoPortal](https://www.eoportal.org/satellite-missions/juno#launch)
[^1]: [LEROS 1b Apogee Enginei flyer](https://www.nammo.com/wp-content/uploads/2021/03/2021-Nammo-Westcott-Liquid-Engine-LEROS1B.pdf) ([local PDF](/codeanddata/))
[^2]: [Stumpf, Paul W.; Bhat, Ram S.; Pavlak, Thomas A., 2017, "Maneuver Operations During Juno’s Approach, Orbit Insertion, and Early Orbit Phase"](https://dataverse.jpl.nasa.gov/file.xhtml?fileId=58768&version=2.0) ([local PDF](/codeanddata/))
