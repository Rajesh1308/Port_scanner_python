# importing sockets
from socket import *

#conscan functions connects to the target
def conscan(tghost, tgport):

    try: 
        #Connecting to the port of target
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.settimeout(0.8)
        connskt.connect((tghost,tgport))
        
        print("[+] port %d/tcp open"% tgport)
        connskt.close()

    except:
        pass

#portscan function finds the host IP and call conscan function
def portScan(tghost, tgports):
    try:
        tgIp = gethostbyname(tghost)
        print("-" * 110)
        print("Starting scan on host : ",tgIp)
        print("-" * 110)
        print("Running TCP scan on the target...")
    except:
        print("[-] Cannot resolve %s"% tghost)

    #This loop is to iterate through each ports 
    for tgport in tgports:
        conscan(tghost, int(tgport))
        

if __name__ == '__main__':

    #Starting port scanner
    print("\n"+"-" * 52 +  "Port Scanner" + "-" * 52)

    #Getting target
    tghost = input(">>Enter the target host (Example : www.google.com or IP addr) : ")

    #Getting port details to scan via if statements
    print("\n" + "-" * 50 + "Port scan details" + "-" * 50)

    print("  1.Fast scan : Scans 30 well known ports (Recommended)")
    print("  2.Manually set port for scanning")
    ch = int(input(">>Enter the choice (1/2): "))
    if ch == 1:
        #port list contains the list of ports for Fast scan
        portslist = [21,22,23,25,53,80,110,111,123,135,139,143,443,445,465,513,514,631,993,995,1723,2049,2121,3306,3389,5432,5900,6000,8009,8080]
        print("-" * 110)
        print("Ports scanned in Fast scan : \n",portslist)
        
        print("-" * 110)
        portScan(tghost,portslist)
        print("\n>>Scanned 30 well known ports")

    elif ch == 2:
        #Manually set ports for scanning
        print("  1.Scan a single port")
        print("  2.Scan a range of ports")
        ch = int(input(">>Enter the choice (1/2): "))

        if ch == 1:
            #Scan single port that entered
            portno = int(input(">>Enter port number : "))
            portslist = range(portno, portno+1)
            portScan(tghost,portslist)
            print("\n>>Scanned port ",portno)

        elif ch == 2:
            #Scans over a range of ports entered
            start_port = int(input(">>Enter starting port : "))
            end_port = int(input(">>Enter ending port : "))
            portslist = range(start_port, end_port+1)
            portScan(tghost,portslist)
            print("\n>>Scanned ports from ", start_port,"to", end_port)
    #Task completed
    print("\n>>Session ended.")
