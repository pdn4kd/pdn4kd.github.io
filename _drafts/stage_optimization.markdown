---
layout: post
title:  "Optimizing Stage Performance"
date:   2018-09-01 00:00:00 -0500
categories: Kerbal Space Program
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

"How do I best use these parts?" is something that one rapidly runs into in [Kerbal Space Program][KSP]. Should I focus more on the [LV-T30 "Reliant"](https://wiki.kerbalspaceprogram.com/wiki/LV-T30_%22Reliant%22_Liquid_Fuel_Engine), or [LV-T45 "Swivel?"](https://wiki.kerbalspaceprogram.com/wiki/LV-T45_%22Swivel%22_Liquid_Fuel_Engine) Or for a slightly larger rocket, ditch them both and use the [RE-I5 "Skipper"](https://wiki.kerbalspaceprogram.com/wiki/RE-I5_%22Skipper%22_Liquid_Fuel_Engine)? The answer is "it depends", but one can use a bit of math to figure out how to use each engine most effectively.

## Single Stage
The lego-like nature of KSP rockets give analytic solutions to some design problems! If you assume a fixed mission ΔV and TWR (Well, TMR) requirement, then something surprising happens. For a given engine you can find the maximum payload (if any) it can carry on that mission, and how much fuel said payload needs.

# Definition of Terms
Most are self explanitory, but:

$$ \Delta V = g_0 \cdot I_{sp} \cdot ln(\frac{m_1}{m_2}) $$ ([The rocket equation][Tsiolkovsky the Tyrannical] is always relevant)

TWR is Thrust to Weight Ratio (N/N, or unitless)

TMR is Thrust to Mass Ratio (N/kg, or kN/Mg)

R is the mass ratio of the fuel tanks. That is, $$R = \frac{full \ mass}{empty \ mass}$$ (unitless, typically 9, but make sure to check)

T is the mass of the *empty* fuel tanks. So for the fully fuelled mass that you see in the VAB/SPH, you'll want to calculate $$R \cdot T$$. This is typically shown in tonnes or Mg, but some mods (eg: KER) will show it in kg. 

# Derivation
$$ TMR = \frac{F}{m_1} $$ (The rocket's necesary accelleration is defined by its highest mass situation)

$$ m_1 = m_{Engine} + m_{Tankage} \cdot R + m_{Payload}$$

$$ m_2 = m_{Engine} + m_{Tankage} + m_{Payload} = m_1 - (R-1) \cdot m_{Tankage}$$

Rearranging the rocket equation:
$$e^{\frac{\Delta V}{g_0 \cdot I_{sp}}} \cdot m_2 = m_1$$

Substituting:
$$e^{\frac{\Delta V}{g_0 \cdot I_{sp}}} \cdot (\frac{F}{TMR} - (R-1) \cdot m_{Tankage} = \frac{F}{TMR}$$

Solving:
$$e^{-\frac{\Delta V}{g_0 \cdot I_{sp}}}


There are, unfortunately, considerable caveats. In particular, the ΔVs, specific impulses, and thrust to mass ratios are sometimes known more by preexisting experience than anything directly accessible ingame or via simple calculation.

Note that if you're launching in atmosphere, you probably want to use a specific impulse typical of 0.2 atm for a single stage. For a 2-stage design, the first should use 0.5 atm and the upper vacuum. These are emperically derived rules of thumb. Also note that you need enough thrust on the pad to overcome gravity, so if you're using an engine that loses a lot of performance for those first few kilometers...

Perhaps the largest flaw in this is that the tankage mass found here cannot be exactly achieved. If you consider the [FL-T100](https://wiki.kerbalspaceprogram.com/wiki/FL-T100_Fuel_Tank) as the smallest available tank, then empty mass must be a multiple of 0.0625 tonnes, and full mass a multiple of 0.5625 tonnes. ie: precision in final stage mass beyond ~0.5 tonnes is impractical with typical tankage. Keeping part counts down may require still greater deviations.

The payload mass is a partial misnomer, since it is really all of the parts of the rocket that are not engines, tankage, or fuel. This "payload" is not just whatever you want to put into orbit, but also any additional control systems, decouplers, fins, etc. that come along for the ride.


# Examples

|Role|Engine|ΔV (m/s)|TMR (m/s²)|Tankage (full, tonnes)|Payload (tonnes)|
|----|------|--|---|--------------|-------|
|Early Expendable SSTO|[LV-T30 "Reliant"](https://wiki.kerbalspaceprogram.com/wiki/LV-T30_%22Reliant%22_Liquid_Fuel_Engine)|3400 (Kerbin → LKO with margin)|14|11.25|2.154|
|Munar lander | [LV-909 "Terrier"](https://wiki.kerbalspaceprogram.com/wiki/LV-909_%22Terrier%22_Liquid_Fuel_Engine) |2700 (Low Kerbin orbit → Munar surface → Kerbin)|5|7.875|3.625|

The SSTO as show is of limited value, but nicely demonstrates an often forgotten aspect of the available design space.

In rounding the Munar lander went with extra ΔV for better landing site selection. Also note that this is far higher mass than a typical lander design.

## Multiple Stage
# Fuel Distribution Between 2 Stages
This is somewhat different in that it assumes a mostly-fixed rocket design, and is merely optimizing for ΔV. Note that this *is not TWR constrained*, and may produce an upper stage incapable of completing the mission. In that case, you can use the maximum weight of the upper stage to define the best useful case.

# Definition of More Terms
$$E_l$$ Engine mass (lower stage)

$$V_{el}$$ Effective exhaust velocity (lower stage), equivalent to $$I_{sp} \cdot g_0$$ for the engine

$$E_l$$ Engine mass (upper stage)

$$V_{el}$$ Effective exhaust velocity (upper stage), equivalent to $$I_{sp} \cdot g_0$$ for the engine

$$P$$ Payload mass

$$S$$ Additional stage mass. That is, the mass penality for having a seperate stage. In KSP terms this is generally the mass of a decoupler or 3. If you prefer conceptual simplicity this could be rolled into the mass of the lower stage engine.



# Calculations
$$a = V_{el} T^2 R (R-1)$$

$$b = T(E_u+P)(V_{eu}(R-1)^2 - V_{el}(R+1)(R-1))$$
$$c = V_{eu}(R-1)(E_u+P)(E_u+E_l+T+P+S)-V_{el}(R-1)(E_u)+P)^2$$

Upper stage fraction of propellant and takage $$ = \frac{-b\pm\sqrt{b^2 - 4ac}}{2a}$$ (choose whichever comes out positive)

And yes, this is a "real world" use of the quadratic equation.

(ex with newbie rocket)

If one continues to play with values, they can get the classic result of mass ratios approaching being the same as the mass of the fuel tanks come to dominate everything else (assuming that the upper and lower stage have the same $$I_{sp}$$). For differing specific impulses, it is preferrable to have the stage with the higher $$I_{sp}$$ (almost always the upper stage) to have a higher mass ratio. The ratio of mass ratios also approaches the ratio of $$I_{sp}$$s for sufficiently tankage dominated rockets, but these are general unachievable within KSP.

(graphs)

# Can this be extended?
Somewhat. The TWR constraints mean that the maximum size of the rocket for any given stage is already well defined. If you are in campaign mode, you may have an explicit mass limit. This does not deal well with the part limit, or details of controllability, though the latter represent a relatively limited portion of the mass of a rocket. Well, barring aerodynamic weirdness.

There are probably more general analytic frameworks that are possible, but I'm no longer anywhere near as involved in KSP as I was when I did the first versions of these equations (circa 2013-2015). That these also predate the 1.0 release are why I do not particularly consider aerodynamics in general, and fairings in particular.

[Tsiolkovsky the Tyrannical]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[KSP]: http://www.kerbalspaceprogram.com
