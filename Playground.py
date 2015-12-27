__author__ = 'nehaavishwa'



def luuping():
    i=0

    while (i<=200):
        if(i<=100):
            i=i+1
            continue
        elif(i<150):
            x=i%2
            if x==0:
                print("Number is even", i)
            else:
                print("Number is odd", i)
        else:
            break

        i=i+1


def seq_class(immutable):
    if immutable:
        cls=tuple
    else:
        cls=list

    return cls

def seq_class1(immutable):
    return tuple if immutable else list




seq=seq_class1(True)
print(seq('hhfhfh'))
#luuping()
