


import tkinter as tk
from tkinter import messagebox
import getpass
import os

# Kullanıcı adı ve şifre
USERNAME = "mege"
PASSWORD = "0199"

# Kullanıcı kimlik doğrulama fonksiyonu
def authenticate(username_input, password_input):
    if username_input == USERNAME and password_input == PASSWORD:
        return True
    else:
        return False

# Giriş ekranı fonksiyonu
def login():
    # Kullanıcı adı ve şifreyi al
    username = entry_username.get("mege")
    password = entry_password.get("0199")

    # Kimlik doğrulama işlemi
    if authenticate(username, password):
        messagebox.showinfo("Başarılı", "Giriş Başarılı!")
        root.destroy()  # Giriş başarılıysa, pencereyi kapat
        # Burada başka bir işlem veya pencere açılabilir
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

# Şifreyi gizleme
def hide_password(event):
    entry_password.config(show="*")

# GUI penceresini oluştur
root = tk.Tk()
root.title("Kullanıcı Giriş Ekranı")
root.geometry("400x300")

# Kullanıcı adı etiketi ve kutusu
label_username = tk.Label(root, text="Kullanıcı Adı:")
label_username.pack(pady=10)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

# Şifre etiketi ve kutusu
label_password = tk.Label(root, text="Şifre:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)
entry_password.bind("<FocusIn>", hide_password)

# Giriş butonu
login_button = tk.Button(root, text="Giriş Yap", command=lambda: login())
login_button.pack(pady=20)

# Çıkış butonu
exit_button = tk.Button(root, text="Çıkış", command=root.quit)
exit_button.pack(pady=5)

# Pencereyi çalıştır
root.mainloop()
