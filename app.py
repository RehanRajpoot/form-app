from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ✅ Correct and secure PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dodadon143?@form-rds-db.cpsy8aqykw31.eu-north-1.rds.amazonaws.com:5432/Fromdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Define the table/model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

# ✅ Route: Home / Form
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Route: Submit form
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    new_entry = Submission(name=name, email=email)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('dashboard'))

# ✅ Route: Dashboard to view submissions
@app.route('/dashboard')
def dashboard():
    all_data = Submission.query.all()
    return render_template('dashboard.html', submissions=all_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')