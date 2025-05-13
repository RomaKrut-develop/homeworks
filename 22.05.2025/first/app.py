from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def voprosi():
    if request.method == 'GET':
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        gender = request.form["gender"]
        hobby = request.form["hobby"]
        city = request.form["city"]
    else:
        render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)