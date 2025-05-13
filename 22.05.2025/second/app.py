from flask import Flask, render_template

app = Flask(__name__)


users = ["Билл", "Пол", "Иван", "Джон", "Майкл"]
products = [
    {"name": "Ноутбук HP", "price": 45000},
    {"name": "Телефон Nokia Lumia", "price": 25000},
    {"name": "Колонки Genius", "price": 5000},
    {"name": "Клавиатура Mitsumi", "price": 3000},
]

@app.route('/')
def index():
    return render_template('index.html', is_logged_in=True, user_role="admin")

@app.route('/users')
def show_users():
    return render_template('users.html', users=users, products=products)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)