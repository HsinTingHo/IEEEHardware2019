import serial
import time
import RPi.GPIO as GPIO #for pi
#making serial connection with arduino
port = '/dev/ttyACM0'
runT = 3
#arduino = serial.Serial(port, 9600, timeout= runT)

#pi GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 21 #for utrasonic
GPIO_ECHO = 20    #for utrasonic



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
        
    
def getDistance(GPIO_TRIGGER, GPIO_ECHO):
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print(str(distance))
    return distance




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
    #if (arduino.inWaiting()>0):
        #distance = arduino.readline()
        #print("Reading: ", distance)

    #initialize robot position according to the sensors' reading
    robot = Robot((0,0))
    print("Robot position: ",robot.position)
    getDistance(GPIO_TRIGGER, GPIO_ECHO)
    
    print("done")
    GPIO.cleanup()
