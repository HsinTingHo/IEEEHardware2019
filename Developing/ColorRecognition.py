import cv2
import numpy as np
print (cv2.__version__)

cap = cv2.VideoCapture(0)   #enables video capture
print(cap)

while cap.read():
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #converts the current frame from color to hsv

    #defines the lower and upper range of red, blue, and yellow
    lower_red = np.array ([100,50,50])      #([136,87,111])
    upper_red = np.array ([140,255,255])    #([180,255,255])

    lower_blue = np.array ([99,115,150])
    upper_blue = np.array ([110,255,255])

    lower_yellow = np.array ([40,50,50])    #yellow ([22,60,200])
    upper_yellow = np.array ([80,255,255])  #yellow ([60,255,255])

    #cleans the frame and creates the individual color mask
    maskRed = cv2.inRange (hsv, lower_red, upper_red)
    maskRed = cv2.erode (maskRed, None, iterations=2)
    maskRed = cv2.dilate (maskRed, None, iterations=2)

    maskBlue = cv2.inRange (hsv, lower_blue, upper_blue)
    maskBlue = cv2.erode (maskBlue, None, iterations=2)
    maskBlue = cv2.dilate (maskBlue, None, iterations=2)

    maskYellow = cv2.inRange (hsv, lower_yellow, upper_yellow)
    maskYellow = cv2.erode (maskYellow, None, iterations=2)
    maskYellow = cv2.dilate (maskYellow, None, iterations=2)

    
    mask = cv2.bitwise_or (maskRed, maskBlue, maskYellow) #creates the final mask
    res = cv2.bitwise_and (frame, frame, mask = mask)   #final result

    #draws the boxes around detect color
    _, contours, _= cv2.findContours (maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, cont in enumerate(contours):
        area = cv2.contourArea (cont)
        if (area > 300):
            x,y,w,h = cv2.boundingRect (cont)
            frame = cv2.rectangle (frame, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText (frame, 'red', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    #cv2.drawContours (frame, contours, -1, (0,0,255), 2)

    _, contours, _= cv2.findContours (maskBlue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for pic, cont in enumerate(contours):
        area = cv2.contourArea (cont)
        if (area > 300):
            x,y,w,h = cv2.boundingRect (cont)
            frame = cv2.rectangle (frame, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText (frame, 'blue', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    #cv2.drawContours (frame, contours, -1, (255,0,0), 2)

    _, contours, _= cv2.findContours (maskYellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, cont in enumerate(contours):
        area = cv2.contourArea (cont)
        if (area > 300):
            x,y,w,h = cv2.boundingRect (cont)
            frame = cv2.rectangle (frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText (frame, 'green', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
    #cv2.drawContours (frame, contours, -1, (0,255,0), 2

    cv2.imshow ('Frame', frame)
    cv2.imshow ('Mask', mask)
    cv2.imshow ('Output', res)

    if (cv2.waitKey (1) & 0xFF == ord ('q')):
        cap.release ()
        cv2.destroyAllWindows ()
        break

