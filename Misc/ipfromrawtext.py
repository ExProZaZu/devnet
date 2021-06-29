import re
import itertools
file = open("iptextfile.txt")
for line in file:
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
        print(ip)