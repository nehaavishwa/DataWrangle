__author__ = 'nvishwakarma'

import os
import pprint
import csv

DATADIR = ""
DATAFILE = r"C:\Users\nVishwakarma\Documents\Python\beatles-diskography.csv"


def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, "rt") as file:
        r = csv.DictReader(file)
        for line in r:

            data.append(line)
    return data


if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    print(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)
