## Computerized Analytics and Hockey, What Could Go Wrong?

Having COVID-19 sucks, but luckily hockey keeps me entertained and so does programming. I built a minor predictive analytics tool that follows input from a `.csv` file about the [Vegas Golden Knights](https://www.nhl.com/goldenknights), for the 2017-2019 seasons. Unfortunately I'm not good at keeping up with publishing code, so this is a few months late.

## vgk_analytics.py

This tool is the first iteration I built of a python script that pulls Win/Loss/Overtime Loss("OTL") data from `.csv` and uses 3-by-3 matrices to complete simple predictions with Markov Chains. I will use this to build a better script that can track any team's record and predict an upcoming regular season(pending no new plagues or disasters).
