import wmi

con = wmi.WMI()

for i in con.Win32_BaseBoard():
    serialnumb = i.SerialNumber
    motherBoardBrand = i.Product
    print("1",serialnumb)
    data = (("serialnumber  {}  | motherBoardBrand  {} /n").format(serialnumb,motherBoardBrand))
    with open("machinedetails.txt",'a') as fopen :
        fopen.write(data)

for os in con.Win32_Processor():
    processorName = os.Name
    corecount = os.NumberOfCores
    data = ((" processorName -- {}   |   corecount -- {}").format(processorName,corecount))
    with open("machinedetails.txt",'a') as fopen :
        fopen.write(data)
for bi in con.Win32_Bios():
    print(bi.SerialNumber)