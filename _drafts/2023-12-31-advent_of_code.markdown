---
layout: post
title:  "Advent of Code 2023"
date:   2023-12-31 23:59:59 -0500
categories: coding
---
This year, for the first time, I participated in the [Advent of Code](https://adventofcode.com), a 25-day set of small coding puzzles/challenges. You're free to approach them most-any way you want, so I used my existing Python knowledge, though tried to build things out a bit.

Anyway, my final "score" was:
![leaderboard](!/images/advent2023.png)

And you can find how I did everything at: [repolink](repolink)

## General thoughts
The puzzles were mostly fun, and reminded me of various Zachtronics games (albeit with way more resources on-hand and fewer targets for the leaderboard). I probably need to build out my skills a lot, since I generally took an hour or two per puzzle, while most people needed <30 minutes. I also need to better generalize, know what tools I have on-hand (it's *Python*, I have so many libraries...), and just get better at parsing inputs. Performance (at least to the point of avoiding giant arrays), probably also.

## Specific Challenges

# Day 01:
My solutions are I think good for what they do. The problem is that they do something silly: going through literally every possible number on a line, stopping at the last one they find (having run out of line) instead of doing something smart with the break command or the like and stoping at the first one. As best I can tell `continue` doesn't do anything and `break` doesn't do enough for what I want?

# Day 0s63:
There was an initial attempt to be clever and use physics. Namely, the boat distance can be considered as $$S = (a \cdot x) (T - x)$$, where a is the acceleration (1 in this problem), x is the time spent waiting, and T is the overall time. This can be rearranged into a quadratic formula, so presumably the wait times for whatever the current record holder is can be found.

I couldn't get it to work (probably some algebra error or something on my part), so just went with checking all possible times (there were few enough times and races that this was fine).

# Day 07:
Part 1
This was a struggle for a while because of datatype issues. It also took me a few hours to figure out how to use the re module. But at least I now know a few regular expressions.

Part 2
I mostly ran into logic issues with how to handle the wild cards. But also a typo (or regex error) that made for a very subtle and frustrating bug. Debugging also made the code much messier and less elegant. Though in the process I'm pretty sure that it can now handle some kinds of bad data.

# Day 08-1
I'm looking at a serious compute limitation, assuming no bugs. It takes >>1e6 steps (and probably >1e7, if not >1e8!)

# Day 09
I wasn't able to do this on the day of.

# Day 10:
Part 1 was fairly straightforward, just took a while to implement (including some debugging bits and better understanding how to manipulate datatypes). I have no idea how to start with part 2.

# Day 11
Aside from getting delayed by other things, this was straightforward.

# Day 12:
I'm unsure on how to even start this.
