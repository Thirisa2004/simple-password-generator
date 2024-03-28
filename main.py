from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=10):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['length'])
        generated_password = generate_password(password_length)
        return render_template('index.html', password=generated_password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
