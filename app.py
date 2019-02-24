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
import csv

class App:
    source = ""
    def __init__(self):
        x = []
        y = []
        self.read_csv()
        # sketch()


    def read_csv(self): #read csv
        with open('csv_files/measurement1.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    #print(f'\t time:{row[0]}  Lcap: {row[1]} Ldeg: {row[2]}.')
                    line_count += 1
            #print(f'Processed {line_count} lines.')



    # def sketch(self): #sketch csv





if __name__ == '__main__':
    App()