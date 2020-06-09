#A simple python script to check if an IP address is available

import subprocess #allows to spawn processes, connect to their I/O pipes
import platform   #access the underlying platform’s data (hardware, OS, etc)

def ip(current_ip):
        try:
            result = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip), shell=True, universal_newlines=True)
            if 'unreachable' in result:
                return False
            else:
                return True
        except Exception:
                return False

if __name__ == '__main__':
    #The Google Public DNS IP addresses (IPv4) are as follows for testing purposes:
    #['8.8.8.8' , '8.8.4.4']
    current_ip = ['8.8.8.8', '1.1.4.1', '8.8.4.4']
    for IP in current_ip:
        if ip(IP):
            print(f"{IP} - ping successful")
        else:
            print(f"{IP} - ping unsuccessful")
