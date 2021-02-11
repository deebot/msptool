import serial
import serial.tools.list_ports
import os

class Model:
    def __init__(self):
        self.currentCom =""
        self.filePath=""
        #self.port_list = list(serial.tools.list_ports.comports())
        #self.ports=list()
        pass

    def serial_ports(self):
        return serial.tools.list_ports.comports()

    def flash(self):
        print("Flashing started")
        print("In model the curent com is: ",self.currentCom)
        print("In model the file path is:",self.filePath)
        com =self.currentCom.split()[0]
        print(com)
        command = "./mspdebug/mspdebug rom-bsl -d " + com + " \"prog " + self.filePath + "\""
        os.system(command)



if __name__ == '__main__':
    pass






    #def show_port(self):
     #   #print(self.port_list[1].__dict__)
     #   print("ShowPort function in Model")
      #  for port, desc, hwid in sorted(self.port_list):
      #      self.ports.append(port)
      #  return self.ports