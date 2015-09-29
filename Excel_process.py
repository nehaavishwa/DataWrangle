#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = r"C:\Temp\2015_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    

    
    ### example on how you can get the data
    minval = min(sheet.col_values(1,1,sheet.nrows))
    maxval = max(sheet.col_values(1,1,sheet.nrows))
    avg = (sum(sheet.col_values(1,1,sheet.nrows))/(sheet.nrows-1))
    
    #print minval
    minpos = sheet.col_values(1,1, sheet.nrows-1).index(minval) + 1
    #print minpos
    #print maxval
    maxpos = sheet.col_values(1,1, sheet.nrows-1).index(maxval) + 1
    #print maxpos
    
    maxtime = xlrd.xldate_as_tuple(sheet.cell_value(maxpos,0),0)
    mintime = xlrd.xldate_as_tuple(sheet.cell_value(minpos,0),0)
    print(maxtime)
    #print mintime
    
        
    '''sheet_data = [sheet.cell_value(r, c) for r in range(1, sheet.nrows)
                                          for c in range(0, 1)]
    minval = min(sheet_data)
    maxval = max(sheet_data)
    print(sheet_data.col_values(1,1,100))'''
    #print(maxval)
    
    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': maxtime,
            'maxvalue': maxval,
            'mintime': mintime,
            'minvalue': minval,
            'avgcoast': avg
    }
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2015, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

data = parse_file(datafile)
print('\n')
print(data)
#test()