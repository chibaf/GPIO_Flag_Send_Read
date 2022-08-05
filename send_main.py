import socket
from time import sleep
from GPIO_flag_send_class import GPIO_flag_send  # send flags to RasPi via socket

host = '192.168.0.11'   # server ip address
port = 9988  #poert number

gpio_flag=GPIO_flag_send(host,port)  # establish socket connection
s = gpio_flag.Socket

flags=[0]*16  # flag data for GPIO
i=0
while True:   # sending flags via socket
  sleep(2)
  i=i+1
  flags[0]=i % 10
  gpio_flag.flag_send(s,flags)
