from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ✅ Replace this with your actual RDS credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Formdb:Dodadon143?@form-rds-db.cpsy8aqykw31.eu-north-1.rds.amazonaws.com:5432/Formdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# ✅ Create table (run once)
with app.app_context():
    db.create_all()

# ✅ Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    new_entry = Submission(name=name, email=email)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    all_submissions = Submission.query.all()
    return render_template('dashboard.html', submissions=all_submissions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
