from flask import Flask, request

app = Flask(__name__)

def fibo(n):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

@app.route("/") # To make our site available at URL:port/
def send_fibo():
	try:	
		return str(fibo(int(request.args['n']))) # getting the argument called "n", converting it to the string, giving it to fibo and converting the output to a string
	except ValueError:
		return "Please use a number as the 'n' argument"
