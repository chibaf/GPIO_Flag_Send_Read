import socket
import time
from GPIO_flag_read_class import GPIO_flag_read

host = '192.168.0.11'  # server ip address
port = 9988

read_socket=GPIO_flag_read(host,port)
s=read_socket.Socket

conn = read_socket.setupConnection(s)
while True: # read data via socket
  data=read_socket.dataTransfer(conn)
  print(data)
