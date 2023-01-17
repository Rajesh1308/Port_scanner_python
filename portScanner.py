from socket import *
def conscan(tghost, tgport):
    try: 
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.settimeout(0.8)
        connskt.connect((tghost,tgport))
        
        print("[+] port %d tcp open"% tgport)
        connskt.close()

    except:
        #print("[-] port %d tcp closed"% tgport)
        pass

def portScan(tghost, tgports):
    try:
        tgIp = gethostbyname(tghost)
        print("---------------------------------------------------")
        print("Starting scan on host : ",tgIp)
        print("---------------------------------------------------")
        print("Running TCP scan on the target...")
    except:
        print("[-] Cannot resolve %s"% tghost)

       
    
    for tgport in tgports:
        #print("Scanning port %d"% tgport)
        conscan(tghost, int(tgport))
        


if __name__ == '__main__':
    print("---------Port Scanner---------")
    tghost = input(">>Enter the target host (Example : www.google.com) : ")
    print("\n---------Port details---------")

    print("  1.Fast scan : Scans important ports")
    print("  2.Manually set port")
    ch = int(input(">>Enter the choice (1/2): "))
    if ch == 1:
        portslist = [21,22,25,53,80,110,111,123,135,139,143,443,445,465,631,993,995,1723,3306,3389,5900,8080]
        portScan(tghost,portslist)
        print("\n>>Scanned 22 well known ports")

    elif ch == 2:
        print("  1.Scan a single port")
        print("  2.Scan a range of ports")
        ch = int(input(">>Enter the choice (1/2): "))

        if ch == 1:
            portno = int(input(">>Enter port number : "))
            portslist = range(portno, portno+1)
            portScan(tghost,portslist)
            print("\n>>Scanned port ",portno)

        elif ch == 2:
            start_port = int(input(">>Enter starting port : "))
            end_port = int(input(">>Enter ending port : "))
            portslist = range(start_port, end_port+1)
            portScan(tghost,portslist)
            print("\n>>Scanned ports from ", start_port,"to", end_port)
    print("\n>>Session ended.")
