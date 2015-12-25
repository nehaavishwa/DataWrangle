__author__ = 'nehaavishwa'

a =[1, [2, [3, [4, [5, 6], 7], 8]]]
b =[1, 0, 2]
x = []


def flatA(a):
    if len(a)>1:
        x.append(a[0])
    return x

def flt(a):
    if not (isinstance(a, list)):
        print(a)
        return
    else:
        flt(a)

flt(a)


