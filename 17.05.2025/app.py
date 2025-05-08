from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def eternal_question():
    if request.method == 'POST':
        answer = request.form['answer']
        return f'your answer is {answer}'
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)