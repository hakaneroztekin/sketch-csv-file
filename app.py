# Read and Sketch .csv Files
# 24 Feb 2019
#
# Implementation Plan
# Read csv files (the requested columns) into arrays
# Sketch the csv files.
# Beautify the graph if needed.

import re
from contextlib import closing

import matplotlib.pyplot as plt
import statsmodels.api as sm
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException

