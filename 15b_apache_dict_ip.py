"""Open a log file from a Unix/Linux system—for example, one from the Apache server. 
For each response code (i.e., three-digit code indicating the HTTP request’s success or failure), 
store a list of IP addresses that generated that code.
"""
from pprint import pprint
from collections import defaultdict
# MY SOLUTION
def apache_codes(file):
    response_codes = {}
    with open(file, 'r')as f:
        for line in f.readlines():
            log_entry = line.split()
            response = log_entry[8]
            ip_addr = log_entry[0]
            response_codes.setdefault(response, []).append(ip_addr)
    pprint(response_codes)
    print()

    total_ips = []
    for k,v in response_codes.items():
        print(f'{k} - {len(v)} ips.')
        total_ips.append(int(len(v)))
    print(sum(total_ips), "total IP addresses.")

apache_codes('apache.log')
print()
#apache404('apache.log')


# BOOK SOLUTION
# Utilizing defaultdic from the collections module
def ip_address(filename):
    output = defaultdict(list)
    
    for one_line in open(filename):
        field = one_line.split()
        ip = field[0]
        response_code = field[8]
        output[response_code].append(ip)

    return output

pprint(ip_address('apache2.log'))


