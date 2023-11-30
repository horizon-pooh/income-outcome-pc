import tkinter as tk
from tkinter import messagebox
import TKSignup
import TKIncome

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

    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                s_username, s_password, _ = line.strip().split(",")
                if username == s_username and password == s_password:
                    root.destroy()
                    TKIncome.income_outcome()
                    messagebox.showinfo('ลงชื่อ', 'Login สำเร็จ')
                    return

        messagebox.showerror("การเข้าสู่ระบบล้มเหลว", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

    except FileNotFoundError:
        messagebox.showerror("ไฟล์ไม่พบ", "ไฟล์ user_data.txt ไม่พบ")
    except Exception as e:
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {str(e)}")


root = tk.Tk()
root.geometry("400x300")
root.title("เข้าสู่ระบบ")

show_password = False

username_label = tk.Label(root, text="Username", width=20, pady=5, font=("Helvetica", 15,"bold"))
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password", width=20, pady=5, font=("Helvetica", 15,"bold"))
password_label.pack()
password_entry = tk.Entry(root, show="*")  
password_entry.pack()

toggle_button = tk.Button(root, text="Show/Hide Password", command=show_pw, font=("Helvetica", 10,"bold"), bg="moccasin")
toggle_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=login, width=15, font=("Helvetica", 10,"bold"), bg="light blue")
login_button.pack(pady=5)

tsignup_button = tk.Button(root, text="Sign up", command=TKSignup.Signup, width=15, bg="light green", font=("Helvetica", 10,"bold"))
tsignup_button.pack()

root.mainloop()
