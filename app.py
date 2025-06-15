from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

submissions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    submissions.append({'name': name, 'email': email})
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', submissions=submissions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

