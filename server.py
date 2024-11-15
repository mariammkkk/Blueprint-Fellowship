import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()

def check_credentials(c):
    c = sqlite3.connect('mydatabase.db')
    cursor = c.cursor()
    cursor.execute(f"""SELECT * 
    FROM users
    WHERE username = '{username}';""")
    rows = cursor.fetchall()

    for username, password in rows:
        if username == rows.username and password == rows.password:
            print("You are an authorized user.")
        else:
            print("You are not an authorized user.")

    c.send()
    account = c.recv(1024).decode() # 1024 bytes tells us the size / buffer of the content we are recieving so that the socket knows how much to expect
    print("[S]: Data received from client: " + account)

    count = 0
    while(count < 100): # use loop to send 1, 2, 3, 4, 5 to client --> you can only send strings 
        c.send(str(count).encode())
        response = c.recv(1024).decode()
        print("[S]: Data received from client: " + response)
        count+=1

    print("Done")

    while True:
        client, addr = ss.accept()
        t2 = threading.Thread(target=check_credentials, args=(client,))
        t2.start()
    
    # Close the connection
        c.close()
    # Close the server socket
        ss.close()
        exit()
          
