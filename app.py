from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

tasks = []

# Home page shows tasks
@app.route('/')
def home():
    return render_template_string('''
        <h2>To-Do List</h2>
        <form action="/add" method="post">
            <input name="task" placeholder="Enter a task" required>
            <button type="submit">Add</button>
        </form>
        <ul>
            {% for task in tasks %}
                <li>{{ loop.index }}. {{ task }}</li>
            {% endfor %}
        </ul>
    ''', tasks=tasks)

# Handle adding new task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
