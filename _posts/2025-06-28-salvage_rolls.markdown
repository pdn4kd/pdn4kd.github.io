---
layout: post
title:  "Salvaging Bad Character Rolls"
date:   2025-06-28 20:53:01 -0400
tags: gaming probability
---
As a silly exercise, one of the character generation methods in D&D is to roll 3D6 for each stat and just directly accept it in order. No customization. For extra silliness, go with something like 2E, where you roll, then pick your race/class. All classes and some races have stat minimum before modifiers are applied. Yes, this means you can have a character that's incapable of doing anything. Normally this (or just a generally bad roll) would allow for a reroll, and things like the Infinity Engine games will automatically reroll or bump up numbers so you can meet (pre-selected) race/class minimums, but let's see what can happen.

# Humans
Humans do not have any stat requirements.

The easiest classes in terms of requirements are Fighter (9 STR), Thief (9 DEX), Cleric (9 WIS), and Wizard (9 INT). Everything else has an equal or higher minimum in one of those for stats and sometimes in additional stats. 

So a non-viable character would have 8 or lower in those 4 stats, and no constraints on CON or CHA. [The probability of this for one 3D6 roll is 56/216 (7/27), or ~25.9%]({% post_url 2023-11-12-d6prop %}). [For 4/4 rolls, it's that to the 4th power, or ~0.452%]({% post_url 2024-09-30-binomial_fun %}). Interestingly, the probability of rolling up a character that has all 4 classes available is ~30.1%. More amusingly, it's also possible to have a character with total stats of up to 68 (slightly higher than the average roll of 63).

# Demi-humans
Can we still save some of these characters? Yes.

In particular, Elves and Halflings give +1 to DEX, so they can turn an 8 DEX roll into a viable thief under some conditions. Dwarves give +1 to CON (not useful). Gnomes give +1 to INT, which sounds like a way to get a wizard, but they are only allowed to be Illusionists, which also have a requirement of 16 DEX. Which would already work as human thieves if we had that, so can't help. Half-elves don't have any stat modifiers.

Here are the relevant races, and their stat minimums:

|Name|STR|DEX|CON|INT|WIS|CHA|
|-|-|-|-|-|-|-|
|Elf|3|6|7|8|3|8|
|Halfling|7|7|10|6|3|3|

(Halflings and dwarves also have maximum allowed stats, but those aren't relevant because the halfling one would allow for a normal character, and dwarves can't help.)

Elf and Halfling stat minimums are somewhat different, but both allow one to sometiems get a thief. That typed, that they both have a minimum of 7 DEX means you can qualify for the race, but not any class still.

So what situations can choose one of these help? Let's work out the relevant stat ranges:

|Name|STR|DEX|CON|INT|WIS|CHA|Likelihood out of 216^6|
|-|-|-|-|-|-|-|-|
|Elf|3-8|8|7-18|8|3-8|8-18|49062456576|
|Both|7-8|8|10-18|8|3-8|8-18|21724083360|
|Halfling|7-8|8|10-18|6-8|3-8|3-18|56787816960|

For reference, there 216^6 = 101559956668416 total different possible dice rolls, and only 56^4 * 216^2 = 458838245376 (~1:221) of them are not outright viable. 

# The Final Numbers

So putting this all together, the likelood of a salvageable character through choosing a demihuman is 56787816960+49062456576-21724083360 = 84126190176 (~1:1207 characters, and ~1:5.5 overwise non-viable ones). And our final truely non-viable number is 458838245376-84126190176 = 374712055200 (0.369% or 1:271)

Incidentally, the highest possible roll for a non-viable (and unsalvageable) character is 8/7/18/8/8/18. Which is pretty amusing when you realize that it totals up to 67, and in principle you can get a working character with a total as low as 24 (9 in one of STR/DEX/INT/WIS, 3 in all other stats).
