#!bin/python3

#IMPORTS
from socket import *

#FUNCTIONS
def Scanner(Target_Client, Target_Port):
    try:
        Connection_Scan = socket(AF_INET, SOCK_STREAM)
        Connection_Scan.connect((Target_Client, Target_Port))
        print("[+]%d/tcp open"% Target_Port)
        Connection_Scan.close()
    except:
        print("[-]%d/tcp closed"% Target_Port)
def Port_Scan(Target_Client, Target_Ports):
    try:
        Target_Address = gethostbyname(Target_Client)
    except:
        print("[-] No Resolve %s "% Target_Client)
        return
    try:
        Target_Name = gethostbyaddr(Target_Address)
        print("\n[+] Scan result of: %s " % Target_Name[0])
    except:
        print("\n[+] Scan result of: %s " % Target_Address)
    setdefaulttimeout(1)
    for Target_Port in Target_Ports:
        print("Scanning Port: %d"%  Target_Port)
        Scanner(Target_Client, int(Target_Port))

#CODE
if __name__ == "__main__":
    Real_Target = input("Input hostname or ip \n >")
    Real_Ports = input("Input Ports in the following syntax: [80, 22, 2444] \n >")
    Port_Scan(Real_Target, [Real_Ports])