import RPi.GPIO as GPIO


# GPIO Pins for Motor Driver Inputs
Motor1A = 24 #physical pin 18
Motor1B = 23 #physical pin 16
Motor1E = 25 #phusical pin 22

def setup():
	GPIO.setmode(GPIO.BCM)		# set to RaspberryPi Broadcom chip-specific pin numbers
	GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

def loop():
	# Going forwards
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)



def destroy():
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
    		loop()
  	except KeyboardInterrupt:
		destroy()
