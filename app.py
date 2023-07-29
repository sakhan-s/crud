from flask import Flask, render_template, request, redirect, url_for

import data

app = Flask(__name__)

@app.route('/')
def index():
  users = data.get_all_users()
  return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])  
def add_user():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    
    user_id = data.add_user(name, email)
    return redirect(url_for('index'))

  return render_template('add_user.html')

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    
    data.edit_user(user_id, name, email) 
    return redirect(url_for('index'))

  user = data.get_user(user_id)
  return render_template('edit_user.html', user=user)
  
@app.route('/delete/<int:user_id>', methods=['POST'])  
def delete_user(user_id):
  data.delete_user(user_id)
  return redirect(url_for('index'))

def init_db():
  db = data.get_db()
  print("Initializing DB...")
  # проверяем, есть ли записи в таблице users
  count = db.execute('SELECT COUNT(*) FROM users').fetchone()[0]

  if count == 0:
    # если записей нет - добавляем тестовые данные
    print('Creating test data...')

    db.execute('INSERT INTO users (name, email) VALUES (?, ?)',
               ('John Doe', 'john@example.com'))
    db.execute('INSERT INTO users (name, email) VALUES (?, ?)',
               ('Jane Doe', 'jane@example.com'))

    print('Test data created')

  else:
    print('DB already initialized')

# вызываем эту функцию в скрипте
init_db()


if __name__ == '__main__':
  app.run()