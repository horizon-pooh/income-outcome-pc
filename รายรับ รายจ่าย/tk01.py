import tkinter as tk

class income_outcome(tk.Tk):
    def __init__(x):
        super().__init__()
        x.title("ระบบติดตามรายได้และค่าใช้จ่าย")
        
        x.รายได้ = 0.0
        x.ค่าใช้จ่าย = 0.0
        x.หน้าต่าง()
    
    def เพิ่มรายได้(x):
        จำนวน = float(x.รายได้_entry.get())
        x.รายได้ += จำนวน
        x.รายได้_label.config(text=f"รายได้ทั้งหมด: {x.รายได้} บาท")
        x.รายได้_entry.delete(0, 'end')  

    def เพิ่มค่าใช้จ่าย(x):
        จำนวน = float(x.ค่าใช้จ่าย_entry.get())
        x.ค่าใช้จ่าย += จำนวน
        x.ค่าใช้จ่าย_label.config(text=f"ค่าใช้จ่ายทั้งหมด: {x.ค่าใช้จ่าย} บาท")
        x.ค่าใช้จ่าย_entry.delete(0, 'end') 

    def แสดงสรุป(x):
        รายได้สุทธิ = x.รายได้ - x.ค่าใช้จ่าย
        x.รายได้สุทธิ_label.config(text=f"รายได้สุทธิ: {รายได้สุทธิ} บาท")

    def หน้าต่าง(x):

        x.รายได้_label = tk.Label(x, text="รายได้ทั้งหมด: 0.0 บาท")
        x.รายได้_label.pack()
        x.รายได้_entry = tk.Entry(x)
        x.รายได้_entry.pack()
        x.รายได้_button = tk.Button(x, text="เพิ่มรายได้", command=x.เพิ่มรายได้)
        x.รายได้_button.pack()

        x.ค่าใช้จ่าย_label = tk.Label(x, text="ค่าใช้จ่ายทั้งหมด: 0.0 บาท")
        x.ค่าใช้จ่าย_label.pack()
        x.ค่าใช้จ่าย_entry = tk.Entry(x)
        x.ค่าใช้จ่าย_entry.pack()
        x.ค่าใช้จ่าย_button = tk.Button(x, text="เพิ่มค่าใช้จ่าย", command=x.เพิ่มค่าใช้จ่าย)
        x.ค่าใช้จ่าย_button.pack()

        x.รายได้สุทธิ_label = tk.Label(x, text="รายได้สุทธิ: 0.0 บาท")
        x.รายได้สุทธิ_label.pack()
        x.แสดงสรุป_button = tk.Button(x, text="แสดงสรุป", command=x.แสดงสรุป)
        x.แสดงสรุป_button.pack()

if __name__ == '__main__':
    app = income_outcome()
    app.mainloop()
