# Авторизация с помощью Flask-Login

**Установка модулей**:

Открыв консоль (Windows) используйте данную комманду:

```bash
    pip install Flask Flask-Login
```

**Начиная работу**:

```
Структура приложения:

   ПРОВОДНИК

   static ---¬
        style.css (опционально)
   templates ---¬
        login.html
   app.py
```

**Код**:

Импортируем все необходимые модули в наш ***app.py***:

```python
from flask import Flask, request, redirect, render_template, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
```

Далее инициализируем приложение и задаем ***шифрование данных***:

```python
app = Flask(__name__) 
app.config = 'your_secret_key' # Стоит учитывать, что 'your_secret_key' просто пример. Всегда используйте надёжные и сложные ключи
```

Также нам необходимо создать логин-менеджер, который будет отвечать за ***установку*** и ***удаление*** **токенов** сессий для пользовательской сессии после **успешной аутентификации**

```python
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
```

Теперь, можем приступить к основному блоку кода:

```python
# Симуляция базы данных пользователей
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

class User(UserMixin): 
    def __init__(self, id):
        self.id = id

@login_manager.user_loader # Стандартный декоратор логин-менеджера
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST']) # Вход в аккаунт
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return 'Неверный логин или пароль'
    return render_template('login.html')

@app.route('/logout') # Отображение страницы когда пользователь выходит из аккаунта
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected') # Если контент закрытый, то можно сделать так. Таким же способом можно добавить условие, что чтобы просмотреть содержимое, нужно авторизоваться
@login_required
def protected():
    return 'Закрытый контент'

if __name__ == '__main__': # Точка входа в приложение
    app.run(debug=True)
```

Подробнее про методы **GET** и **POST** я расписал в ***'flask-wtf.md'***

**HTML-Форма**:

Создайте файл ``templates/login.html`` для формы входа:

В качестве примера, форма будет выглядить так:

```HTML
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вход</title>
</head>
<body>
    <h1>Войдите в систему</h1>
    <form method="post" action="/login">
        <label for="username">Логин:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Войти</button>
    </form>
</body>
</html>
```