class GPIO_flag_read:

  import socket

#host = '192.168.0.11'  # server ip address
#port = 9988

  def __init__(self,host,port):   # set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #reuse address
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return self.s

  def setupConnection(self,s):   # establish socket connection with client by client requést
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

  def dataTransfer(self,conn):  # receive data from client via socket
    while True:
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        flags = [str(val) for val in data.split(",")]  # devide line into flags
        print(flags)
#    conn.close()
