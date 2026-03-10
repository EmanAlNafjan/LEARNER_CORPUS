# KSAUHS Learner Corpus
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18941931.svg)](https://doi.org/10.5281/zenodo.18941931)
![Corpus](https://img.shields.io/badge/type-learner%20corpus-blue)
![Language](https://img.shields.io/badge/language-English-green)
![Context](https://img.shields.io/badge/context-academic%20writing-orange)
![License](https://img.shields.io/badge/license-CC--BY--NC%204.0-lightgrey)

## Overview

The **KSAUHS Learner Corpus** is a longitudinal corpus of English academic writing produced by first-year students enrolled in the **Pre-Professional Program (PPP)** at **King Saud bin Abdulaziz University for Health Sciences (KSAUHS)** in Saudi Arabia.

The corpus documents student writing produced during the preparatory year prior to entry into health science programs such as medicine, dentistry, pharmacology, nursing, and applied medical sciences. The dataset captures authentic learner language produced as part of regular coursework and invigilated examinations in an intensive English-medium academic environment.

The corpus was compiled to support research in:

- learner corpus research  
- second language acquisition  
- academic writing development  
- corpus-based pedagogy and data-driven learning  
- corpus linguistics and educational NLP

---

## Corpus Composition

The corpus contains writing produced by **157 students** enrolled in the preparatory program.

Data collection began with an initial cohort of over **500 first-year students**, of whom **202 provided informed consent** to participate in the study. Due to missing or incomplete submissions within the institutional learning management system, **157 students were retained for inclusion in the corpus**.

Each included student contributed:

- two handwritten invigilated exams  
- multiple coursework writing assignments  
- draft and final versions for some assignments

Texts were collected across **four academic trimesters**, allowing the corpus to capture **longitudinal development in learner writing**.

---

## Corpus Structure

The repository contains the following primary files and folders.

### Dataset

`KSAUHS_Learner_Corpus.xlsx`

This file contains the structured corpus dataset.

Each row represents **one anonymized learner** identified by a five-digit learner ID.

Columns include:

#### Learner metadata

- learner ID  
- academic major (final program placement)  
- age  
- parental first languages  
- languages spoken at home  
- schooling background  
- years of English instruction  
- prior stay in English-speaking countries  
- reference tool use (dictionaries and grammar resources)

#### Writing submissions

Student texts are arranged **chronologically according to trimester and assignment order**.

---

## Task Identification System

Writing tasks follow a structured numbering convention:
Example: 3.2.2
Meaning:

- **3** → third trimester  
- **2** → second assignment in that trimester  
- **2** → final version  

Version codes:

- **1 = draft**
- **2 = final submission**

This system allows researchers to track **revision processes and longitudinal writing development**.

---

## Annotation

All texts were manually processed and annotated.

The annotation workflow included:

- transcription of handwritten exam scripts into digital text  
- conversion of Word and PDF submissions into plain text  
- structural tagging using XML-style markup

#### Examples of tags include:

<title>Mobile use in class</title> 

<in_text_reference>in-text reference</in_text_reference> 

<reference_list> list of references</reference_list> 

First and <original=foremast>foremost</original> , mental health 

## Ethical Considerations

The collection of participants’ written production and metadata was approved by the Institutional Review Board (IRB) of:

King Abdullah International Medical Research Center (KAIMRC)
Ministry of National Guard – Health Affairs
Kingdom of Saudi Arabia

IRB Approval Number: IRB/1344/22
Study Number: NRC22R/312/06

All participants provided informed consent prior to inclusion in the study. All data released in this repository have been fully anonymized.


## Data Disclaimer

All texts have been anonymized to remove personally identifiable information. While every effort was made to ensure accuracy during transcription and annotation, minor inconsistencies may remain due to the manual nature of the corpus compilation process.

## Interactive Corpus Interface

An interactive interface for exploring the corpus is available online:

https://ksauhs-learner-corpus.streamlit.app/

The Streamlit application allows users to:

- browse learner texts
- inspect learner metadata
- perform basic concordance searches
- explore corpus content interactively

The interface is designed for exploratory access to the corpus, while the full dataset remains available in this repository for independent analysis.

## Citation

If you use the KSAUHS Learner Corpus in your research, please cite the dataset:

AlNafjan, E., Alfelaij, A., Alfawaz, N., et al. (2026).  
**KSAUHS Learner Corpus (Version 1.0)**. Zenodo.  
https://doi.org/10.5281/zenodo.18941931

### Associated manuscript

AlNafjan, E., Alfelaij, A., Alfawaz, N., et al. (under review).  
*The KSAUHS Learner Corpus: A longitudinal resource on Arabic L1 EFL academic writing.*
