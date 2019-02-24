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
    # Csv file content:
    # Time, L:Measurement, L:ConvertedCap, L:Angle, R:Measurement, R:ConvertedCap, R:Angle
    time_values = []
    row_L_measurement = []
    row_L_angle = []
    row_R_measurement = []
    row_R_angle = []

    def __init__(self):
        self.read_all_csv()


    def read_all_csv(self):
        input_val = input("How many files do you want to read? ")
        i = 1
        while i <= int(input_val):
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
                    self.time_values.append(row[0])
                    self.row_L_measurement.append(row[1])

                    line_count += 1
            print(f'Processed {line_count} lines.')

            print("The file will be sketched.")
            self.sketch()



    def sketch(self):  # sketch csv

        #results = sm.OLS(self.row_1, sm.add_constant(self.time_values)).fit()

        #print("X size:", len(self.row[0]), "Y size:", len(self.row[1]))

        plt.scatter(self.time_values, self.row_L_measurement)
        plt.xlabel('Time')
        plt.ylabel('Measurements')
        plt.show()



if __name__ == '__main__':
    App()