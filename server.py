from flask import Flask, render_template, session, redirect, request, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Beautiful!'

@app.route('/number_please')
def number_please():
	return "{}".format(random.randint(1,20))

@app.route('/complement/<name>/<int:number>')
def complement_ely(name, number):
	if name.title() =='Ely':
		return render_template("hello.html", name=name, number=number)
	else:
		return render_template("not_ely.html", name=name)

@app.route('/welcome/<name>')
def welcome(name):
	if not 'is_ely' in session:
		session['is_ely']=name.title() == "Ely"
	return render_template("welcome.html", is_ely=session['is_ely'])

@app.route('/logout')
def logout():
	session.clear()
	return "Loged Out! Bye"

# @app.route('/secret/<password>')
# def show_secret_word(password):
# 	if not 'is_loggedin' in session:
# 		session['is_loggedin']= password =='bananaPie'
# 	return render_template("secret.html", my_session=session['is_loggedin'])

@app.route('/register', methods=['POST','GET'])
def process_registration():
	if request.method == 'POST':
		fname = request.form.get('fname')
		lname = request.form.get('lname')
		gender = request.form.get('gender')
		edu_level = request.form.get('edu_level')
		phone = request.form.get('phone')
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		return render_template("profile.html",fname=fname, lname=lname, gender=gender, edu_level=edu_level, phone=phone,email=email, username=username)
	return render_template("register.html")

	
@app.route('/login', methods=['POST','GET'])
def process_login():
	if request.method == 'POST':
		password = request.form.get('pass')
		username = request.form.get('username')
		if username == 'elykips' and password == 'elykips+254':
			return render_template("success.html", username=username, password=password)
		else:
			return render_template("login.html")



@app.route('/session')
def check_session():
	if not 'is_loggedin' in session:
		return redirect("https://yahoo.com")
	else:
		return render_template("session.html", my_session=session['is_loggedin'])

@app.route('/table/<int:rows>/<int:columns>', methods=['GET'])
def generate_table(rows, columns):
	return render_template("table.html", columns=columns,rows=rows)



app.secret_key = b'\x1b\x98\xa8y\xd4`\xb3\xa2\x0e\xecp\x027\xa0"\xefOcu\xfba\xe5\xad\x03'

