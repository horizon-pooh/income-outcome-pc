import tkinter as tk
from tkinter import messagebox
import TKFN

def show_pw():
    global show_password
    if show_password:
        password_entry.config(show="")
        show_password = False
    else:
        password_entry.config(show="*")
        show_password = True
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        try:
            root.destroy()
            TKFN.income_outcome()
            messagebox.showinfo('ลงชื่อ','ลงทะเบียนสำเร็จแล้ว')
        
        except:
            messagebox.showinfo('ดาวน์โหลดล้มเหลว','โปรดทำในครั้งต่อไป')
    else:
            messagebox.showerror("การเข้าสู่ระบบล้มเหลว", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

root = tk.Tk()
root.title("เข้าสู่ระบบ")

show_password = False

username_label = tk.Label(root, text="Username:" , width=20 , font=30 , pady=5 , wraplength=200)
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:" , width=20 , font=30 , pady=5)
password_label.pack()
password_entry = tk.Entry(root, show="*")  
password_entry.pack()

toggle_button = tk.Button(root, text="Show/Hide Password", command=show_pw )
toggle_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=login , width=20 , bg="light blue")
login_button.pack()

root.mainloop()
