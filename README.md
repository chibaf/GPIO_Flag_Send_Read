# GPIO_Flag_Send_Read
# sending GPIO flags to another RasPi via socket

(RasPi1->RasPi2)

programs positions:

read flags: GPIO_flag_read_class.py,read_main.py: on RasPi2

send flags: GPIO_flag_send_class.py,send_main.py: on RasPi1

usage:

python3 read_main.py (on RasPi2)

python3 send_main.py (on RasPi1)

where the ip address of RasPi2 is required.

# ref: 

chibaf/socket_exercise_1: socket on tcp/ip https://github.com/chibaf/socket_exercise_1

Classes — Python 3.10.6 documentation https://docs.python.org/3/tutorial/classes.html
