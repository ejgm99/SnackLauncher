from threading import Thread
import time

global cycle
cycle = 0.0

class Hello5Program:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global cycle
        while self._running:
            time.sleep(5) #Five second delay
            print("5 Cycle I've recieved: ", cycle)
            cycle = cycle + 1.0
            print("5 Cycle I'm leaving: ", cycle)

class Hello2Program:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        global cycle
        while self._running:
            time.sleep(2) #Five second delay
            print("2 Cycle I've recieved: ", cycle)
            cycle = cycle + 0.5
            print("2 Cycle I'm leaving: ", cycle)

#Create Class
FiveSecond = Hello5Program()
print(cycle)
#Create Thread
FiveSecondThread = Thread(target=FiveSecond.run)
print(cycle)
#Start Thread
FiveSecondThread.start()
print(cycle)

#Create Class
TwoSecond = Hello2Program()
#Create Thread
TwoSecondThread = Thread(target=TwoSecond.run)
#Start Thread
TwoSecondThread.start()


Exit = False #Exit flag
while Exit==False:
 print("M Cycle I've recieved")
 cycle = cycle + 0.1
 print("M Cycle I'm Sen ", cycle)
 time.sleep(1) #One second delay
 if (cycle > 5): Exit = True #Exit Program

TwoSecond.terminate()
FiveSecond.terminate()
print("Goodbye :)")
