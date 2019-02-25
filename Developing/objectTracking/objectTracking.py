import cv2
import numpy as np

def nothing():
    pass
def getColor():
    #color = input('Enter color: ')
    return raw_input('Enter color: ')

def createTrackbars():
    #create a black img window
    img = np.zeros((300, 512,3), np.uint8) #Return a new array of given shape and type, filled with zeros.
    cv2.namedWindow('image')

    #create trackbars for color change
    cv2.createTrackbar('R', 'image', 0, 255, nothing)#(trackbarName, windowName, value, count, onChange)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    #create switch for ON/OFF
    switch = '0 : OFF\n1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while(1):
        cv2.imshow('imgage', img)
        k = cv2.waitKey(1) & 0xFF #Waits for a pressed key. returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
        if k == 27: #esc is pressed
            break

        #get current positions of four trackbars
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos('S', 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]
    cv2.destroyAllWindows()

def main():
    #declare variables
    Red = ([17, 15, 100], [50, 56, 200]) # lower, upper
    Blue = ([86, 31, 4], [220, 88, 50])
    Yellow = ([25, 146, 190], [62, 174, 250])
    Green = ([47, 61, 60], [80, 255, 255])

    Frame_H = 480
    Frame_W = 640
    maxNumObj = 50
    minObjArea = 20 * 20
    maxObjArea = Frame_H * Frame_W /1.5
    trackObjects = False
    useMorphOps = False
    cameraON = cv2.VideoCapture(0)
    print(cameraON)
    color = getColor()
    #Mat cameraFeed #to store each frame of webcam feed
    #Mat HSV # store HSV img
    #Mat threshold # store binary threshold img
    x = y = 0 #x and y value of the location of the object
    #createTrackbars()
    while(1):
        _, frame = cameraON.read()
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if(color == 'red'):
            mask = cv2.inRange(frame, np.array(Red[0], "uint8"), np.array(Red[1], "uint8"))#find the color within the boundaries
        elif(color == 'blue'):
            mask = cv2.inRange(frame, np.array(Blue[0], "uint8"), np.array(Blue[1], "uint8"))#find the color within the boundaries
        elif(color == 'yellow'):
            mask = cv2.inRange(frame, np.array(Yellow[0], "uint8"), np.array(Yellow[1], "uint8"))#find the color within the boundaries
        elif(color == 'green'):
            mask = cv2.inRange(frame, np.array([65,60,60]), np.array([80,255,255]))
        output = cv2.bitwise_and(frame, frame, mask = mask)

        #show the image
        cv2.imshow("frame", frame) #hstack: Stack arrays in sequence horizontally (column wise).
        cv2.imshow("mask", mask)
        cv2.imshow("Output", output)
        k = cv2.waitKey(1) & 0xFF #Waits for a pressed key. returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.
        if k == 27: #esc is pressed
            break
    return 0;

main()
