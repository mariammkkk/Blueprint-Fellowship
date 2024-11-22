import threading
import socket
import time

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET --> types of address your program can work with
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# user input
print("--- Enter User Credentials ---")
username = input("Username: ")
password = input("Password: ")

# connect to the server on local machine
server_binding = ("localhost", 9999)
cs.connect(server_binding)

# sends the username and password to the server
cs.send(username.encode())
time.sleep(0.1) # add a small delay
cs.send(password.encode())

# receive data from server:
data_from_server = cs.recv(1024)
response = data_from_server.decode()
print("[C]: Data received from server: " + response)

if "Unauthorized" in response:
    print("[C]: Login failed.")
else:
    print("[C]: Login successful.")

# close the client sockets
cs.close()
exit()
