import socket
import sys

if len(sys.argv) < 3:
    print(f"Uso {sys.argv[0]} [host] [porta]")
    sys.exit(1)

#target_host = "www.pudim.com.br"
#target_port = 80

target_host = sys.argv[1]
target_port = int(sys.argv[2])

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
