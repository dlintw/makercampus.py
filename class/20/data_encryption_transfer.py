from cryptography.fernet import Fernet
import socket

# 生成密鑰並保存到文件
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# 加載密鑰
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)

# 加密數據
text = "這是一段需要加密和傳輸的數據。"
encrypted_text = cipher.encrypt(text.encode())

# 創建伺服器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print("伺服器正在監聽...")

# 等待客戶端連接
client_socket, addr = server_socket.accept()
print(f"客戶端 {addr} 已連接")

# 傳輸加密數據
client_socket.sendall(encrypted_text)
print("加密數據已傳輸")

# 關閉連接
client_socket.close()
server_socket.close()

# 創建客戶端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# 接收加密數據
received_encrypted_text = client_socket.recv(1024)
print(f"接收到的加密數據：{received_encrypted_text}")

# 解密數據
decrypted_text = cipher.decrypt(received_encrypted_text).decode()
print(f"解密後的數據：{decrypted_text}")

# 關閉連接
client_socket.close()
