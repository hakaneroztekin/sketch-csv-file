# Read and Sketch .csv Files
# 24 Feb 2019
#
# Implementation Plan
# Read csv files (the requested columns) into lists
# Sketch the csv files.
# Beautify the graph if needed.

# The current csv data characteristics:
# The files contain sensor measurements
# Each column has its specific meaning
# So, csv reading will be specialized for that aim
# Though, csv reader can be modified for different type of csv files.

import re
from contextlib import closing
import matplotlib.pyplot as plt
import statsmodels.api as sm
from bs4 import BeautifulSoup
import csv

class App:
    row = []

    def __init__(self):
        # Csv file content:
        # Time, L:Measurement, L:ConvertedCap, L:Angle, R:Measurement, R:ConvertedCap, R:Angle

        self.read_all_csv()
        # sketch()

    def read_all_csv(self):
        input_val = input("How many files do you want to read? ")
        i = 1
        while i < int(input_val):
            self.read_csv(i)
            i += 1
            print("All files are read")

    def read_csv(self, i):  # read csv
        source = "csv_files"
        file_name = "measurement" + str(i) + ".csv"
        full_address = source + "/" + file_name

        with open(full_address) as csv_file:
            print("Reading file: " + file_name)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                    #print(f'\t time:{row[0]}  Lcap: {row[1]} Ldeg: {row[2]}.')
                    self.row.append(row)
                    line_count += 1
            print(f'Processed {line_count} lines.')

            print("The file will be sketched.")



    # def sketch(self):  # sketch csv





if __name__ == '__main__':
    App()