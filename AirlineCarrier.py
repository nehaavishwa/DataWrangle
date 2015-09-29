from bs4 import BeautifulSoup


def options(soup, id1):
    option_values = []
    carrier_list = soup.find(id=id1)
    print('\n')
    print(carrier_list) #.find_all('option'))
    for option in carrier_list.find_all('option'):
        #print(option)
        option_values.append(option['value'])
        #print(option_values)
    return option_values


def print_list(label, codes):
    print("\n%s:" % label)
    for c in codes:
        print(c)


def main():
    soup = BeautifulSoup(open(r'C:\Users\nVishwakarma\Downloads\DataElements.html'))

    codes = options(soup, 'CarrierList')
    print_list('Carrier', codes)

    codes = options(soup, 'AirportList')
    print_list('Airport', codes)

main()

