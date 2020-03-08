# from pythonping import ping
# import sys

# ping("",verbose=True,out=sys.stdout)


import os
hostnames = ["127.0.0.1","google.com","yahoo.com"]
for host in hostnames :
    response = os.system("ping -c 1 " + host)

    if response == 0:
        print (host, 'is up!')
        data = (("{} - ONLINE \n").format(host))
        with open("log.txt",'a') as fopen :
            fopen.write(data)
    else:
        print (host, 'is down!')









