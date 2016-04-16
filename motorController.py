from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

print "FILE RUN"

mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(3)

def mixTheDrink():
	myMotor.setSpeed(255)
	myMotor.run(Adafruit_MotorHAT.RELEASE);

	myMotor.run(Adafruit_MotorHAT.FORWARD)
	time.sleep(5.0)
	turnOffMotors()

mixTheDrink()