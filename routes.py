from flask import Flask, render_template, request
from calculator import operation
import smtplib
import os

# env variables
EMAIL_I=os.environ.get("EMAIL_I",None)

# Declare the app
app = Flask(__name__,
			static_folder='img')

# Start an app route which is '/'
@app.route('/')
# Declare the main function
def home():
	return render_template('home.html', user='mario', title='home')

#Create the link from the webpage subscribe to the webpage form
@app.route('/form', methods=["POST"])
# Declare the main function
def form():
	email = request.form.get("email")

	message = "You have subscribed to the Newsletter of the course ENE425 Sustainable Energy taught at NHH in 2021. "
	#message = "Link to the newsletter: (https: // indd.adobe.com / view / e4780b8e-b6b6-4508-95a4-0bdf3d351b6f)."
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("mblazquezdepaz@gmail.com", EMAIL_I)
	server.sendmail("mblazquezdepaz@gmail.com", email, message)

	return render_template('form.html', title='form', email=email)

# Start an app route which is '/chapter1'
@app.route('/teachers')
# Declare the main function
def chapter1():
	return render_template('teachers.html', title='ch1')

# Start an app route which is '/app'
@app.route('/app_calculator')
# Declare the main function
def app_calculator():
	return render_template('app_calculator.html', title='app_calculator')

# App Calculator
@app.route('/send1', methods=['POST'])
def send(sum=sum):
	num1 = request.form.get("num1")
	num2 = request.form.get("num2")
	oper_name = request.form.get("operation")

	num1 = float(num1)
	num2 = float(num2)
	if oper_name == "add":
		oper_result = num1 + num2
	elif oper_name == "subtract":
		oper_result = num1 - num2
	elif oper_name == "multiply":
		oper_result = num1 * num2
	elif oper_name == "divide":
		oper_result = num1 / num2

	return render_template ('app_calculator.html', sum=oper_result)

# App web
@app.route('/app_web')
def app_web():
	return render_template('app_web.html', title='app web')

# App web. Module 1.
@app.route('/app_web/module1')
def app_web_module1():
	return render_template('app_web_module1.html', check="20")



# App web. Module 1. Exercise 1.
# App web. Module 1.
@app.route('/app_web/module1/ex1', methods=['POST'])
def app_web_module1_ex1():
	if request.method == "POST":
		num1 = request.form.get("num1")

		num1 = float(num1)
		if num1 == 2:
			answ = "right"
		else:
			answ = "wrong"
		return render_template('app_web_module1.html', check=answ)
	else:
		return render_template('app_web_module1.html', check="20")


if __name__ == "__main__":
    app.run()
