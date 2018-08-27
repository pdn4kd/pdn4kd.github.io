---
layout: post
title:  "Optimizing Stage Performance"
date:   2018-10-01 00:00:00 -0500
categories: Kerbal Space Program
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

"How do I best use these parts?" is something that one rapidly runs into in Kerbal Space Program. Should I focus more on the LV-T30 "Reliant", or LV-T45 "Swivel?" Or for a slightly larger rocket, ditch them both and use the "Skipper"?

## Single Stage
The lego-like nature of KSP rockets give analytic solutions to some design problems! If you assume a fixed mission ΔV and TWR (Well, TMR) requirement, then something surprising happens. For a given engine you can find the maximum payload (if any) it can carry on that mission, and how much fuel said payload needs.

# Definition of Terms

# Derivation
$$ \Delta V = g_0 * I_{sp} * ln(\frac{m_1}{m_2}) $$ ([The rocket euqation][Tsiolkovsky the Tyrannical] is always relevant)
$$ TMR = \frac{F}{m_1} $$
$$ m_1 = E + m_t * R + m_p$$
$$ m_2 = E + m_t + m_p$$

Rearranging the rocket equation and substituting:
$$e^{\frac{\Delta V}{g_0 \cdot I_{sp}}} = \frac{m1}{m2}$$
$$m_1 = \frac{F}{TMR}$$
$$m_2 = m_1 - (R-1)*m_p$$
$$e^{\frac{\Delta V}{g_0 \cdot I_{sp}}} = \frac{F/TMR}{F/TMR - (R-1)*m_p}$$

And finally the parameters we want:
$$ m_p (1-R) = \frac{e^{-\frac{\Delta V}{g_0 \cdot I_{sp}}} - 1) \cdot F}{TMR \cdot (1 - R)}$$
$$R*m_t = \frac{F}{TMR} - E - m_p$$


Note that if you're launching in atmosphere, you probably want to use a specific impulse typical of 0.2 atm for a single stage. For a 2-stage design, the first should use 0.5 atm and the upper vacuum. These are emperically derived rules of thumb. Also note that you need enough thrust on the pad to overcome gravity, so if you're using an engine that loses a lot of performance for those first few kilometers...

## Multiple Stage
# Fuel Distribution Between 2 Stages
This is somewhat different in that it assumes a mostly-fixed rocket design, and is merely optimizing for ΔV. Note that this *is not TWR constrained*, and may produce an upper stage incapable of completing the mission. In that case, you can use the maximum weight of the upper stage to define the best useful case.

...

...And you thought you'd never find a use for the quadratic equation...

# Can this be extended?
Somewhat. The TWR constraints mean that the maximum size of the rocket for any given stage is already well defined.

[Tsiolkovsky the Tyrannical]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
