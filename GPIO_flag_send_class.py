def mkline(flags):  # pack flags into a line
  line=''
  for i in range(0,len(flags)):
    if i==0:
      line=str(flags[0])
    else:
      line=line+","+str(flags[i])
  return line

class GPIO_flag_send:

  import socket

  def __init__(self,host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establish socket connection
    s.connect((host, port))
    return self.s
    
  def flag_send(self,s,flags):
    line=mkline(flags)
    s.send(str.encode(line))

