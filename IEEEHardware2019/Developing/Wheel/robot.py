import serial
import time
#making serial connection with arduino
port = '/dev/ttyACM0'
runT = 3
arduino = serial.Serial(port, 9600, timeout= runT)


class Zone:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def buildGrid(grid):
        for x in range(grid.width):
            for y in range (grid.height):
                print(x, y)

class Robot:
	def __init__(self, initPosition):
		self.position = initPosition




#send signal to control the wheel

while 1:
    var = ''
    distance = 0
	gridSize = 3

	#test communication between arduino and python
    var = raw_input()
    if var == '0':
        arduino.write('0')
        print("The sensor is reading.")
        time.sleep(2)
   
    #initialize grid for zone
    board = Zone(gridSize, gridSize)
    board.buildGrid()
	
    
	#get distance from arduino
    if (arduino.inWaiting()>0):
        distance = arduino.readline()
        print("Reading: ", distance)

	#initialize robot position according to the sensors' reading
    robot = Robot((0,0))
    print("Robot position: ",robot.position)
       
