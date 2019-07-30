from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

#Create an '/add' route here:
@app.route('/add', methods = ['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	
	else:
		student_name = request.form['student_name']
		student_year = request.form['student_year']

		add_student(student_name, student_year)
		return render_template('add.html')

@app.route("/delete/<int:student_id>", methods = ['POST', 'GET'])
def delete_student(student_id):
	delete_student_id(student_id)
	return redirect(url_for('home'))

app.route("/updatelabstatus/<int:student_id>", methods = ['POST', 'GET'])
def update_lab(student_id):
	
	
if __name__ == '__main__':
    app.run(debug=True)
