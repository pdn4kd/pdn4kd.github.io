---
layout: post
title:  "HabEx Targetlist Results Graphs"
date:   2025-02-27 00:00:01 -0400
tags: research stars notes
---
Results are grouped by relevant feature. There is some redundancy in the graphs. All captions should be considered rough notes. This is technically a "second pass" (with the initial one much earlier), though it would be more difficult to easily archive/show the raw data from the "first pass" simulations. (This also does not do any declination, deep, blind, or planets cuts)

## General Feature Histograms / all P-Modes
All 4 p-mode compensation methods are shown as seperate graphs here. They are ordered: fixed 5 minute, fixed 10 minute, scaled with stellar parameters (mass and radius), and scaled with stellar parameters (surface gravity and effective temperature).

# Exposure Times
<img src="/images/HabEx/exppdf_all5_habex.png" width="49%">
<img src="/images/HabEx/exppdf_all10_habex.png" width="49%">
<img src="/images/HabEx/exppdf_allp_habex.png" width="49%">
<img src="/images/HabEx/exppdf_alle_habex.png" width="49%">

Exposure times as histograms (top) and cumulative distribution functions (bottom) for every star in our telescope/instrument combinations. There is a tail of stars with very long exposure times (and which are therefore difficult to observe at high precision). The PDF appears the same for all 3 sets of stars due to the current bin size of 20 minutes, as whatever chosen p-mode correction has little effect beyond that. Due to finer bin sizes, the CDFs do show that the exact distribution of exposure times is shuffled around somewhat, though the effect is again small (and largely confined to telescope/instrument/precision combinations that skew to shorter exposure times). 

In all cases, there is a "tail" of stars that have relatively long exposure times, even for favorable telescope/instrument/precision combinations. For less favorable ones, this "tail" can mean that around half of all stars have exposure times of over two hours (and so are difficult to observe).

(The need to select easy stars for reasons beyond stellar activity feels worth discussing. Alongside how little difference the p-mode choice makes. Perhaps at some point graphs of mass/radius/p-mode timescale be should added?)

<img src="/images/HabEx/expcdf_all5_habex.png" width="49%">
<img src="/images/HabEx/expcdf_all10_habex.png" width="49%">
<img src="/images/HabEx/expcdf_allp_habex.png" width="49%">
<img src="/images/HabEx/expcdf_alle_habex.png" width="49%">

The variable p-mode for high precision raises additional issues, though. Are the short exposure stars changing substantially with required photon noise?
(Adding non-canonical systems might show these effects more clearly)

In any case, the distribution of exposure times is longer here than for the EPRV or HWO target lists, but that cannot be easily seen.

# Observations
<img src="/images/HabEx/obspdf_habex5_10year.png" width="49%">
<img src="/images/HabEx/obspdf_habex10_10year.png" width="49%">
<img src="/images/HabEx/obspdf_habexp_10year.png" width="49%">
<img src="/images/HabEx/obspdf_habexe_10year.png" width="49%">

Histograms of total number of observations for the different telescope/instrument combinations as both PDFs (top) and CDFs (bottom). Differences between different architectures are quite obvious, though the ones between different p-mode compensation methods are subtle (and not apparent for the architectures with longer exposure times and fewer observations).

Because of the details of the target list (both position and exposure times), between around 25 and 40 percent of the target stars are never observed.

<img src="/images/HabEx/obscdf_habex5_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habex10_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habexp_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habexe_10year.png" width="49%">

The distributions of observations are largely similar between different p-mode compensation methods, with the exception of the fixed 10-minute case for otherwise short exposure times (NEID, 3.5 m, 27 cm/s and NIRS, 11.88 m, 40 cm/s). For those two telescope/instrument/precision combinations, a long fixed p-mode timescale increases the exposure times for most of the stars, and causes a noticeable reduction in the number of observations.

In any case, the number of observations for each configuration is smaller than for the EPRV or HWO target lists, but that cannot be easily seen.

# Exposure Times and Observations
<img src="/images/HabEx/Exposure_Time5_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Time10_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Timep_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Timee_Exposure_Number_tradeoffs3py.png" width="49%">

Total number of observations (top) and total time spent observing (bottom) for each star and telescope/instrument combination as a function of exposure time. The p-mode minimum observation times are 5 minutes (right), 10 minutes (center), and variable as a function of stellar properties (right).

<img src="/images/HabEx/Exposure_Time5_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Time10_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Timep_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/HabEx/Exposure_Timee_Total_Exposure_tradeoffs3py.png" width="49%">

Number of observations decrease slowly with increasing exposure time (while time spent on a given star increases) until around 300 minutes, and which point both rapidly decrease as the stars become increasingly impractical to observe.

# Exposure Times and Stellar Parameters
<img src="/images/HabEx/Teff_Exposure_Time5_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/Teff_Exposure_Time10_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/Teff_Exposure_Timep_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/Teff_Exposure_Timee_tradeoffs1py.png" width="49%">

Exposure time as a function of effective temperature for all 4 p-mode oscillation compensation methods. This target list shows a clear trend of increasing observation difficulty for hotter stars, though choice of telescope, instrument, and target precision are more important for GKM stars.

<img src="/images/HabEx/vsini_Exposure_Time5_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/vsini_Exposure_Time10_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/vsini_Exposure_Timep_tradeoffs1py.png" width="49%">
<img src="/images/HabEx/vsini_Exposure_Timee_tradeoffs1py.png" width="49%">

Exposure time as a function of rotational velocity for all 4 p-mode oscillation compensation methods. This target list shows a shallow, but clear trend of increasing observation difficulty for hotter stars, though choice of telescope, instrument, and target precision are more important. Altair (with a vsini of 211 km/s) is not shown, as it would be far off the top-right corner of the plot and is unobservable at our desired precisions.

(And of course, Teff and v·sin(i) are somewhat correlated, with the latter blowing up once you get hotter than [~6200 K...](https://en.wikipedia.org/wiki/Kraft_break))

# Right Ascension and Declination
<img src="/images/HabEx/RAVsObsNum_habex5_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsNum_habex10_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsNum_habexp_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsNum_habexe_lin.png" width="49%">

Total number of observations per star as a function of Right Ascension (top) and Declination (bottom). There is a clear trend in right ascension, we believe from a combination of night length and weather (though it is suppressed for longer exposure time telescope/instrument/precision combinations). That the peak corresponds with stars that have the longest time above the horizon in fall (around 270 degrees) and not winter/early spring (when the weather is better and nights longer) is surprising. (Will eventually need to check on weather, is this accurate?)

<img src="/images/HabEx/DecVsObs_habex5_lin.png" width="49%">
<img src="/images/HabEx/DecVsObs_habex10_lin.png" width="49%">
<img src="/images/HabEx/DecVsObs_habexp_lin.png" width="49%">
<img src="/images/HabEx/DecVsObs_habexe_lin.png" width="49%">

Declination does not show a clear trend, with number of observations per star being relatively flat north of about -40 degrees. Below that, stars are never observed. (This is somewhat surprising, perhaps our earlier -30 dec cut was pessimistic? At least for sites in Arizona.)

The unobserved stars at more northerly declinations should all have long exposure times. (ie: impractical to observe regardless of location)

<img src="/images/HabEx/RAVsObsTime_habex5_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsTime_habex10_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsTime_habexp_lin.png" width="49%">
<img src="/images/HabEx/RAVsObsTime_habexe_lin.png" width="49%">

Total observation time per star as a function of Right Ascension (top) and Declination (bottom). No clear trends are visible. (And given the lack of anything interesting along with this likely being an unimportant measure, it's unlikely to be in the paper. Just here as a reference)

<img src="/images/HabEx/DecVsObsTime_habex5_lin.png" width="49%">
<img src="/images/HabEx/DecVsObsTime_habex10_lin.png" width="49%">
<img src="/images/HabEx/DecVsObsTime_habexp_lin.png" width="49%">
<img src="/images/HabEx/DecVsObsTime_habexe_lin.png" width="49%">


## Observation Counts and Detection Heuristic / Per P-mode
# Fixed P-mode (5 minute) Results
<img src="/images/HabEx/obspdf_habex5_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habex5_10year.png" width="49%">

<img src="/images/HabEx/snrpdf_habex5_10year.png" width="49%">
<img src="/images/HabEx/snrcdf_habex5_10year.png" width="49%">

<img src="/images/HabEx/kpdf_habex5_10year.png" width="49%">
<img src="/images/HabEx/kcdf_habex5_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Fixed P-mode (10 minute) Results
<img src="/images/HabEx/obspdf_habex10_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habex10_10year.png" width="49%">

<img src="/images/HabEx/snrpdf_habex10_10year.png" width="49%">
<img src="/images/HabEx/snrcdf_habex10_10year.png" width="49%">

<img src="/images/HabEx/kpdf_habex10_10year.png" width="49%">
<img src="/images/HabEx/kcdf_habex10_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Variable P-mode (M-R) Results
<img src="/images/HabEx/obspdf_habexp_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habexp_10year.png" width="49%">

<img src="/images/HabEx/snrpdf_habexp_10year.png" width="49%">
<img src="/images/HabEx/snrcdf_habexp_10year.png" width="49%">

<img src="/images/HabEx/kpdf_habexp_10year.png" width="49%">
<img src="/images/HabEx/kcdf_habexp_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Variable P-mode (g-T) Results
<img src="/images/HabEx/obspdf_habexe_10year.png" width="49%">
<img src="/images/HabEx/obscdf_habexe_10year.png" width="49%">

<img src="/images/HabEx/snrpdf_habexe_10year.png" width="49%">
<img src="/images/HabEx/snrcdf_habexe_10year.png" width="49%">

<img src="/images/HabEx/kpdf_habexe_10year.png" width="49%">
<img src="/images/HabEx/kcdf_habexe_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Telluric Corrections / all P-modes
Despite [my simplistic atmospheric assumptions](% post_url 2023-11-30-atmosphere %), Earth's atmosphere has many shallow lines that are difficult to correct for, especially in the infrared. To simulate (well, correct for) this, I consider an additional noise term added in quadrature with the instrument and photon noise ones. I choose values of 3 cm/s for the visible spectrograph and 115 cm/s for the NIR spectrograph, as these [follow from the literature (Wang et al 2022)](https://ui.adsabs.harvard.edu/abs/2022AJ....164..211W/abstract).

(This noise term was at least extremely easy to introduce, since we already have it split out into instrument and photon noise bits. Just another σ^2...)

<img src="/images/HabEx/kcdf_habex5_combined.png" width="49%">
<img src="/images/HabEx/kcdf_habex10_combined.png" width="49%">
<img src="/images/HabEx/kcdf_habexp_combined.png" width="49%">
<img src="/images/HabEx/kcdf_habexe_combined.png" width="49%">

<img src="/images/HabEx/kcdf_habex5_combined_ohno.png" width="49%">
<img src="/images/HabEx/kcdf_habex10_combined_ohno.png" width="49%">
<img src="/images/HabEx/kcdf_habexp_combined_ohno.png" width="49%">
<img src="/images/HabEx/kcdf_habexe_combined_ohno.png" width="49%">

<img src="/images/HabEx/kcdf_habex5_combined_log.png" width="49%">
<img src="/images/HabEx/kcdf_habex10_combined_log.png" width="49%">
<img src="/images/HabEx/kcdf_habexp_combined_log.png" width="49%">
<img src="/images/HabEx/kcdf_habexe_combined_log.png" width="49%">

CDFs of minimum detectable reflex velocity (K, in cm/s) of a planet at SNR = 10 over our telescope/instrument combinations at multiple scales. All p-mode simulations are again shown. The results with no microtellurics are shown as solid lines, while the telluric noise are the dotted lines.

<img src="/images/HabEx/snrcdf_habex5_combined.png" width="49%">
<img src="/images/HabEx/snrcdf_habex10_combined.png" width="49%">
<img src="/images/HabEx/snrcdf_habexp_combined.png" width="49%">
<img src="/images/HabEx/snrcdf_habexe_combined.png" width="49%">

<img src="/images/HabEx/snrcdf_habex5_combined_log.png" width="49%">
<img src="/images/HabEx/snrcdf_habex10_combined_log.png" width="49%">
<img src="/images/HabEx/snrcdf_habexp_combined_log.png" width="49%">
<img src="/images/HabEx/snrcdf_habexe_combined_log.png" width="49%">

CDFs of the SNR for a detection of a K = 10 cm/s planet over our telescope/instrument combinations at multiple scales. All p-mode simulations  are agan shown. The results with no microtellurics are shown as solid lines, while the telluric noise are the dotted lines.

As our assumed noise is smaller than the instrument and photon noise sources in all but the most optimistic visible surveys, microtellurics have little effect. In contrast, this noise source dominates over all others in the NIR (being far larger than the instrument or photon components, even in the most pessimistic cases), and must be better accounted for if this wavelength range is to be useful in the EPRV era.

(This is an unsurprising result given the values and how our detection heuristic works.)
