import socket
import threading
import sqlite3
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
import logging
from datetime import datetime

HOST = '127.0.0.1'
PORT = 9095

KEY = b'X9QIf45mAvNpEFCOk1Npe-UdboSK07KGZXEmGUqRLTA='
cipher = Fernet(KEY)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

ph = PasswordHasher()

# Security logging setup
logging.basicConfig(
    filename='security.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Database setup
conn = sqlite3.connect("users.db", check_same_thread=False)
conn.execute("PRAGMA journal_mode=WAL;")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

# Logs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def log_security_event(username, action, client_ip=None, details=None):
    """Log security events to both file and database"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

   
    log_message = f"User: {username} | Action: {action}"
    if client_ip:
        log_message += f" | IP: {client_ip}"
    if details:
        log_message += f" | Details: {details}"

    if action in ['LOGIN_FAILED_NO_USER', 'LOGIN_FAILED_WRONG_PASSWORD', 'REGISTER_FAILED_USER_EXISTS']:
        logging.warning(log_message)
    else:
        logging.info(log_message)

    
    cursor.execute(
        "INSERT INTO logs (username, action) VALUES (?, ?)",
        (username, action)
    )
    conn.commit()



def log_event(username, action):
    log_security_event(username, action)


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle(client, username, client_ip):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break

            print(f"{username} (encrypted): {message}")  # ✅ ADD THIS LINE

            broadcast(message)

        except:
            break

    if client in clients:
        clients.remove(client)

    log_security_event(username, "LEFT_CHAT", client_ip, "User disconnected from chat")
    print(f"{username} disconnected")  # optional but useful

    client.close()


def authenticate(client):
    client_ip = client.getpeername()[0]  # Get client IP address

    while True:
        try:
            encrypted_data = client.recv(1024)
            data = cipher.decrypt(encrypted_data).decode('utf-8')

            action, username, password = data.split("||")

            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            # REGISTER
            if action == "REGISTER":
                if result is not None:
                    log_security_event(username, "REGISTER_FAILED_USER_EXISTS", client_ip, "Username already exists")
                    client.send(cipher.encrypt("USER_EXISTS".encode()))
                else:
                    hashed_password = ph.hash(password)
                    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
                    conn.commit()

                    log_security_event(username, "REGISTER_SUCCESS", client_ip, "New user registration")
                    client.send(cipher.encrypt("REGISTER_SUCCESS".encode()))
                    return username

            # LOGIN
            elif action == "LOGIN":
                if result is None:
                    log_security_event(username, "LOGIN_FAILED_NO_USER", client_ip, "User does not exist")
                    client.send(cipher.encrypt("NO_USER".encode()))
                else:
                    try:
                        ph.verify(result[0], password)

                        log_security_event(username, "LOGIN_SUCCESS", client_ip, "Successful authentication")
                        client.send(cipher.encrypt("LOGIN_SUCCESS".encode()))
                        return username

                    except:
                        log_security_event(username, "LOGIN_FAILED_WRONG_PASSWORD", client_ip, "Incorrect password")
                        client.send(cipher.encrypt("WRONG_PASSWORD".encode()))

        except Exception as e:
            log_security_event("UNKNOWN", "AUTH_ERROR", client_ip, f"Authentication error: {str(e)}")
            print("AUTH ERROR:", e)
            client.close()
            return None


def receive():
    while True:
        client, address = server.accept()
        client_ip = address[0]
        print(f"[NEW CONNECTION] {address}")

        username = authenticate(client)
        if username:
            print(f"[AUTH SUCCESS] {username}")
            log_security_event(username, "JOIN_CHAT", client_ip, "User joined chat room")
        else:
            print(f"[AUTH FAILED] {address}")
            log_security_event("UNKNOWN", "CONNECTION_FAILED", client_ip, "Failed authentication attempt")

        if username:
            clients.append(client)

            broadcast(f"{username} joined the chat!".encode('utf-8'))
            client.send("Connected to server!".encode('utf-8'))

            thread = threading.Thread(target=handle, args=(client, username, client_ip))
            thread.start()
        else:
            client.close()


print("Server is running...")
receive()