import serial,time

class arduino_serial(): #interface for talking to arduino
    def __init__(self,path = "../../../../../dev/tty.usbserial-DN00YO77", rate = 250000):
        self.serial = serial.Serial(path, rate)
        self.out = "hello"
        self.mode = True
        self.response = ""
        time.sleep(2)
        print("yeet")
    def write(self, msg):
        self.serial.write(msg.encode("ascii"))
        # print("        writing: "+msg)
        # print("        flushng...")
        # self.serial.flush()
        # print("        flushed! ")
    def hardReset(self):
        print("Reseting arduino")
        self.write("00000000")
        self.serial.close()
        self.serial.open()
        time.sleep(1)
        self.serial.reset_input_buffer()
    def clearOut(self):
        self.serial.reset_output_buffer()
    def readLine(self):
        out = self.serial.readline()
        return out
    def specialWrite(self,msg): #this willl be improved later but for now is just this
        time.sleep(2) #this delay is needed because of serial shenanigans
        self.write(msg)
