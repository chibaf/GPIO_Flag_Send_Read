import socket
from time import sleep
import GPIO_flag_send_class

host = '192.168.0.11'   # server ip address
port = 9988

gpio_flag=GPIO_flag_send(host,port)
s = gpio_flag.s  # establish socket connection

flags=[0]*16
while True:   # sending flags via socket
  sleep(2)
  gpio_flag.flag_send(s,flags)
