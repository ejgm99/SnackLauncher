from threading import Thread
import pygame,time


global xy
xy = [0,0]
pygame.init()
pygame.joystick.init()

class Hello5Program():
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global cycle
        while self._running:
            time.sleep(.5) #Five second delay
            print(cycle)


class XYJoystick():
    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.prX = 0
        self.prY = 0
    def input(self):
        global xy
        pygame.event.get()
        xy[0] = self.joystick.get_axis(0)

print("Joystick Test")
s = XYJoystick()
s.input()

# X = Stepper()
# XThread = Thread(target=Stepper.run)
# X = Stepper()
# XThread.start()

FiveSecond = Hello5Program()
#Create Thread
FiveSecondThread = Thread(target=Hello5Program.run)
#Start Thread
FiveSecondThread.start()

while True:
    s.input()
