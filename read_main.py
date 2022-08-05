import socket
import time
import GPIO_flag_read_class

host = '192.168.0.11'  # server ip address
port = 9988

read_socket=GPIO_flag_read(host,port)
s=read_socket.s

while True: # read data via socket
  conn = read_socket.setupConnection(s)
  read_socket.dataTransfer(conn)
