from flask import Flask, render_template, request, redirect, url_for
from db import init_db, add_user, get_all_users
from datetime import datetime

app = Flask(__name__)

# Инициализация БД при старте приложения
init_db()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = int(request.form['age'])
    
    # Валидация данных
    if not name or not email:
        return "Имя и email обязательны для заполнения", 400
    
    if age < 1 or age > 120:
        return "Возраст должен быть между 1 и 120", 400
    
    if '@' not in email:
        return "Некорректный email", 400
    
    # Добавление пользователя в БД
    if add_user(name, email, age):
        return redirect(url_for('success'))
    else:
        return "Пользователь с таким email уже существует", 400

@app.route('/success')
def success():
    return "Данные успешно сохранены!"

@app.route('/users')
def show_users():
    users = get_all_users()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)