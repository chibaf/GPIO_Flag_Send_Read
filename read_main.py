import socket
import time
from GPIO_flag_read_class import GPIO_flag_read  # read flags from socket

host = '192.168.0.11'  # server ip address
port = 9988  #port number

read_socket=GPIO_flag_read(host,port)  #set up socket
s=read_socket.Socket # socket

conn = read_socket.setupConnection(s)  # establish socket connection
while True:
  flags=read_socket.dataTransfer(conn)  # read flags via socket
  print(flags)
