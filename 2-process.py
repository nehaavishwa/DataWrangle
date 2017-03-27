#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = r"/home/nehaavishwa/PycharmProjects/DataWrangle/Files/data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """This is example of the data structure you should return.
    Each item in the list should be a dictionary containing all the relevant data
    from each row in each file. Note - year, month, and the flight data should be 
    integers. You should skip the rows that contain the TOTAL data for a year
    data = [{"courier": "FL",
            "airport": "ATL",
            "year": 2012,
            "month": 12,
            "flights": {"domestic": 100,
                        "international": 100}
            },
            {"courier": "..."}
    ]
    """
    data = []
    info = {}
    with open(f, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(open(f))
        #print(soup.find_all("option"))
        ops = soup.find_all('option')
        tbl = soup.find('tr', attrs={'class':'libraryTHY2_Center'}) #soup.a #title #table['class']
        #print(tbl.find_all('td'))
        for t in tbl:
            l = len(t)-6
            print(str(t)[4:l])
        #td = tbl.find('td')
        #print(td)
        for option in ops:
            #print(option['value'])
            if(len(option['value'])==2):
                info['courier']=option['value']
            if(len(option['value'])==3):
                info['airport']=option['value']

        print(info)
        data.append(info)
        print(data)
    # info["courier"], info["airport"] = f[:6].split("-")
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    '''with open("{}/{}".format(datadir, f), "r") as html:
        soup = BeautifulSoup(open(html))'''

    return data


def test():
    print("Running a simple test...")
    #open_zip(datadir)
    files = process_all(datadir)
    data = []
    for f in files:
        f=datadir+"/"+f
        #print(f)
        data += process_file(f)

    '''
    assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print("... success!")
    '''

if __name__ == "__main__":
    test()