import os
import subprocess
import time



def currentuser() :
    user = (subprocess.run("echo %username%",shell=True,capture_output=True))
    user = user.stdout
    return user.decode()
def hostname() :
    host = subprocess.run("hostname",shell=True,capture_output=True)
    host = host.stdout
    return host.decode()



os.chdir(".//PsTools")
# print(os.getcwd())
hostip = "192.168.42.108"
cmd =  (r"PsExec.exe \\{} cmd").format(hostip)
subprocess.run(cmd,shell=True,capture_output=True)
time.sleep(2)
print(currentuser())
print(hostname())

# print("hello")
# p1 = subprocess.run("echo %username%",shell=True,capture_output=True)
# p2 = subprocess.run("hostname",shell=True,capture_output=True)
# # print("hello")
# p1 = p1.stdout
# p2 = p2.stdout
# p1 =  p1.decode()
# p2 =  p2.decode()
# print(p1,p2)




