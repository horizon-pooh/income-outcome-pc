import tkinter as tk
from tkinter import messagebox
import tk01

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        try:
            tk01.income_outcome()
            messagebox.showinfo('ลงชื่อ','ลงทะเบียนสำเร็จแล้ว')
        
        except:
            messagebox.showinfo('ดาวน์โหลดล้มเหลว','โปรดทำในครั้งต่อไป')
    else:
            messagebox.showerror("การเข้าสู่ระบบล้มเหลว", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

root = tk.Tk()
root.title("เข้าสู่ระบบ")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
