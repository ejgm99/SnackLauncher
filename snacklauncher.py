from threading import Thread

import pygame,time

global xy,dxy
xy = [0,0]
dxy = [False, False]
pygame.init()
pygame.joystick.init()

class XYJoystick():
    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.prX = 0
        self.prY = 0
        self.xMax = .00500
        self.xMin = .00250
        self.xRange = self.xMax - self.xMin
        self.yMax = .00500
        self.yMin = .00250
        self.yRange = self.yMax - self.yMin
    def input(self):
        global xy
        global dxy
        pygame.event.get()
        xInput = self.clip(self.joystick.get_axis(0))
        yInput = self.clip(self.joystick.get_axis(1))
        dxy[0] = xInput>0
        dxy[1] = yInput>0
        xy[0] = self.scaleInput(abs(xInput), self.xRange,0)
        xy[1] = self.scaleInput(abs(yInput), self.yRange,500)
    def clip(self, n):
        if(abs(n)<.1):
            n =0
        return n
    def scaleInput(self, n, range,c):
        if(n==0):
            return -1
        return n*range+c

s = XYJoystick()

class Stepper():
    def __init__(self, p, step_pin,dir_pin, is_coupled = False ):
        self._running = True
        self.pos =p
        self.cpr = 200 # counts per revolution
        self.delay = .001 # seconds
        self.rps = 1.5
        self.direction = 0
        self.is_coupled = is_coupled

        self.dirPin = step_pin
        self.stepPin = dir_pin

        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.dirPin, GPIO.OUT)
        # GPIO.setup(self.stepPin, GPIO.OUT)

        self.minSpeed = 1 #rotations per second
        self.maxSpeed = 2 #rotations per second
        self.range = self.maxSpeed - self.minSpeed

        self.oldTime = time.time()
    def terminate(self):
        self._running = False
    def run(self):
        global xy, dxy
        while self._running:
            delay = xy[self.pos]
            dir = dxy[self.pos]
            if(self.is_coupled):
                dir = not dir
            print(self.is_coupled, dir)
            if(xy[self.pos]!=-1):
                self.pulseStepper(delay,dir)
    def pulseStepper(self, delay, dir):
            # GPIO.output(self.dirPin, self.stepPin)
            # GPIO.output(STEP, GPIO.HIGH)
            print(xy[self.pos])
            # GPIO.output(STEP, GPIO.LOW)
            # print(dxy[self.pos])

X = Stepper(0,20,21)
XThread = Thread(target=X.run)
XThread.start()

# Y = Stepper(1,22,23)
# YThread = Thread(target=Y.run)
# YThread.start()
#
# cY = Stepper(1,20,21,is_coupled = True)
# cYThread = Thread(target=cY.run)
# cYThread.start()

while True:
    s.input()
