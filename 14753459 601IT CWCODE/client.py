import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
PORT = 9095
KEY = b'X9QIf45mAvNpEFCOk1Npe-UdboSK07KGZXEmGUqRLTA='
cipher = Fernet(KEY)

BG = "#1e1e2f"
FRAME = "#2c2c3e"
ACCENT = "#4a90e2"
TEXT = "#ffffff"
ENTRY = "#3a3a4f"


class Client:
    def __init__(self):
        self.connect()
        self.login_window()

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

    def login_window(self):
        self.win = tk.Tk()
        self.win.title("Secure Chat")
        self.win.geometry("350x300")
        self.win.configure(bg=BG)

        frame = tk.Frame(self.win, bg=FRAME)
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(frame, text="Secure Chat", bg=FRAME, fg=TEXT,
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(frame, text="Username", bg=FRAME, fg=TEXT).pack()
        self.user_entry = tk.Entry(frame, bg=ENTRY, fg=TEXT, insertbackground="white")
        self.user_entry.pack(pady=5)

        tk.Label(frame, text="Password", bg=FRAME, fg=TEXT).pack()
        self.pass_entry = tk.Entry(frame, show="*", bg=ENTRY, fg=TEXT, insertbackground="white")
        self.pass_entry.pack(pady=5)

        tk.Button(frame, text="Login", bg=ACCENT, fg="white",
                  command=self.login).pack(pady=5)

        tk.Button(frame, text="Register", bg="#5cb85c", fg="white",
                  command=self.register).pack(pady=5)

        self.status = tk.Label(frame, text="", bg=FRAME, fg="red")
        self.status.pack(pady=5)

        self.win.mainloop()

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            self.status.config(text="Fill all fields")
            return

        try:
            data = f"LOGIN||{username}||{password}"
            self.sock.send(cipher.encrypt(data.encode()))

            response = cipher.decrypt(self.sock.recv(1024)).decode()

            if response == "LOGIN_SUCCESS":
                self.nickname = username
                self.win.destroy()
                self.start_chat()
            elif response == "WRONG_PASSWORD":
                self.status.config(text="Wrong password")
            elif response == "NO_USER":
                self.status.config(text="User not found")

        except:
            self.status.config(text="Connection error")
            self.reconnect()

    def register(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            self.status.config(text="Fill all fields")
            return

        try:
            data = f"REGISTER||{username}||{password}"
            self.sock.send(cipher.encrypt(data.encode()))

            response = cipher.decrypt(self.sock.recv(1024)).decode()

            if response == "REGISTER_SUCCESS":
                self.nickname = username
                self.win.destroy()
                self.start_chat()
            elif response == "USER_EXISTS":
                self.status.config(text="Username exists")

        except:
            self.status.config(text="Connection error")
            self.reconnect()

    def reconnect(self):
        try:
            self.sock.close()
        except:
            pass
        self.connect()

    def start_chat(self):
        self.chat = tk.Tk()
        self.chat.title("Chat")
        self.chat.geometry("500x500")
        self.chat.configure(bg=BG)

        tk.Label(self.chat, text=f"Logged in as {self.nickname}",
                 bg=FRAME, fg=TEXT).pack(fill="x")

        self.text_area = scrolledtext.ScrolledText(
            self.chat, bg="#252535", fg=TEXT)
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)
        self.text_area.config(state='disabled')

        bottom = tk.Frame(self.chat, bg=BG)
        bottom.pack(fill="x", padx=10, pady=10)

        self.input = tk.Entry(bottom, bg=ENTRY, fg=TEXT)
        self.input.pack(side="left", expand=True, fill="x", padx=(0, 10))

        tk.Button(bottom, text="Send", bg=ACCENT, fg="white",
                  command=self.send).pack(side="right")

        self.running = True

        threading.Thread(target=self.receive).start()
        self.chat.protocol("WM_DELETE_WINDOW", self.stop)
        self.chat.mainloop()

    def send(self):
        msg = f"{self.nickname}: {self.input.get()}"
        encrypted = cipher.encrypt(msg.encode())
        self.sock.send(encrypted)
        self.input.delete(0, 'end')

    def receive(self):
        while self.running:
            try:
                msg = self.sock.recv(1024)
                try:
                    msg = cipher.decrypt(msg).decode()
                except:
                    msg = msg.decode()

                self.text_area.config(state='normal')
                self.text_area.insert('end', msg + "\n")
                self.text_area.config(state='disabled')
                self.text_area.yview('end')
            except:
                break

    def stop(self):
        self.running = False
        self.sock.close()
        self.chat.destroy()


Client()