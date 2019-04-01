import serial
import time
import RPi.GPIO as GPIO #for pi
#making serial connection with arduino

port = '/dev/ttyACM0'
runT = 3
arduino = serial.Serial(port, 9600, timeout= runT)

#pi GPIO Pins
#GPIO.setmode(GPIO.BCM)
#GPIO_TRIGGER_front = 21 #for utrasonic
#GPIO_ECHO_front = 20    #for utrasonic



class Zone:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def buildGrid(grid):
        for x in range(grid.width):
            for y in range (grid.height):
                print(x, y)

class Robot:
    destination = [0, 0]
    position = [0, 0]
    def __init__(self, initPosition):
        self.position = initPosition
        
        
        
def setPoint(robot):
    #print("passed in value: "+ str(robot.position))
    if (robot.position == [0,0]):
        robot.destination = [32, 32]
    if (robot.position == [0,91]):
        print("Setting destination")
        robot.destination = [32, 59]
    if (robot.position == [91,91]):
        robot.destination = [59, 59]
    if (robot.position == [91,0]):
        robot.destination = [59, 32]
        
    
def getDistance(sensor):
    GPIO.setmode(GPIO.BCM)
    print(sensor)
    if(sensor == "front"):
        GPIO_TRIGGER = 21 
        GPIO_ECHO = 20
    elif(sensor == "right"):
        GPIO_TRIGGER = 16 
        GPIO_ECHO = 12
    elif(sensor == "back"):
        GPIO_TRIGGER = 26 
        GPIO_ECHO = 19
    elif(sensor == "left"):
        GPIO_TRIGGER = 13 
        GPIO_ECHO = 6
      
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
    distance = ((TimeElapsed * 34300) / 2)/74
    
    return distance

def setInitPosition():
    front = right = back = left = 0
    position = [0, 0]
    front = getDistance("front")
    print("front:" +str(front))
    right = 100 #getDistance("right")
    back = 40 #getDistance("back")
    left = 2.9#getDistance("left")
    if(back <= 3 and left <= 3):       
        position = [0, 0]
    elif(front <= 3.0 and left <= 3.0):
        position = [0, 91]
    elif(front <= 3 and right <= 3):
        position = [91, 91]
    elif(back <= 3 and right <=3):
        position = [91, 0]
    robot = Robot(position)
        
    return robot

def turnRight(arduino, robot):
    arduino.write('right')
    robot.position[0] + 1 #move 1 inch right
def turnLeft(arduino, robot):
    arduino.write('left')
    robot.position[0] - 1 #move 1 inch left
def forward(arduino, robot):
    arduino.write('forward')
    robot.position[1] + 1 #move 1 inch forward
def backward(arduino, robot):
    arduino.write('backward')
    robot.position[1] - 1 #move 1 inch backward
    

while 1:
    #********************Prep**************************
    #connect arduino
    print(arduino.read())
    distance = 0
    gridSize = 3
   
    #initialize grid for zone
    board = Zone(gridSize, gridSize)
    board.buildGrid()
    
    
    #initialize robot position according to the sensors' reading
    robot = setInitPosition()
    print("Robot position: ",robot.position)
    
    #********************Prep**************************
    
    #********************Main decision**************************
    
    
    
    print(robot.destination)
    i=0
    for i in range(5):
        forward(arduino, robot)
        print("Robot position: ",robot.position)
        arduino.write('stop')
    break

setPoint(robot)
print("Next destination: ",robot.destination)
print("done")
GPIO.cleanup()
