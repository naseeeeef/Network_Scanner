
import socket

#called from imported package
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#for user can enter the input
ipaddress = input("enter your ipaddress:")
port = int(input("enter your port:"))

#for define the exception
def PortScanner(port):
    if sock.connect_ex((ipaddress,port)):
        print(f"PORT {port} is closed ( :")
    else:
        print(f"PORT {port} is open : )")
PortScanner(port)
