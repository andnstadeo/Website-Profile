from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle(): 
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0.0))
        area = 3.14159*radius**2
    return render_template('circle.html', area=area)  

@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    area = None
    if request.method =='POST':
        base = float(request.form.get('base', 0.0))
        height = float(request.form.get('height', 0.0))
        area = 0.5*base*height
    return render_template('triangle.html', area=area)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works', methods=['GET', 'POST'])
def works():
    operation = None
    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == "touppercase":
            return redirect(url_for('touppercase'))
        elif operation == "triangle":
            return redirect(url_for('triangle'))
        elif operation == "circle":
            return redirect(url_for('circle'))
    return render_template('works.html')

if __name__ == '__main__':
    app.run(debug = True)
