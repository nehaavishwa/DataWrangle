# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = r"C:\Users\nVishwakarma\Documents\Python\beatles-diskography.csv"
datafile = os.path.join(DATADIR, DATAFILE)




def parse_file_test(datafile):
    data = []


    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        for h in enumerate(header):
            print("Header" + h)



        '''for i, line in enumerate(f):
            #print(line)
            if (i == 0):
                (key) = line.split(',')
                #print(key.strip(''))
            if (i > 0 and i <= 10):
                for x in range(0, len(key)):
                    (val) = line.split(',')
                    mydict = {key[x]: val[x] for key1 in key}
                    print(mydict)

                data.append(mydict)'''
        data.append(h)
    return data


def parse_file(datafile):
    data = []

    with open(datafile, "r") as f:
            header = f.readline().split(",")
            counter = 0
            for line in f:
                if counter == 10:
                    break

                fields = line.split(",")
                entry = {}
                for i, val in enumerate(fields):
                    entry[header[i].strip()] = val.strip()

                data.append(entry)
                counter += 1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


d = parse_file(datafile)
print(d)
#parse_file(datafile)
#test()