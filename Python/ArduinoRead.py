import serial

ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 9600
ser.timeout  = 2

ser.open()
ser.flushInput()

while 1:
	print(ser.readline())
	


