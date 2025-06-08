# Хранение данных и сессии

**Установка модулей**:

Открыв консоль (Windows) используйте данную комманду:

```bash
    pip install Flask flask-session
```

**Начиная работу**:

```
Структура приложения:

   ПРОВОДНИК

   static ---¬
        style.css (опционально)
   templates ---¬
        index.html
   app.py
```

**Код**:

В качестве примера, приведу простое веб-приложение для заметок

Импортируем модуль в ***app.py***:

```python
from flask import Flask, session, redirect, url_for, request, render_template_string
```

Далее инициализируем приложение и задаем ***шифрование данных***:

```python
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'your_secret_key' # Ключ для шифрования данных вместо 'your_secret_key' должен стоять более надежный
```

Также, назначим **настройки** ***сессии***:

```python
app.config['SESSION_TYPE'] = 'filesystem'
session.init_app(app)
```

Создаем ***роутеры*** (пути):

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        session['user_id'] = user_id  # Сохраняем ID пользователя в сессии
        return redirect(url_for('index'))
    return render_template_string('index.html')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    notes = session.get('notes', [])
    return render_template_string(user_id=user_id, notes=notes)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Удаляем ID пользователя из сессии
    return redirect(url_for('login'))
```

Подробнее про методы **GET** и **POST** я расписал в ***'flask-wtf.md'***

Последний штрих, добавим **точку входа** в приложение:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML-код**:

В качестве примера, frontend будет выглядить так:

```HTML
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Заметки-Онлайн</title>
</head>
<h1>Заметки</h1>
    <ul>
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
    </ul>
    <form method="post" action="/add">
        <input type="text" name="note" placeholder="Добавьте заметку" required>
        <button type="submit">Добавить</button>
    </form>
```
