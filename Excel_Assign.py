# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = r"C:\Temp\2013_ERCOT_Hourly_Load_Data.xls"
outfile = r"C:\Temp\2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    #data = None
    maxval_coast = max(sheet.col_values(1, 1, sheet.nrows))
    maxpos_coast = sheet.col_values(1,1, sheet.nrows-1).index(maxval_coast) + 1
    maxtime_COAST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_coast,0),0)
    #print(maxval_coast)
    maxval_EAST = max(sheet.col_values(2, 1, sheet.nrows))
    maxpos_EAST = sheet.col_values(2, 1, sheet.nrows-1).index(maxval_EAST) + 1
    maxtime_EAST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_EAST, 0), 0)
    #print(maxval_EAST)
    maxval_FAR_WEST = max(sheet.col_values(3, 1, sheet.nrows))
    maxpos_FAR_WEST = sheet.col_values(3, 1, sheet.nrows-1).index(maxval_FAR_WEST) + 1
    maxtime_FAR_WEST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_FAR_WEST, 0), 0)
    #print(maxval_FAR_WEST)
    maxval_NORTH = max(sheet.col_values(4, 1, sheet.nrows))
    maxpos_NORTH = sheet.col_values(4, 1, sheet.nrows-1).index(maxval_NORTH) + 1
    maxtime_NORTH = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_NORTH, 0), 0)
    #print(maxval_NORTH)
    maxval_NORTH_C = max(sheet.col_values(5, 1, sheet.nrows))
    maxpos_NORTH_C = sheet.col_values(5, 1, sheet.nrows-1).index(maxval_NORTH_C) + 1
    maxtime_NORTH_C = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_NORTH_C, 0), 0)
    #print(maxval_NORTH_C)
    maxval_SOUTHERN = max(sheet.col_values(6, 1, sheet.nrows))
    maxpos_SOUTHERN = sheet.col_values(6, 1, sheet.nrows-1).index(maxval_SOUTHERN) + 1
    maxtime_SOUTHERN = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_SOUTHERN, 0), 0)
    #print(maxval_SOUTHERN)
    maxval_SOUTH_C = max(sheet.col_values(7, 1, sheet.nrows))
    maxpos_SOUTH_C = sheet.col_values(7, 1, sheet.nrows-1).index(maxval_SOUTH_C) + 1
    maxtime_SOUTH_C = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_SOUTH_C, 0), 0)
    #print(maxval_SOUTH_C)
    maxval_West = max(sheet.col_values(8, 1, sheet.nrows))
    maxpos_WEST = sheet.col_values(8, 1, sheet.nrows-1).index(maxval_West) + 1
    maxtime_WEST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_WEST, 0), 0)


    #print(maxtime_COAST)
    # YOUR CODE HERE
    data = {'COAST': {'Max Load': maxval_coast, 'Time': maxtime_COAST},
             'EAST': {'Max Load': maxval_EAST, 'Time': maxtime_EAST},
             'FAR_WEST': {'Max Load': maxval_FAR_WEST, 'Time': maxtime_FAR_WEST},
             'NORTH': {'Max Load': maxval_NORTH, 'Time':maxtime_NORTH},
             'NORTH_C': {'Max Load': maxval_NORTH_C, 'Time': maxtime_NORTH_C},
             'SOUTHERN': {'Max Load': maxval_SOUTHERN,'Time': maxtime_SOUTHERN},
             'SOUTH_C': {'Max Load': maxval_SOUTH_C, 'Time': maxtime_SOUTH_C},
             'West': {'Max Load': maxval_West, 'Time': maxtime_WEST}
            }
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data


def save_file(data, filename):
    # YOUR CODE HERE
    print(data)

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    #test()
    data = parse_file(datafile)
    save_file(data, outfile)

