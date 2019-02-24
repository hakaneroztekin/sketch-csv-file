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
from matplotlib.pyplot import figure
import numpy as np

class App:
    # Csv file content:
    # Time, L:Measurement, L:ConvertedCap, L:Angle, R:Measurement, R:ConvertedCap, R:Angle
    time_values = []
    row_L_measurement = []
    row_L_angle = []
    row_R_measurement = []
    row_R_angle = []
    file_count = 0

    def __init__(self):
        self.file_count = int(input("How many files do you want to read? "))
        self.read_all_csv()


    def read_all_csv(self):
        i = 1
        while i <= self.file_count:
            self.read_csv(i)
            i += 1
            print("All files are read")

    def read_csv(self, i):  # read csv
        zero_time = 0 # the starting time value; will be used to normalize the time values
        source = "csv_files"
        file_name = "measurement" + str(i) + ".csv"
        full_address = source + "/" + file_name

        with open(full_address) as csv_file:
            print("Reading file: " + file_name)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    zero_time = float(row[0])
                #print(f'\t time:{row[0]}  Lcap: {row[1]} Ldeg: {row[2]}.')
                self.time_values.append(float(row[0]) - zero_time)  # normalize the time values
                self.row_L_measurement.append(float(row[1]))
                self.row_L_angle.append(float(row[3]))
                self.row_R_measurement.append(float(row[4]))
                self.row_R_angle.append(float(row[6]))
                line_count += 1
            print(f'Processed {line_count} lines.')

            print("The file will be sketched.")
            self.sketch()



    def sketch(self):  # sketch csv
        print("Plot Initialized")
        index = 1
        figure(num=None, figsize=(32, 16), dpi=1024, facecolor='w', edgecolor='k')
        #max_value = int(max(self.row_L_measurement))
        #min_value = int(min(self.row_L_measurement))
        #print("min: " + str(min_value) + " max: " + str(max_value))

        plt.plot(self.time_values, self.row_L_measurement, 'r')
        plt.plot(self.time_values, self.row_R_measurement, 'b')

        #plt.ylim(400, 600)

        plt.xlabel("Time(ms)")
        plt.ylabel("Measurements")
        plot_name = str(index) + "-measurement.png"
        plt.savefig(plot_name)
        print(plot_name + " is saved")





if __name__ == '__main__':
    App()