---
layout: post
title:  "Binomial distribution notes and applications"
date:   2024-09-30 20:30:01 -0400
tags: probability binomial
---
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## [The distribution itself](https://en.wikipedia.org/wiki/Binomial_distribution)
For $$n$$ trials, each with a probability $$p$$ of success, the relative probabilities of $$k$$ successes are:
$$P(k) = \left(\frac{n!}{k!(n-k)!}\right) p^k (1-p)^{n-k}$$

The first part is the number of different ways a combination of k successes and n-k failures can occur,with the second being the probability of any 1 specific combination will. Contrast combinations $$\left( ^n_k \right) = \frac{n!}{k!(n-k)!}$$ with with permuations $$\frac{n!}{(n-k)!}$$.

You'll often see a probability of failure: $$q = 1-p$$. This mostly makes the equations a bit more compact. (And it's worth noting that for any given probability $$x$$ in this post, the probabilility of the opposite happening is $$1-x$$, which may be easier to calculate)

As a distribution for $$n$$ repeated trials, the mean is: $$μ_p = n \cdot p$$ and standard deviation is: $$σ_p = \sqrt{n \cdot p \cdot (1-p)}$$


Sampling N times out of a distribution and getting P successes is a bit different.
the mean is: $$μ_p = P/N $$ and the standard deviation is: $$σ_p = \sqrt{\frac{P(1-P)}{N}}$$

(Capitalization matter a lot here, I'm using upper-case P/Q for the raw numbers, and lower case p/q for the probabilities normalized into 0-1.)

## Direct Applications
# 7-game series are not statistically significant
No, seriously, the win-loss results don't tell you if one team is better than another to the standard p-value (0.05). In the most one-sided case (4 wins in a row, last 3 games aren't played), the probability of this happeneing with 2 equally matched teams is $$0.5^4 = 0.0625$$.

# The probability of something that hasn't happened
[John D Cook has noted](https://www.johndcook.com/blog/2010/03/30/statistical-rule-of-three/) that you can estimate the probability of something that hasn't happened (in n trials) as being no more than 3/n. In the large $$n$$ limit, $$(1-3/n)^n$$ approaches (just under) 0.05, though one should take the accuracy with a grain of salt for small samples.

## Empirical version / finding a distribution from trials
If you have a series of N trials with k successes, you can say that your probability of success p is: $$p = \frac{P}{N}$$ (as one would expect)

Also your p is $$μ=\frac{P}{N}$$ of a distribution with a standard deviation of: $$σ_p = \sqrt{\frac{p(1-p)}{N}} = \sqrt{\frac{P(1-P)}{N^3}}$$

Yes, this is as in μ±σ.

# Combining distributions (large N only)
$$μ_{a±b} = μ_a ± μ_b$$ and $$σ_{a±b} = \sqrt{\frac{σ_a^2}{N_a}+\frac{σ_b^2}{N_b}}$$

Which is to say, that the means add/subtract like you'd expect, but the standard deviations are always added in quadrature. If (and only if) you're combining samples from the same distribution, can you bring those error bars down (in an amount proportional to $$\sqrt{N}$$).

# Probability of 2 things being equivalent (large N only)
In essence, given a set of trials and successes from each, do they have the same μ and σ?

We want the difference in distributions:

$$μ_{a-b} = μ_a - μ_b$$ and $$σ_{a-b} = \sqrt{σ_a^2+σ_b^2}$$

And from dealing directly with samples:

$$μ_{a-b} = \frac{P_a}{N_a} - \frac{P_b}{N_b}$$ and $$σ_{a-b} = \sqrt{\frac{P_a (1-P_a)}{N_ai^3} + \frac{P_b (1-P_b)}{N_b^3}}$$

So we can describe the difference between two distributions in standard deviations a z-score:

$$z_{ab} = \frac{μ_{ab}}{σ_{ab}}$$


As an example, this lets us also settle (or rather fail to settle) a long standing question about Shuttle vs Soyuz reliability.

Looking at the shuttle over its lifetime (1981-2011), there were 135 missions, 2 of which resulted in loss of crew. For a more or less comparable Soyuz launch history: from 1967 to 2016, there have been 129 crewed missions, 2 of which resulted in loss of crew:

|Name|Number|LoC failure|Comments|
|-|-|
|Soyuz 7K-whatever (1-40)| 39 | 2|The naming scheme is a mess|
|Soyuz T-1 - 15|15|0|Includes T-10-1 abort, excludes T-1|
|Soyuz TM-1 - TM-34| 33|0|TM-1 was uncrewed|
|Soyuz TMA-1 - TMA-22|22|0||
|Soyuz TMA-01M - TMA-20M|20|0||
|Totals|129|2||

So this means that the probability of a LoC incident with Soyuz was about 0.0155, with a standard deviation of 0.0109. For the shuttle, we get a mean of 0.0148 and standard deviation of 0.0104.

The results 0.0155±0.0109 and 0.0148±0.0104 substantially overlap, and it's notable that for both σ is almost as large as μ. Putting these into the difference equation(s), we get 0.0006891 ± 01505e-2, or a z-score of ~0.0458 (ie: a tiny fraction of a standard deviation).

So with actual flights, they're indistinguishable, and you need to do more sophisticated studies like: https://ntrs.nasa.gov/citations/20110015032 and https://ntrs.nasa.gov/citations/20100014848

(For datasets that do not follow a binomial or normal distribution, you probably want a [K-S test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test).)

## [Probability of a long run](https://arxiv.org/PS_cache/math/pdf/0511/0511652v1.pdf)
We want the probability of getting run of $$r$$ in $$n$$ trials.

For this we have: $$y_n = 1 - β_{n,r} + p^r * β_{n-r,r}$$

$$β_{n,r} = \sum_{l=0}^{n/(r+1)} (-1)^l * nck(n-lr, l) * (q*p^r)^l$$

Where $$nck(n,k)$$ is choosing k unique items for a set of n: $$ nck(n,k) = \frac{n!}{k!(n-k)!}$$

Many places on the net will show you a $$z_n$$, where $$y_n = 1-z_n$$, or $$z_n = β_{n-r,r} - β_{n,r}$$

As a python code:
{% highlight python %}
import numpy as np

def nck(n, k):
    '''classic n choose k, or combinations of k items chosen from a set of n. takes ints n, k. returns n!/(k!(n-k)!'''
    a = np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k)
    return a

def β(n, r):
	'''The probability (y) of getting a run of r successes in n trials, when for any given trial the probability of success is p and of failure is q.'''
    range = np.arange(0, np.floor(n/(r+1))+1)
    b = [(-1)**l * nck(n - l*r, l) * (q * p**r)**l for l in range]
    return (np.sum(b)) 

y = 1 - β(n, r) + p**r * β(n-r, r)
print(y)
{% endhighlight %}

Expect surprisingly high numbers in some cases, especially when $$r \ll n$$.
