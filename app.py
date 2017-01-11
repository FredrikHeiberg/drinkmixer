from flask import Flask, render_template, request, json, session, redirect
#from flask.ext.session import Session
from flask_session import Session
app = Flask(__name__)

#from motorController import mixTheDrink, mixingWater
import threading
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
#import time
#import atexit

# create a default object, no changes to I2C address or frequency
#mh = Adafruit_MotorHAT(addr=0x60)

SESSION_TYPE = 'redis'
Session(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	drinkName = request.form['name']
	drinkSize = request.form['size']
	mixTime = mixDrink(drinkName, drinkSize)
	return render_template('process.html', mixTime=mixTime)


# @app.route('/mix', methods=['GET'])
# def mix():
# 	# Get value from JS
# 	drinkParams = request.args.get('drinkOrder')
# 	test = request.args.get('#romCoke')
# 	drinkParams = ['romCoke', 400]

# 	# Run mixing with specified values
# 	mixDrink(drinkParams[0],drinkParams[1])
# 	print drinkParams

# 	return render_template('index.html')

#myMotor = mh.getMotor(3)

# Run Python code to select desired drink and size
def mixDrink(name, size):
	print name
	mixTime = 0
	if name == 'romCoke':
		mixTime = 2
	elif name == 'ginTonic':
		mixTime = 10
	elif name == 'vodkaFanta':
		mixTime = 2

	#mixTheDrink(name, size)
	#mixingWater()
	t = threading.Thread()
	if name == 'romCoke':
		t = threading.Thread(target=mixingWater, args=(name, size, mixTime))
		#mixingWater(name, size, mixTime)
	elif name == 'ginTonic':
		t = threading.Thread(target=mixTheDrink, args=(name, size, mixTime))
		#mixTheDrink(name, size, mixTime)
	t.start()
	return mixTime

	#else:
	#	mixTheDrink(name, size)
	#print "run mixer: %s, %s" %(name, size)
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def romCoke(size):
	print "rom and coke"
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def ginTonic(size):
	print "gin and tonic"
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def fantaVodka(size):
	print "fanta and vodka"
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

# recommended for auto-disabling motors on shutdown!
#def turnOffMotors():
#	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
#atexit.register(turnOffMotors)

if __name__ == '__main__':
	app.run(debug=True)
