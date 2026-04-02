---
layout: post
title:  "Example Data Products (or Something) using WMATA Ridership in Matplotlib and Plotly"
date:   2026-04-02 15:00:00 -0400
tags: resume
---
This is some example data analysis/graphing stuff I threw together as an example of building out skills. [WMATA has an extensive repository of ridership data](https://www.wmata.com/initiatives/ridership-portal/Metrobus-Ridership-Summary.cfm) though you'll often get it in a somewhat annoying format. (The "CSV" is really a UTF-16 TSV, and has an extra row with titles that could have been incorporated into the main set of headers) I also added a 'location' based on the route names.

Please enjoy both a static graph, and a mostly related (if rather hacky) [plotly dashboard](https://70f1f5ab-e69b-497f-aac2-787ec3d15f36.plotly.app/) (caution there's something weird going on so currently firefox doesn't see it as a real thing to connect to):

![Bus Ridership Time Series Breakdown](/images/WMATABuses202512.png "WMATA metrobus ridership (paid and total), for: a 4 year time series (all of the years 2022-2025), and breakdowns of how it changed in each month of 2025 compared with the previous month, and with the same month in 2024. It's possible that Better Bus slightly reduced overall ridership while slightly increasing fare paying ridership.")
![Overall Bus Ridership Time Series](/images/WMATABuses20182025.png "All metrobus ridership (paid and otherwise) since good data first became available in mid 2018. Pre-pandmic ~70-80% of passengers paid fares, with the number going to zero (obviously) while fares were suspended in the depths of it. When fare collection resumed in 2021, only a limited subset (who in absolute terms remained constant) continued to pay, so the ridership recovery since then has not helped WMATA finances. Interestingly, the Better Bus initiative (started late July 2025) has no obvious effect here.")

Why the focus on fare evasion? It's easy to show with the available data, and as someone who has and uses the bus transit here, while being far from a metro stop, I have a strong personal interest in the system working well!

The [Python for the graph](/codeanddata/busridershipfares.py), [collection of WMATA data it uses](/codeanddata/TotalBoardingsPaid.csv), [code for the dashboard](/codeanddata/busridershipall_dash.py), and [collection of WMATA data that it also uses](/codeanddata/WMATA202601.csv) are available.

Building out actual machine learning skills (most likely domain related) is in the works. But I can in fact generalize what I have to some data analysis and creating simple dashboards! If there's interest in expanding this or say putting together an alternate demo with observatory/stellar/exoplanet/survey simulation datasets, feel free to contact me.
