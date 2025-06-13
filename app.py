from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Console output
        print("📥 New Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        # Optional: Save to file (local storage)
        with open('submissions.txt', 'a') as f:
            f.write(f"{name} | {email} | {message}\n")

        return '✅ Thank you for your submission!'

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
