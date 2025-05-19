from flask import Flask, app, request, g, redirect, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('my_products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,    
            username TEXT  NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()



@app.route('/')
def index():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def login():
    if request.method == ['GET', 'POST']:
        username = request.form['Name_input']
        email = request.form['Email_input']
        password = request.form['Password_input']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                       (username, email, password))
        conn.commit()
        conn.close()

        return f"User {username} authorized"
    
    return render_template('index.html')

if __name__ == ('__main__'):
    init_db()
    app.run(debug=True)