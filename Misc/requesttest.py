import requests
import subprocess
import socket
urls = ['intranet.com', 'https://bbc.co.uk']
ips = ["192.168.167.20","192.168.167.6"] 
urlReached = []
urlNotReached = []
reached = []  
not_reached = []  
reverse_dns = []   
def request_test(sites):
    for url in urls:
        resp = requests.get(url)
        respcode = resp.status_code
        if respcode == 200:
            urlReached.append(url)
        else: 
            urlNotReached.append(url)

def ping_test (ips):
    for ip in ips:
        ping_test = subprocess.call('ping %s -n 2' % ip)      
        if ping_test == 0:                   
            reached.append(ip)
        else:
            not_reached.append(ip)                             

def nslookup_test(hosts):
    for ip in ips:
        nslookuptest = socket.getfqdn(ip)
        reverse_dns.append(nslookuptest)
        

ping_test(ips)
request_test(urls)
nslookup_test(ips)

print("these urls were not accessable over http/https : " + str(urlNotReached))
print("these urls were accessable over http/https : " + str(urlReached))
print("these ips were accessable over ping : " + str(reached))
print("these ips were not accessable over ping : " + str(not_reached))
print("these DNS records were resolved from IP list : " + str(reverse_dns))