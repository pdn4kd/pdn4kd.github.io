---
layout: post
title:  "Target List Archive"
date:   2025-02-24 19:30:01 -0500
tags: research stars notes
---
My (PhD-related) exoplanet simulations used 3 main target lists, which in various places I've called HWO, EPRV, and HabEx. For ease of access, I'm putting copies of them here, in assorted formats that are relevant.

I'm also including links graphs of the derived properties. No in depth discussions are included (see the paper for those), as these are just for reference, though most of the captions are reproduced. (And indeed, a lot of these derived properties are kind of redundant so not included in the paper)

The tables are not reproduced as markdown because that would just be excessively large.

# HWO
This is derived from [Mamajek & Stapelfeldt (2024)](https://arxiv.org/abs/2402.12414), though the specific data I used is from 2023 and earlier. The initial list is at [the NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)'s HWO ExEP Precursor Science Stars, though they lack v·sin(i) values, which I got from multiple sources (though primarily [Glebocki 2005](https://ui.adsabs.harvard.edu/abs/2005yCat.3244....0G/abstract)).

[The CSV as data](/codeanddata/targetstars_hwo.csv)

[Also a version including citations](/codeanddata/mission_exep_targets.csv)

# EPRV
This is also derived from (a circa fall 2019 version of) Eric Mamajeck's work, and is a composite of a bunch of different datasets. Here, I ended up just directly using it.

His [initial target list](/codeanddata/NASA_mission_study_stars20191023.xlsx) was assembled as an excel file (and, er, google doc), though I worked with [a somewhat cut down CSV version](/codeanddata/emamajeckgreenyellowredlist.csv).

We initially looked at his "[yellow](/codeanddata/targetstars_yellow.csv)" and "[green](/codeanddata/targetstars_green.csv)" lists, then tweaked the green one into a "[green prime](/codeanddata/targetstars_greenprime.csv)" list (with the best exposure times in my code), and then split it by declination into [north](/codeanddata/targetstars_greenprimeN.csv)/[south](/codeanddata/targetstars_greenprimeS.csv) target lists for the simulations proper. (Note that the north/south lists overlap a bit)


If you want to use the [final EPRV version of the "green prime" list](/codeanddata/targetstars_eprv.csv), or a [data-only version of the full listing](/codeanddata/targetstars_all.csv), they're here.


# HabEx
This is the initial dataset that I put together circa 2018, with a target list that was proposed for the then HabEx mission. I ended up modestly altering it (dropping one or two impractical stars, adding one that was part of a distant binary), but mostly just found stellar properties. Most (all?) of the initial members had Hipparcos numbers.

While less important, we looked at a -30° Dec cut as well as some subsets in terms of a blind search, existing planets and a possible deep dive.

The last addition was stellar activity (in terms of Ca H and K indicies, and $$R_{HK}$$, though no cuts were made with this.

[A finalized version](/codeanddata/targetstars_habex.csv) is included, as well as [some that are more 'raw'](/codeanddata/habex_provisional_20190129.csv) ([including the aforementioned stellar activity](/codeanddata/habex_candidate_20190129.csv)).


# Overall List sizes

|List Name|Sublist|Stars|
|--|
|HabEx|(all)|72|
|HabEx|Dec cut|53|
|HabEx|Blind| 63 / 46|
|HabEx|Deep| 13 / 9|
|HabEx|Planets| 8 / 6|
|EPRV|(all)|309|
|EPRV|green|106|
|EPRV|yellow|94|
|EPRV|green prime|101|
|EPRV|green prime north|58|
|EPRV|green prime south|62|
|HWO|(all)|164|
|HWO|Dec cut|114|
