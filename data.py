import sqlite3

def get_db():
  db = sqlite3.connect('database.db')
  db.row_factory = sqlite3.Row
  
  return db

def add_user(name, email):
  db = get_db()
  cursor = db.cursor()
  
  cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                (name, email))
  db.commit()
  
  return cursor.lastrowid
  
def edit_user(user_id, name, email):
  db = get_db()
  cursor = db.cursor()
  
  cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', 
                 (name, email, user_id))
  db.commit()
  
def get_user(user_id):
  db = get_db()
  cursor = db.cursor()
  
  cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
  return cursor.fetchone()

def get_all_users():
  db = get_db()
  return db.execute('SELECT * FROM users').fetchall()

def delete_user(user_id):
  db = get_db()
  db.execute('DELETE FROM users WHERE id = ?', (user_id,))
  db.commit()