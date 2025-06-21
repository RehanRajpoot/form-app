from flask import Flask, render_template, request, flash
from config import DATABASE_URI
from models import db, FormSubmission

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Needed for flash messages

db.init_app(app)

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

            flash('✅ Form submitted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'❌ Error: {str(e)}', 'error')

    return render_template('form.html')

# (Optional) View all submissions route
@app.route('/submissions')
def submissions():
    all_data = FormSubmission.query.all()
    return render_template('submissions.html', data=all_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)