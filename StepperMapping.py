import threading
import time
import RPi.GPIO as GPIO

class horizontalAxis(threading.Thread):
    def init(self):
        threading.Thread.__init__(self)

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

    def run(self):
        while True:
            #access data from the queue to get the latest speed
            # speed value -1 to 1
            self.currentTime = time.time()
            if self.currentTIme - oldTime > self.delay:
                GPIO.output(self.stepPin, GPIO.HIGH)
                GPIO.output(self.dirPin, self.direction)
                GPIO.output(self.stepPin, GPIO.LOW)
                self.oldTime = self.currentTime

    def scaleInput(self, speedIn):
        if speedIn > 0:
            self.direction = 1
        elif speedIn < 0:
            self.direction = 0

        speedIn = abs(speedIn)
        output = speedIN * self.range + self.minSpeed
        # delay = 1 / (cpr * rps)
        self.delay = 1 / (self.cpr * output)
