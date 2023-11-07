import tkinter as tk

รายได้ = 0
ค่าใช้จ่าย = 0

class income_outcome():

def เพิ่มรายได้():
    global รายได้
    จำนวน = float(รายได้_entry.get())
    รายได้ += จำนวน
    รายได้_label.config(text=f"รายได้ทั้งหมด: {รายได้} บาท")
    รายได้_entry.delete(0, 'end') 

def เพิ่มค่าใช้จ่าย():
    global ค่าใช้จ่าย
    จำนวน = float(ค่าใช้จ่าย_entry.get())
    ค่าใช้จ่าย += จำนวน
    ค่าใช้จ่าย_label.config(text=f"ค่าใช้จ่ายทั้งหมด: {ค่าใช้จ่าย} บาท")
    ค่าใช้จ่าย_entry.delete(0, 'end')  

def แสดงสรุป():
    รายได้สุทธิ = รายได้ - ค่าใช้จ่าย
    รายได้สุทธิ_label.config(text=f"รายได้สุทธิ: {รายได้สุทธิ} บาท")

window = tk.Tk()
window.title("ระบบติดตามรายได้และค่าใช้จ่าย")

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
