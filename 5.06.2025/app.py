from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'boris_is_dev'  # Необходимо для работы сессий

# База данных пользователей (в реальном приложении следует использовать БД)
users = {
    "admin": {
        "password": "Linux",
        "role": "Администратор"
    },
    "user1": {
        "password": "Microsoft",
        "role": "Пользователь"
    },
    "user2": {
        "password": "Apple",
        "role": "Пользователь"
    }
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Проверка пользователя
        if username in users and users[username]['password'] == password:
            # Успешный вход
            session['username'] = username
            session['role'] = users[username]['role']
            flash(f'Привет, {username}! Вы вошли как: {users[username]["role"]}', 'success')
            return redirect(url_for('welcome'))
        else:
            # Неправильные данные
            flash('Неправильный логин или пароль, попробуйте еще раз', 'error')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', 
                         username=session['username'], 
                         role=session['role'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)