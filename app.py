from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store form submissions in memory
form_data_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    form_data_list.append({
        'name': name,
        'email': email,
        'message': message
    })

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', submissions=form_data_list)

if __name__ == '__main__':
    app.run(debug=True)
