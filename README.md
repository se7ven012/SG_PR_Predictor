# SG_PR_Predictor

Singapore PR application predictor

## Data

Application data is obtained from [here](http://sgprapp.com/listPage?&page=0)  
For each applicant, the data is categorized into 11 attributes

* year_of_stay   (Years of applicant stay in Singapore)
* is_local_uni   (Applicant is graduated from a local university)
* is_local_poly  (Applicant is graduated from a local polytechnic)
* is_diploma     (Applicant has a Polytechnic Diploma)
* is_bachelor    (Applicant has a Bachelor Degree)
* is_master      (Applicant has a Master Degree)
* is_phd         (Applicant has a PhD)
* is_malaysian   (Applicant is Malaysian)
* is_couple      (Applicant applied with his/her wife/husband)
* with_child     (Applicant applied with his/her child/children)
* is_ep          (Applicant holding an employment pass)

## Quick Start

1. Download python orange3 from [here](https://github.com/biolab/orange3)
2. Run orange3 and import [pr.ows](SG_PR_Predictor/pr.ows)
3. Prepare your own prediction data and make it as test data
4. Run prediction in orange3
