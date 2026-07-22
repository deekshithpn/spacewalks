# Spacewalks

## Overview

Space walks is a python analyusis tool for researchers to generate visulaizations and statistical summaries of NASA;s exztra vehicular activity datasets.

## Features

Key features of Spacewalks:

- Generates a CSV table of summary statistics of extrea vehicular activity crew sizes.
- Generates a litne plot to show cumulative duration of space walks over time.

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation 

## Installation Instuctions

Follow the following steps for installation.

1. Clone the spacewalks repo to your local machine using git. If you don't have Git installed u can download it drom official Git wwebsite.
'''
git clone git@github.com:deekshithpn/spacewalks.git
cd spacewalks
'''
2. Install the necessary dependencies.
```
python3 -m pip install -r requirements.txt
``` 
## Usage Example

To run an analysis using the eva_data_analysis.py script from the command line terminal,
launch the script using Python as follows:

python3 eva_data_analysis.py eva-data.json eva-data.csv

The first argument is path to the JSON data file.
The second argument is the path the CSV output file.


