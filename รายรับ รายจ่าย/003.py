import tkinter as tk
from tkinter import messagebox

# โค้ดของหน้า Login
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        try:
            messagebox.showinfo('signup', 'successfully sign up')
            # หาก Login สำเร็จ ให้เรียกฟังก์ชันแสดงหน้าหลัก
            show_main_window()
        except:
            messagebox.showinfo('download Failed', 'please do next time')
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# ฟังก์ชันแสดงหน้าหลัก
def show_main_window():
    # ปิดหน้า Login
    login_window.destroy()

    # สร้างหน้าหลัก
    window = tk.Tk()
    window.title("ระบบติดตามรายได้และค่าใช้จ่าย")

    # โค้ดของระบบติดตามรายได้และค่าใช้จ่าย
    รายได้ = 0
    ค่าใช้จ่าย = 0

    def เพิ่มรายได้():
        global รายได้
        จำนวน = float(รายได้_entry.get())
        รายได้ += จำนวน
        รายได้_label.config(text=f"รายได้ทั้งหมด: {รายได้} บาท")
        รายได้_entry.delete(0, 'end')  # Clear the input field

    def เพิ่มค่าใช้จ่าย():
        global ค่าใช้จ่าย
        จำนวน = float(ค่าใช้จ่าย_entry.get())
        ค่าใช้จ่าย += จำนวน
        ค่าใช้จ่าย_label.config(text=f"ค่าใช้จ่ายทั้งหมด: {ค่าใช้จ่าย} บาท")
        ค่าใช้จ่าย_entry.delete(0, 'end')  # Clear the input field

    def แสดงสรุป():
        รายได้สุทธิ = รายได้ - ค่าใช้จ่าย
        รายได้สุทธิ_label.config(text=f"รายได้สุทธิ: {รายได้สุทธิ} บาท")

    รายได้_label = tk.Label(window, text="รายได้ทั้งหมด: 0.0 บาท")
    รายได้_label.pack()
    รายได้_entry = tk.Entry(window)
    รายได้_entry.pack()
    รายได้_button = tk.Button(window, text="เพิ่มรายได้", command=เพิ่มรายได้)
    รายได้_button.pack()

    ค่าใช้จ่าย_label = tk.Label(window, text="ค่าใช้จ่ายทั้งหมด: 0.0 บาท")
    ค่าใช้จ่าย_label.pack()
    ค่าใช้จ่าย_entry = tk.Entry(window)
    ค่าใช้จ่าย_entry.pack()
    ค่าใช้จ่าย_button = tk.Button(window, text="เพิ่มค่าใช้จ่าย", command=เพิ่มค่าใช้จ่าย)
    ค่าใช้จ่าย_button.pack()

    รายได้สุทธิ_label = tk.Label(window, text="รายได้สุทธิ: 0.0 บาท")
    รายได้สุทธิ_label.pack()
    แสดงสรุป_button = tk.Button(window, text="แสดงสรุป", command=แสดงสรุป)
    แสดงสรุป_button.pack()

    window.mainloop()

# สร้างหน้า Login
login_window = tk.Tk()
login_window.title("Login")

username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=check_login)
login_button.pack()

login_window.mainloop()
