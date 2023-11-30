import tkinter as tk
from tkinter import messagebox

class Signup():
    userlist = []

    def __init__(a):
        a.main_signup = tk.Tk()
        a.main_signup.title("ลงทะเบียน")
        a.main_signup.geometry("220x130")

        tk.Label(a.main_signup, text ="Sign Up",font = ("Helvetica", 15, "bold")).grid(row=0, column=1)
        tk.Label(a.main_signup, text ="Username",font = ("Helvetica", 10, "bold")).grid(row=1)
        tk.Label(a.main_signup, text ="Password",font = ("Helvetica", 10, "bold")).grid(row=2)
        tk.Label(a.main_signup, text ="Email",font = ("Helvetica", 10, "bold")).grid(row=3)

        a.einput = tk.Entry(a.main_signup)
        a.uinput = tk.Entry(a.main_signup)
        a.winput = tk.Entry(a.main_signup)

        a.einput.grid(row=1, column=1)
        a.uinput.grid(row=2, column=1)
        a.winput.grid(row=3, column=1)

        button1 = tk.Button(a.main_signup, width=7, height=1, text="สมัคร", command=a.makeuser, bg = "light green", font=("Helvetica", 10, "bold"))
        button1.grid(row=4, column=1, padx=3, pady=3)
        button2 = tk.Button(a.main_signup, width=7, height=1, text="ออก", command=a.main_signup.destroy, bg = "red", font=("Helvetica", 10, "bold"))
        button2.grid(row=4, column=0, padx=3, pady=3)

    def makeuser(a):
        user_info = [a.einput.get(), a.uinput.get(), a.winput.get()]
        Signup.userlist.append(user_info)
        print(Signup.userlist)

        file_path = 'user_data.txt'
        with open(file_path, 'a') as file:
            file.write(','.join(user_info) + '\n')

        messagebox.showinfo('Sign up', 'คุณได้สร้างรหัสผ่านสำเร็จ')
        a.main_signup.destroy()

if __name__ == '__main__':
    app = Signup()
    tk.mainloop()
