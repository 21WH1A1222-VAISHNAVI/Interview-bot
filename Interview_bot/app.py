from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_url_path='/static')

# SQLite database setup
conn = sqlite3.connect('interview_data.db')
cursor = conn.cursor()

# Create a table to store interviewee information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        university TEXT NOT NULL,
        major TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        university = request.form['university']
        major = request.form['major']
        email = request.form['email']

        # Store the form data in the database
        conn = sqlite3.connect('interview_data.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO interviews (name, university, major, email)
            VALUES (?, ?, ?, ?)
        ''', (name, university, major, email))

        conn.commit()
        conn.close()

        return render_template('submission.html', name=name)

@app.route('/interview')
def interview():
    # Here, you can generate and fetch questions from a database or any other source
    # For now, I'll provide a simple list of questions
    questions = [
        "Introduce yourself",
        
        "Explain the concept of Object-Oriented Programming.",

        "What is the difference between HTTP and HTTPS?",
        # Add more questions as needed
    ]

    return render_template('interview.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
