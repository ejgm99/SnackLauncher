from threading import Thread

import pygame,time

global xy
xy = [0,0]

pygame.init()
pygame.joystick.init()

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
        xy[1] = self.joystick.get_axis(1)

s = XYJoystick()

class Stepper():
    def __init__(self, p):
        self._running = True
        self.pos =p
        self.cpr = 200 # counts per revolution
        self.delay = .001 # seconds
        self.rps = 1.5
        self.direction = 0

        self.dirPin = 20
        self.stepPin = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.setup(self.stepPin, GPIO.OUT)

        self.minSpeed = 1 #rotations per second
        self.maxSpeed = 2 #rotations per second
        self.range = self.maxSpeed - self.minSpeed

        self.oldTime = time.time()
    def terminate(self):
        self._running = False
    def run(self):
        global xy
        while self._running:
            time.sleep(.5) #Five second delay
            print(str(self.pos),xy[self.pos])
    def scaleInput(self, speedIn):
        if speedIn > 0:
            self.direction = 1
        elif speedIn < 0:
            self.direction = 0

        speedIn = abs(speedIn)
        output = speedIN * self.range + self.minSpeed
        # delay = 1 / (cpr * rps)
        self.delay = 1 / (self.cpr * output)


X = Stepper(0)
XThread = Thread(target=X.run)
XThread.start()

Y = Stepper(1)
YThread = Thread(target=Y.run)
YThread.start()

while True:
    s.input()

TwoSecond.terminate()
FiveSecond.terminate()
