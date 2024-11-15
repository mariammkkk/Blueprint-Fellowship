import threading
import socket

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

# receive data from server:
data_from_server=cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)    
cs.send([username, password]).encode() # sends the username and password to the server as a list

count = 0
while(count < 100): # use loop to send 1, 2, 3, 4, 5 to client
    response = cs.recv(1024).decode()
    print("[C]: Data received from server: " + response)
    response = "Acknowledging " + str(count)
    cs.send(response.encode())
    count+=1

print("Done")

# close the client sockets
cs.close()
exit()