# Формы с помощью Flask-WTF

**Установка модулей**:

Открыв консоль (Windows) используйте данную комманду:

```bash
    pip install Flask Flask-WTF WTForms
```

**Начиная работу**:

```
Структура приложения:

   ПРОВОДНИК

   static ---¬
        style.css (опционально)
   templates ---¬
        register.html
   app.py
   forms.py
```

**Код**:

Импортируем все необходимые модули в наш ***app.py***:

```python
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
```

Далее инициализируем приложение и задаем ***шифрование данных***:

```python
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'your_secret_key' # Ключ для шифрования данных вместо 'your_secret_key' должен стоять более надежный
```

Создаем ***роутеры*** (пути):

```python
@app.route('/register', methods=['GET', 'POST']) # '/register' это путь к нашей странице и функции register
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Здесь вы можете обработать данные формы, например, сохранить их в базу данных
        return redirect(url_for('success')) # Перенаправляет на '/success'
    return render_template('register.html', form=form) # render_template отвечает за отображение страницы. 'register.html' это то, что он будет отображать

@app.route('/success') # Этот путь будет показан в тот момент, когда пользователь зарегистрируется
def success():
    return 'Registration successful!' # Сообщение о том, что всё удалось 
```

Необходимо пояснить про ***методы***.

Все методы выполняют операции с **сервером**

|   Метод    |       GET        |       POST       |
| ---------- | ---------------- | ---------------- |
|    Цель    | получение данных | отправка данных  |
|  Передача  |    через URL     |  в теле запроса  |
|   Лимиты   |    длина URL     |    отсутствуют   |

Главный аспект в методах на ***безопасность***.

GET - Данные открыты для всех пользователей в адресной строке, поэтому не должны быть использованы для передачи конфиденциальной информации.

POST - Данные запросов не видны в адресной строке, что делает их более безопасными для передачи конфиденциальной информации.
