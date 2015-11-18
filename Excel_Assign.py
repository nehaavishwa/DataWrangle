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
    with ZipFile('{0}'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    #data = None
    maxval_coast = max(sheet.col_values(1, 1, sheet.nrows))
    maxpos_coast = sheet.col_values(1,1, sheet.nrows-1).index(maxval_coast) + 1
    maxtime_coast = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_coast,0),0)
    tup_coast = (maxtime_coast)
    max_YEAR_coast = tup_coast[0]
    max_MONTH_coast = tup_coast[1]
    max_DAY_coast = tup_coast[2]
    max_HOUR_coast = tup_coast[3]
    #print(maxval_coast)
    maxval_EAST = max(sheet.col_values(2, 1, sheet.nrows))
    maxpos_EAST = sheet.col_values(2, 1, sheet.nrows-1).index(maxval_EAST) + 1
    maxtime_EAST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_EAST, 0), 0)
    tup_EAST = (maxtime_EAST)
    max_YEAR_EAST = tup_EAST[0]
    max_MONTH_EAST = tup_EAST[1]
    max_DAY_EAST = tup_EAST[2]
    max_HOUR_EAST = tup_EAST[3]
    #print(maxval_EAST)
    tup_Far_West = ()
    maxval_FAR_WEST = max(sheet.col_values(3, 1, sheet.nrows))
    maxpos_FAR_WEST = sheet.col_values(3, 1, sheet.nrows-1).index(maxval_FAR_WEST) + 1
    maxtime_FAR_WEST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_FAR_WEST, 0), 0)
    tup_Far_West = (maxtime_FAR_WEST)
    max_YEAR_FAR_WEST = tup_Far_West[0]
    max_MONTH_FAR_WEST = tup_Far_West[1]
    max_DAY_FAR_WEST = tup_Far_West[2]
    max_HOUR_FAR_WEST = tup_Far_West[3]
    #print(tup_Far_West[0])
    #print(maxval_FAR_WEST)
    maxval_NORTH = max(sheet.col_values(4, 1, sheet.nrows))
    maxpos_NORTH = sheet.col_values(4, 1, sheet.nrows-1).index(maxval_NORTH) + 1
    maxtime_NORTH = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_NORTH, 0), 0)
    tup_NORTH = (maxtime_NORTH)
    max_YEAR_NORTH = tup_NORTH[0]
    max_MONTH_NORTH = tup_NORTH[1]
    max_DAY_NORTH = tup_NORTH[2]
    max_HOUR_NORTH = tup_NORTH[3]
    #print(maxval_NORTH)
    maxval_NORTH_C = max(sheet.col_values(5, 1, sheet.nrows))
    maxpos_NORTH_C = sheet.col_values(5, 1, sheet.nrows-1).index(maxval_NORTH_C) + 1
    maxtime_NORTH_C = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_NORTH_C, 0), 0)
    tup_NORTH_C  = (maxtime_NORTH_C)
    max_YEAR_NORTH_C = tup_NORTH_C[0]
    max_MONTH_NORTH_C = tup_NORTH_C[1]
    max_DAY_NORTH_C = tup_NORTH_C[2]
    max_HOUR_NORTH_C = tup_NORTH_C[3]
    #print(maxval_NORTH_C)
    maxval_SOUTHERN = max(sheet.col_values(6, 1, sheet.nrows))
    maxpos_SOUTHERN = sheet.col_values(6, 1, sheet.nrows-1).index(maxval_SOUTHERN) + 1
    maxtime_SOUTHERN = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_SOUTHERN, 0), 0)
    tup_SOUTHERN  = (maxtime_SOUTHERN)
    max_YEAR_SOUTHERN = tup_SOUTHERN[0]
    max_MONTH_SOUTHERN = tup_SOUTHERN[1]
    max_DAY_SOUTHERN = tup_SOUTHERN[2]
    max_HOUR_SOUTHERN = tup_SOUTHERN[3]
    #print(maxval_SOUTHERN)
    maxval_SOUTH_C = max(sheet.col_values(7, 1, sheet.nrows))
    maxpos_SOUTH_C = sheet.col_values(7, 1, sheet.nrows-1).index(maxval_SOUTH_C) + 1
    maxtime_SOUTH_C = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_SOUTH_C, 0), 0)
    tup_SOUTH_C  = (maxtime_SOUTH_C)
    max_YEAR_SOUTH_C = tup_SOUTH_C[0]
    max_MONTH_SOUTH_C = tup_SOUTH_C[1]
    max_DAY_SOUTH_C = tup_SOUTH_C[2]
    max_HOUR_SOUTH_C = tup_SOUTH_C[3]
    #print(maxval_SOUTH_C)
    maxval_WEST = max(sheet.col_values(8, 1, sheet.nrows))
    maxpos_WEST = sheet.col_values(8, 1, sheet.nrows-1).index(maxval_WEST) + 1
    maxtime_WEST = xlrd.xldate_as_tuple(sheet.cell_value(maxpos_WEST, 0), 0)
    tup_WEST  = (maxtime_WEST)
    max_YEAR_WEST  = tup_WEST[0]
    max_MONTH_WEST  = tup_WEST[1]
    max_DAY_WEST  = tup_WEST[2]
    max_HOUR_WEST = tup_WEST[3]

    #print(maxtime_COAST)
    # YOUR CODE HERE
    data = {'COAST': {'Max Load': maxval_coast, 'Year': max_YEAR_coast, 'Month': max_MONTH_coast, 'Day': max_DAY_coast, 'Hour': max_HOUR_coast},
             'EAST': {'Max Load': maxval_EAST, 'Year': max_YEAR_EAST, 'Month': max_MONTH_EAST, 'Day': max_DAY_EAST, 'Hour': max_HOUR_EAST},
             'FAR_WEST': {'Max Load': maxval_FAR_WEST, 'Year': max_YEAR_FAR_WEST, 'Month': max_MONTH_FAR_WEST, 'Day': max_DAY_FAR_WEST, 'Hour': max_HOUR_FAR_WEST},
             'NORTH': {'Max Load': maxval_NORTH, 'Year': max_YEAR_NORTH, 'Month': max_MONTH_NORTH, 'Day': max_DAY_NORTH, 'Hour': max_HOUR_NORTH},
             'NORTH_C': {'Max Load': maxval_NORTH_C, 'Year': max_YEAR_NORTH_C, 'Month': max_MONTH_NORTH_C, 'Day': max_DAY_NORTH_C, 'Hour': max_HOUR_NORTH_C},
             'SOUTHERN': {'Max Load': maxval_SOUTHERN, 'Year': max_YEAR_SOUTHERN, 'Month': max_MONTH_SOUTHERN, 'Day': max_DAY_SOUTHERN, 'Hour': max_HOUR_SOUTHERN},
             'SOUTH_C': {'Max Load': maxval_SOUTH_C, 'Year': max_YEAR_SOUTH_C, 'Month': max_MONTH_SOUTH_C, 'Day': max_DAY_SOUTH_C, 'Hour': max_HOUR_SOUTH_C},
             'WEST': {'Max Load': maxval_WEST, 'Year': max_YEAR_WEST, 'Month': max_MONTH_WEST, 'Day': max_DAY_WEST, 'Hour': max_HOUR_WEST}
            }
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data


def save_file(data, filename):
    # YOUR CODE HERE

    with open(filename, 'w') as csvfile:
        fieldnames = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
        writer = csv.DictWriter(csvfile, delimiter='|', fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            print(d, data[d], data[d]['Hour'])
            writer.writerow({'Station': d, 'Year': data[d]['Year'], 'Month': data[d]['Month'], 'Day': data[d]['Day'], 'Hour': data[d]['Hour'], 'Max Load': data[d]['Max Load']})





    
def test():
    #open_zip(datafile)
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
            print(line)
            station = line['Station']
            print(station)
            if station == 'FAR_WEST':
                print(station)
                for field in fields:
                    print(field)
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        print("STATION FIELD",station, field, ans[station][field], "LINE FIELD", line[field])
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        print(number_of_rows)
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()
    #data = parse_file(datafile)
    #save_file(data, outfile)

