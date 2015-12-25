__author__ = 'nehaavishwa'

import os
filename = r'/home/nehaavishwa/PycharmProjects/DataWrangle/Diskography.csv'
data=[]

def parse_file(filename):

    with open(filename, 'r') as f:
        header = f.readline().split(",")
        for h in header:
            print(h)
            data.append(h)
        #print(header)# header

    return data


a = parse_file(filename)
print(a)

#Things to prepare
#phone technical what to expect


