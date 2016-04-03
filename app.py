from flask import Flask, render_template, request, json
app = Flask(__name__)

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

# Run Python code to select desired drink and size
def mixDrink(name, size):
	print "run mixer: %s, %s" %(name, size)

def romCoke(size):
	print "rom and coke"

def ginTonic(size):
	print "gin and tonic"

def fantaVodka(size):
	print "fanta and vodka"

if __name__ == '__main__':
	app.run(debug=True)
