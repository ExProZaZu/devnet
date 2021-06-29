import requests
import subprocess
urls = ['http://google.com', 'https://bbc.co.uk']
hosts = ["192.168.167.20","192.168.167.6"] 
urlReached = []
urlNotReached = []
reached = []  
not_reached = []     
def request_test(sites):
    for url in urls:
        resp = requests.get(url)
        respcode = resp.status_code
        if respcode == 200:
            urlReached.append(url)
        else: 
            urlNotReached.append(url)

def ping_test (host):
    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' % ip)      
        if ping_test == 0:                   
            reached.append(ip)
        else:
            not_reached.append(ip)                             

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
ping_test(hosts)
request_test(urls)
print("these urls were not accessable over http/https : " + str(urlNotReached))
print("these urls were accessable over http/https : " + str(urlReached))
print("these ips were accessable over ping : " + str(reached))
print("these ips were not accessable over ping : " + str(not_reached))