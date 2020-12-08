## A Recurring Reproduction Error in the Administration of the Generalized Anxiety Disorder Scale

This repository contains the materials associated with Zorowitz et al. (2020), _A Recurring Reproduction Error in the Administration of the Generalized Anxiety Disorder Scale_.

Please see the remainder of this README file for details on the literature reviews conducted as part of this letter.

### Project Organization

    ├── annotated                                <- Annotated lists of publications using the GAD-7.
    │   ├── psychinfo_results_annotated.tsv      <- Annotated list of publications from the APA PsycInfo database.
    │   ├── scholar_results_annotated.tsv        <- Annotated list of publications from the Google Scholar database.
    |
    ├── raw                                      <- Unannotated lists of publications using the GAD-7.
    │   ├── psychinfo_results_annotated.tsv      <- Original list of publications from the APA PsycInfo database.
    │   ├── scholar_results_annotated.tsv        <- Original list of publications from the Google Scholar database.
    │   
    ├── scripts                                  <- Code used to perform literature reviews.
    │   ├── search_scholar.py                    <- Script used to pull citations from Google Scholar.
    │   
    ├── requirements.txt                         <- Python packages required by this project.

### Literature Review - Google Scholar

The authors used Google Scholar to identify published articles and theses that included the reproduction error. Google Scholar was necessary as (to our knowledge) it is the only academic literature database that performs full text search of the body of a publication.

An initial list of articles were found on Google Scholar using various permutations of the search query "gad-7" + "not at all sure". The search was performed using the [`scholarly`](https://github.com/scholarly-python-package/scholarly) package in python. Full details of the search methods can be found in [`search_scholar.py`](scripts/search_scholar.py). The unannotated list of results returned by this search can be found in [scholar_results_raw.tsv](raw/scholar_results_raw.tsv).

Each publication was then manually inspected to confirm that the authors had reported making the reproduction error (i.e. using "not at all sure" instead of "not at all" when administering the GAD-7). These inspections were performed to prevent false positives (e.g. authors administered GAD-7, but the phase "not at all sure" appeared elsewhere in the publication). Two coders, Sam Zorowitz (sz) and Gina Choe (gc), performed the inspections.

The resulting annotated list of publications can be found in [scholar_results_annotated.tsv](annotated/scholar_results_annotated.tsv). The variable `error` indicates if the corresponding publication made the error (Yes = 1, No = 0). The variable `language` indicates the language that the GAD-7 was administered in.

## Literature Review - APA PsychInfo

The authors used APA PsychInfo to perform a secondary review in order to measure the fraction of recently published articles that report the anchors of the GAD-7 (i.e. "not at all", "several days", etc). This review was performed in order to quantify the risk of underestimating the reproduction error in the literature. That is, if the norm is to not to report the response anchors used when administering the GAD-7, then it is likely that the number of publications identified having made the error is an underestimate of the total number of studies having made the error.

An initial list of 121 recent publications having used the GAD-7 was identified on APA PsychInfo using the following search criteria:

- Search terms (s1): gad-7
- Limiters - Peer Reviewed; English; Exclude Dissertations; Publication Year: 2018-2020
- Expanders - Apply equivalent subjects
- Narrow by Tests: - generalized anxiety disorder 7
- Narrow by Methodology: - empirical study
- Search modes - Find all my search terms

The unannotated list of publications can be found in [psychinfo_results_raw.csv](raw/psychinfo_results_raw.csv).

Each publication was then manually inspected to confirm whether the authors reported the response anchors used when administering the GAD-7. One coder, Sam Zorowitz (sz), performed the inspections.

The resulting annotated list of publications can be found in [psychinfo_results_annotated.tsv](annotated/psychinfo_results_annotated.tsv). The variable `Anchors` indicates if the corresponding publication reported the anchors (Yes = 1, No = 0). 
