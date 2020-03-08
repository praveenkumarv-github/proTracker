import os
import subprocess
import time

print("helll")

os.chdir(".//PsTools")
hostip = "192.168.42.108"
cmd =  (r"PsExec.exe \\{} cmd").format(hostip)
subprocess.run(cmd,shell=True,capture_output=True)
time.sleep(2)



