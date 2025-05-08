from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get['name']
        return f'Hello, {name}'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)