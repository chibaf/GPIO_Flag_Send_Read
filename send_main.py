import socket
from time import sleep
from GPIO_flag_send_class import GPIO_flag_send

host = '192.168.0.11'   # server ip address
port = 9988

gpio_flag=GPIO_flag_send(host,port)
s = gpio_flag.Socket  # establish socket connection

flags=[0]*16
while True:   # sending flags via socket
  sleep(2)
  gpio_flag.flag_send(s,flags)
