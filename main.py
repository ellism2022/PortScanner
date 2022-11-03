import socket
import time
import sys
from datetime import datetime
from smtpd import program

now = datetime.now()

with open('filename.txt', 'a') as file:
    print("Starting Date and Time =", now)
    print("Starting Date and Time =", now, file=file)

try:
    remoteServer = input("Enter a host to scan: ")
    ip = socket.gethostbyname(remoteServer)
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Host is not available")
    sys.exit()
except KeyboardInterrupt:
    print("You manually exited the program")
    sys.exit()

for port in range(1, 1026):
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((ip, port))
    except:
        with open('filename.txt', 'a') as file:
            print('[OPEN] Port open :', port)
            print('[OPEN] Port open :', port, file=file)

later = datetime.now()

with open('filename.txt', 'a') as file:
    print("Ending Date and Time =", later)
    print("Ending Date and Time =", later, file=file)

print('Time taken:', later - now)
with open('filename.txt', 'a') as file:
    print('Time taken: ', later - now, file=file)

