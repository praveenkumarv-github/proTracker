import pyping
import platform 
from .core import *


hostnames = [
    "192.168.0.0",
    "192.168.0.1",
    "192.168.1.224",
    "192.168.1.225",
    ]

for host in hostnames :
    r = pyping.ping(host)
    if r.ret_code == 0:
        data = (("{} - ACTIVE \n").format(host))
        print(("{}   - Active").format(host))
        with open("active.inactivehostname.txt",'a') as fopen :
            fopen.write(data)
    else:
        data = (("{} - INACTIVE \n").format(host))
        print("Failed with {} / {}  Inactive".format(r.ret_code,host))
        with open("active.inactivehostname.txt",'a') as fopen :
            fopen.write(data)
            
            
            
    