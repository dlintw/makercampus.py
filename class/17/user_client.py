import requests

BASE_URL = 'http://localhost:5000/users'

def create_user(user):
    response = requests.post(BASE_URL, json=user)
    if response.status_code == 201:
        print("User created:", response.json())
    else:
        print(f"Failed to create user, status code: {response.status_code}")

def get_users():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to get users, status code: {response.status_code}")

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Failed to get user, status code: {response.status_code}")

def update_user(user_id, user):
    response = requests.put(f"{BASE_URL}/{user_id}", json=user)
    if response.status_code == 200:
        print("User updated:", response.json())
    else:
        print(f"Failed to update user, status code: {response.status_code}")

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 204:
        print("User deleted")
    else:
        print(f"Failed to delete user, status code: {response.status_code}")

# 使用示例
new_user = {'id': 1, 'name': 'Alice', 'age': 30}
create_user(new_user)

get_users()
get_user(1)

updated_user = {'name': 'Alice', 'age': 31}
update_user(1, updated_user)

delete_user(1)
