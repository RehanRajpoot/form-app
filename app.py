from flask import Flask, render_template, request
from models import db, FormSubmission

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dodadon143?@localhost:5432/formdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Automatically create tables on startup
with app.app_context():
    db.create_all()

# Route for the form
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            data = FormSubmission(name=name, email=email, message=message)
            db.session.add(data)
            db.session.commit()

            return "Form submitted successfully!"
        except Exception as e:
            db.session.rollback()
            return f"Error saving data: {e}"
    return render_template('form.html')

# Optional route to view submissions
@app.route('/submissions')
def submissions():
    all_data = FormSubmission.query.all()
    return render_template('submissions.html', data=all_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
