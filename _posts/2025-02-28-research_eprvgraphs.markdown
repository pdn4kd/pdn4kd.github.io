---
layout: post
title:  "EPRV Targetlist Results Graphs"
date:   2025-02-28 00:00:01 -0500
tags: research stars notes
---
Results are grouped by relevant feature. There is some redundancy in the graphs. All captions should be considered rough notes. (This is the "green prime" list, as the rest are not explored in the paper at all)

## General Feature Histograms / all P-modes
All 4 p-mode compensation methods are shown as seperate graphs here. They are ordered: fixed 5 minute, fixed 10 minute, scaled with stellar parameters (mass and radius), and scaled with stellar parameters (surface gravity and effective temperature).

# Exposure Times
<img src="/images/EPRV/exppdf_all5_eprv.png" width="49%">
<img src="/images/EPRV/exppdf_all10_eprv.png" width="49%">
<img src="/images/EPRV/exppdf_allp_eprv.png" width="49%">
<img src="/images/EPRV/exppdf_alle_eprv.png" width="49%">

Exposure times as histograms (top) and cumulative distribution functions (bottom) for every star in our telescope/instrument combinations. There is a tail of stars with very long exposure times (and which are therefore difficult to observe at high precision). The PDF appears the same for all 3 sets of stars due to the current bin size of 20 minutes, as whatever chosen p-mode correction has little effect beyond that. Due to finer bin sizes, the CDFs do show that the exact distribution of exposure times is shuffled around somewhat, though the effect is again small (and largely confined to telescope/instrument/precision combinations that skew to shorter exposure times). 

(The need to select easy stars for reasons beyond stellar activity feels worth discussing. Alongside how little difference the p-mode choice makes. Should graphs of mass/radius/p-mode timescale be added?)

<img src="/images/EPRV/expcdf_all5_eprv.png" width="49%">
<img src="/images/EPRV/expcdf_all10_eprv.png" width="49%">
<img src="/images/EPRV/expcdf_allp_eprv.png" width="49%">
<img src="/images/EPRV/expcdf_alle_eprv.png" width="49%">

(The variable p-mode for high precision raises additional issues, though. Are the short exposure stars changing substantially with required photon noise? Adding non-canonical systems also might show these effects more clearly?

# Observations
<img src="/images/EPRV/obspdf_eprv5_10year.png" width="49%">
<img src="/images/EPRV/obspdf_eprv10_10year.png" width="49%">
<img src="/images/EPRV/obspdf_eprvp_10year.png" width="49%">
<img src="/images/EPRV/obspdf_eprve_10year.png" width="49%">

Histograms of total number of observations for the different telescope/instrument combinations as both PDFs (top) and CDFs (bottom). Differences between different architectures are quite obvious, though the ones between different p-mode compensation methods are subtle (and not apparent for the architectures with longer exposure times and fewer observations).

<img src="/images/EPRV/obscdf_eprv5_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprv10_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprvp_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprve_10year.png" width="49%">

## General Feature Comparisons / All P-modes

# Exposure Times and Observations
<img src="/images/EPRV/Exposure_Time5_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Time10_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Timep_Exposure_Number_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Timee_Exposure_Number_tradeoffs3py.png" width="49%">

Total number of observations (top) and total time spent observing (bottom) for each star and telescope/instrument combination as a function of exposure time.

<img src="/images/EPRV/Exposure_Time5_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Time10_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Timep_Total_Exposure_tradeoffs3py.png" width="49%">
<img src="/images/EPRV/Exposure_Timee_Total_Exposure_tradeoffs3py.png" width="49%">

# Exposure Times and Stellar Parameters
Only effective temperature and v·sin(i) are studied, since it's expected that those matter more than eg: metallicity or log(g).

<img src="/images/EPRV/Teff_Exposure_Time5_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/Teff_Exposure_Time10_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/Teff_Exposure_Timep_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/Teff_Exposure_Timee_tradeoffs1py.png" width="49%">

Exposure time as a function of effective temperature. This target list shows a clear trend of increasing observation difficulty for hotter stars, though choice of telescope, instrument, and target precision are more important for GKM stars.

<img src="/images/EPRV/vsini_Exposure_Time5_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/vsini_Exposure_Time10_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/vsini_Exposure_Timep_tradeoffs1py.png" width="49%">
<img src="/images/EPRV/vsini_Exposure_Timee_tradeoffs1py.png" width="49%">

Exposure time as a function of rotational velocity. This target list does not show any clear trends with exposure time for desired precision vs vsini (though there may be a weak one below 2 km/s). This may be because all stars in the sample are slow rotators.

# Right Ascension and Declination
<img src="/images/EPRV/RAVsObsNum_eprv5_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsNum_eprv10_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsNum_eprvp_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsNum_eprve_lin.png" width="49%">

Total number of observations per star as a function of Right Ascension (top) and Declination (bottom). There is a clear trend in right ascension, I believe from a combination of night length and weather (though it is suppressed for longer exposure time telescope/instrument/precision combinations). That the peak corresponds with stars that have the longest time above the horizon in fall (around 270 degrees) and not winter/early spring (when the weather is better and nights longer) is surprising. (eventually: check on weather, is this accurate?)

<img src="/images/EPRV/DecVsObs_eprv5_lin.png" width="49%">
<img src="/images/EPRV/DecVsObs_eprv10_lin.png" width="49%">
<img src="/images/EPRV/DecVsObs_eprvp_lin.png" width="49%">
<img src="/images/EPRV/DecVsObs_eprve_lin.png" width="49%">

Declination does not show a clear trend, with number of observations per star being relatively flat north of about -40 degrees. Below that, stars are never observed. (This is somewhat surprising, perhaps our -30 dec cut in earlier iterations was pessimistic? At least for sites in Arizona.)

<img src="/images/EPRV/RAVsObsTime_eprv5_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsTime_eprv10_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsTime_eprvp_lin.png" width="49%">
<img src="/images/EPRV/RAVsObsTime_eprve_lin.png" width="49%">

Total observation time per star as a function of Right Ascension (top) and Declination (bottom). No clear trends are visible. (And given the lack of anything interesting along with this likely being an unimportant measure, don't expect it in the paper.)

<img src="/images/EPRV/DecVsObsTime_eprv5_lin.png" width="49%">
<img src="/images/EPRV/DecVsObsTime_eprv10_lin.png" width="49%">
<img src="/images/EPRV/DecVsObsTime_eprvp_lin.png" width="49%">
<img src="/images/EPRV/DecVsObsTime_eprve_lin.png" width="49%">

# Observation Counts and Detection Heuristic / Per P-mode 
# Fixed P-mode (5 minute) Results
<img src="/images/EPRV/obspdf_eprv5_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprv5_10year.png" width="49%">

<img src="/images/EPRV/snrpdf_eprv5_10year.png" width="49%">
<img src="/images/EPRV/snrcdf_eprv5_10year.png" width="49%">

<img src="/images/EPRV/kpdf_eprv5_10year.png" width="49%">
<img src="/images/EPRV/kcdf_eprv5_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Fixed P-mode (10 minute) Results
<img src="/images/EPRV/obspdf_eprv10_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprv10_10year.png" width="49%">

<img src="/images/EPRV/snrpdf_eprv10_10year.png" width="49%">
<img src="/images/EPRV/snrcdf_eprv10_10year.png" width="49%">

<img src="/images/EPRV/kpdf_eprv10_10year.png" width="49%">
<img src="/images/EPRV/kcdf_eprv10_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Variable P-mode (M-R) Results
<img src="/images/EPRV/obspdf_eprvp_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprvp_10year.png" width="49%">

<img src="/images/EPRV/snrpdf_eprvp_10year.png" width="49%">
<img src="/images/EPRV/snrcdf_eprvp_10year.png" width="49%">

<img src="/images/EPRV/kpdf_eprvp_10year.png" width="49%">
<img src="/images/EPRV/kcdf_eprvp_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Variable P-mode (g-T) Results
<img src="/images/EPRV/obspdf_eprve_10year.png" width="49%">
<img src="/images/EPRV/obscdf_eprve_10year.png" width="49%">

<img src="/images/EPRV/snrpdf_eprve_10year.png" width="49%">
<img src="/images/EPRV/snrcdf_eprve_10year.png" width="49%">

<img src="/images/EPRV/kpdf_eprve_10year.png" width="49%">
<img src="/images/EPRV/kcdf_eprve_10year.png" width="49%">

Histograms/PDFs (left) and CDFs (right) of the number of observations (top), SNR of a nominal 10 cm/s planet detection (middle), and minimum detectable reflex velocity k of a nominal SNR = 10 planet detection (bottom).

# Telluric Corrections / all P-modes
Despite the atmospheric assumptions earlier in the paper, Earth's atmosphere has many shallow lines that are difficult to correct for, especially in the infrared. To simulate this, I consider an additional noise term added in quadrature with the instrument and photon noise ones. I choose values of 3 cm/s for the visible spectrograph and 115 cm/s for the NIR spectrograph, as these [follow from the literature (Wang et al 2022)](https://ui.adsabs.harvard.edu/abs/2022AJ....164..211W/abstract).

(This noise term was at least extremely easy to introduce, since we already have it split out into instrument and photon noise bits. Just another σ^2...)

<img src="/images/EPRV/kcdf_eprv5_combined.png" width="49%">
<img src="/images/EPRV/kcdf_eprv10_combined.png" width="49%">
<img src="/images/EPRV/kcdf_eprvp_combined.png" width="49%">
<img src="/images/EPRV/kcdf_eprve_combined.png" width="49%">

<img src="/images/EPRV/kcdf_eprv5_combined_ohno.png" width="49%">
<img src="/images/EPRV/kcdf_eprv10_combined_ohno.png" width="49%">
<img src="/images/EPRV/kcdf_eprvp_combined_ohno.png" width="49%">
<img src="/images/EPRV/kcdf_eprve_combined_ohno.png" width="49%">

<img src="/images/EPRV/kcdf_eprv5_combined_log.png" width="49%">
<img src="/images/EPRV/kcdf_eprv10_combined_log.png" width="49%">
<img src="/images/EPRV/kcdf_eprvp_combined_log.png" width="49%">
<img src="/images/EPRV/kcdf_eprve_combined_log.png" width="49%">

CDFs of minimum detectable reflex velocity (K, in cm/s) of a planet at SNR = 10 over our telescope/instrument combinations at multiple scales. All p-mode simulations are again shown. The results with no microtellurics are shown as solid lines, while the telluric noise are the dotted lines.

<img src="/images/EPRV/snrcdf_eprv5_combined.png" width="49%">
<img src="/images/EPRV/snrcdf_eprv10_combined.png" width="49%">
<img src="/images/EPRV/snrcdf_eprvp_combined.png" width="49%">
<img src="/images/EPRV/snrcdf_eprve_combined.png" width="49%">

<img src="/images/EPRV/snrcdf_eprv5_combined_log.png" width="49%">
<img src="/images/EPRV/snrcdf_eprv10_combined_log.png" width="49%">
<img src="/images/EPRV/snrcdf_eprvp_combined_log.png" width="49%">
<img src="/images/EPRV/snrcdf_eprve_combined_log.png" width="49%">

CDFs of the SNR for a detection of a K = 10 cm/s planet over our telescope/instrument combinations at multiple scales. All p-mode simulations are again shown. The results with no microtellurics are shown as solid lines, while the telluric noise are the dotted lines.

As our assumed noise is smaller than the instrument and photon noise sources in all but the most optimistic visible surveys, microtellurics have little effect. In contrast, this noise source dominates over all others in the NIR (being far larger than the instrument or photon components, even in the most pessimistic cases), and must be better accounted for if this wavelength range is to be useful in the EPRV era.

(This is an unsurprising result given the values and how our detection heuristic works.)
