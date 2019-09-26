import pygame

pygame.init()
pygame.joystick.init()

class XYJoystick():
    def __init__(self,path = "../../../../dev/ttyUSB0"):
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.prX = 0
        self.prY = 0
        self._running = True
    def terminate(self):
        self._running = False
    def run(self):
        global x
        global y
        global z
        self.input()
    def input(self):
        pygame.event.get()
        self.x = int(self.joystick.get_axis(0)*10)
        self.y = int(self.joystick.get_axis(1)*10)
        self.b = self.joystick.get_button(0)
        self.clean()
    def clean(self):
        if(abs(self.x) >5) and (abs(self.y)<4):
            self.y = 0
        if(abs(self.y) >5) and (abs(self.x)<4):
            self.x = 0
    def getMsg(self):
        return self.signedInttoStr(self.x) + self.signedInttoStr(self.y)+str(self.b)
    def signedInttoStr(self, n):
        out = ""
        if(n==0):
            return "c0"
        if(n == -10):
            n = -9
        if(n == 10):
            n = 9
        if(n>0):
            out ="c"
        if(n<0):
            out ="a"
        out = out + str(abs(n))
        # if len(out)>1:
        #     if(n >= 10):
        #         out ='9'
        # if (n>0):
        #     out = "+"+out
        return out
