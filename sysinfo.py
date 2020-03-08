# import platform


# uname =  platform.uname()
# print(uname.system) #node = machine name 
# print(uname.node) #system = operating system
# print(uname.version) #os version


import subprocess
def currentuser() :
    user = (subprocess.run("echo %username%",shell=True,capture_output=True))
    user = user.stdout
    return user.decode()
def who() :
    username = (subprocess.run('''quser | find "Active"''',shell=True,capture_output=True,))
    username = username.stdout
    return username.decode()

def hostname() :
    host = subprocess.run("hostname",shell=True,capture_output=True)
    host = host.stdout
    return host.decode()
def gpuModel() :
    gpu = (subprocess.run("wmic path win32_VideoController get name",shell=True,capture_output=True))
    gpu = gpu.stdout
    gpu = gpu[5:]
    return gpu.decode()

def macaddr(hostip) :
    cmd = ('''getmac /s {} | find "Device" '''.format(hostip))
    macaddress = subprocess.run(cmd,shell=True,capture_output=True)
    macaddress = macaddress.stdout
    macaddress =  macaddress[0:14]
    return macaddress.decode()


print(currentuser())
print(hostname())
print(gpuModel())
hostip ="192.168.225.119"
print(macaddr(hostip))
# print(who())
