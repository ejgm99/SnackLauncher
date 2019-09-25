import XYJoystick, ArduinoSerial

s = XYJoystick.XYJoystick()
ser = ArduinoSerial.arduino_serial();

while True:
    s.input()
    print(s.getMsg())
    ser.write(s.getMsg())
    print(ser.readLine())
