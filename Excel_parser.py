__author__ = 'nvishwakarma'

import xlrd

datafile = r"C:\Temp\2015_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)]
                                       for r in range(sheet.nrows)]

    print("\nList Comprehension")
    print("data[3][2]")
    print(data[3][2])

    print("\nCell in a Nested Loop:")
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print(sheet.cell_value(row, col))

    print("\nRows, Columns, and CELLS:")
    print("Number of rows in the sheet:")
    print(sheet.nrows)
    print(sheet.ncols)
    print(sheet.cell_type(1, 2))
    print(sheet.cell_value(1, 2))
#1 : Text
#2: Number
#3: Date
    print(sheet.col_values(3, 0, 4))

    print("\nDates:")
    print("Type of data in cell (row 1, col 0):")
    excel_date = sheet.cell_value(2, 0)
    print(excel_date)
    print(xlrd.xldate_as_tuple(excel_date, 0))
    '''
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }'''
    return data


data = parse_file(datafile)
#print(data)

