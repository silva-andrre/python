#code from THM Python4Pentesters

#Melhorias: incluir barra de evolucao para acompanhar a qtde de portas ja listadas

import sys,socket,pyfiglet

ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \n Port Scanner")
print(ascii_banner)

ip = sys.argv[1]
open_ports = []

ports = range(1,65535)

def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print ("Open ports are: ")
    print (sorted(open_ports))
else:
    print("Looks like no ports are open :[")
