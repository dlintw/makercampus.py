import sqlite3

conn = sqlite3.connect('user_management.db')

# 創建表
with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

def create_user(name, age):
    with conn:
        conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    print("用戶創建成功")

def get_user(name):
    cursor = conn.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()
    if user:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    else:
        print("用戶不存在")

def update_user(name, new_age):
    with conn:
        conn.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
    print("用戶信息更新成功")

def delete_user(name):
    with conn:
        conn.execute("DELETE FROM users WHERE name = ?", (name,))
    print("用戶刪除成功")

# 操作用戶
create_user("Alice", 30)
get_user("Alice")
update_user("Alice", 28)
get_user("Alice")
delete_user("Alice")
get_user("Alice")
