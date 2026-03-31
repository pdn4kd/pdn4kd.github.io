---
layout: post
title:  "An Unserious Approach to reforming Date and Time Systems"
date:   2026-04-01 00:00:00 -0400
tags: silliness
---

# The System
The Second is used entirely for short intervals, with SI prefixes as needed. The kilosecond is the most common, occupying a role similiar to the (deprecated) hour. Megaseconds are encouraged, much like sometimes hundreds of days are in the present.

The Day is retained (as 86400 Seconds) because we are trapped on the surface of a spinning oblate spheroid. Synching up day start may require retaining some timezones, though we can get away with maybe half as many as there are currently. Unless you have a job where you care about local solar and sidereal time, object rise/set times barely matter. And if you do, software exists!

The Year is also retained for equivalent reasons. As a unit, it is 365.2425 Days (as per the Gregorian Calendar), but for calendar purposes continues as per the existing Gregorian System. This also slightly changes the length of the lightyear, as that currently uses a Julian Year.
Weeks and months are no longer formal units, rather just day of the year is used. Decades/centuries/millenia are discouraged from formal useage, but remain acceptable informally.

Shorter units of time will continue to use SI prefixes with seconds, though using eg: millidays or centiyears can be accepted in some cases. Likewise for longer time SI prefixes for years with eg: gigaseconds allowed if discussion spans a sufficiently large range of relevant times.

# The Reasoning
The primary problem with a great many measurement systems (including times/dates) is that there are too many besoke units covering too small ranges. This is a familiar frustration to any American in the kitchen, where there are 7 units in common use (teaspoons, tablespoons, ounces, cups, pints, quarts, gallons). All for there being a total of 768 teaspoons in a gallon (ie: the scaling from a teaspoon to a gallon is *smaller* than from a milliliter to a liter). Times aren't as bad, but there are again a bunch of arbitrary units in the middle that are of questionable value given that people can understand numbers with multiple digits.

This is not just an annoyance; jumping through the unit conversion hoops makes it difficult to compare and reason about a great many quantities, especially intermediate sized ones. Indeed, I am in favor of replacing the vast majority of units with SI prefixes and/or scientific notation.

# Anything Else?
Eh, I suppose someone could try silly calenders for Kerbin or Droo.
