from flask import Flask, render_template, request, json
app = Flask(__name__)

import motorController

#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
#import time
#import atexit

# create a default object, no changes to I2C address or frequency
#mh = Adafruit_MotorHAT(addr=0x60)

param = []
drinkName = ""
drinkSize = ""

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	
	if request.method == 'POST':
		param = request.json
		if param != None:
			drinkName = param.get('name')
			drinkSize = param.get('size')

			mixDrink(drinkName, drinkSize)

	return render_template('index.html', error=error)

@app.route('/process', methods=['GET', 'POST'])
def process():
	return render_template('process.html')

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
	print "run mixer: %s, %s" %(name, size)
	mixDrink()
	os.system("motorController.py")
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def romCoke(size):
	print "rom and coke"
	mixDrink()
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def ginTonic(size):
	print "gin and tonic"
	mixDrink()
	#myMotor.setSpeed(255)
	#myMotor.run(Adafruit_MotorHAT.FORWARD)
	#time.sleep(5.0)

def fantaVodka(size):
	print "fanta and vodka"
	mixDrink()
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
