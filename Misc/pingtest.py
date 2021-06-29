import subprocess
def ping_test (host):

    reached = []                           #Empty list to collect reachable hosts
    not_reached = []                          #Empty list to collect unreachable hosts

    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' % ip)        #Ping host n times
        if ping_test == 0:                    #If ping test is 0, it' reachable
            reached.append(ip)

        else:
            not_reached.append(ip)                              #Else, it's not reachable

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
hosts = ["192.168.167.20","192.168.167.6","192.168.21.198","192.168.22.211","192.168.22.212","192.168.22.217","192.168.23.82","192.168.23.254","192.168.167.55","192.168.167.10", "192.168.167.8"]         #Hosts list
ping_test (hosts)