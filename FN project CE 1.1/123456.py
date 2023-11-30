import tkinter as tk

class income_outcome(tk.Tk):
    def __init__(x):
        super().__init__()
        x.title("ระบบติดตามรายได้และค่าใช้จ่าย")
        x.geometry("360x260")
         
        x.รายได้ = 0.0
        x.ค่าใช้จ่าย = 0.0
        x.ประวัติรายได้ = []
        x.ประวัติค่าใช้จ่าย = []
        x.หน้าต่าง()
    
    def เพิ่มรายได้(x):
        จำนวน = float(x.รายได้_entry.get())
        x.รายได้ += จำนวน
        x.รายได้_label.config(text=f"รายได้ทั้งหมด: {x.รายได้} บาท")
        x.รายได้_entry.delete(0, 'end')  
        x.ประวัติรายได้.append(จำนวน)

    def เพิ่มค่าใช้จ่าย(x):
        จำนวน = float(x.ค่าใช้จ่าย_entry.get())
        รายละเอียด = x.ค่าใช้จ่าย_รายละเอียด_entry.get()  # Added entry for expense details
        x.ค่าใช้จ่าย += จำนวน
        x.ค่าใช้จ่าย_label.config(text=f"ค่าใช้จ่ายทั้งหมด: {x.ค่าใช้จ่าย} บาท")
        x.ค่าใช้จ่าย_รายละเอียด_entry.delete(0, 'end') 
        x.ประวัติค่าใช้จ่าย.append((จำนวน, รายละเอียด))

    def แสดงสรุป(x):
        รายได้สุทธิ = x.รายได้ - x.ค่าใช้จ่าย
        x.รายได้สุทธิ_label.config(text=f"รายได้สุทธิ: {รายได้สุทธิ} บาท")
        x.แสดงประวัติ()

    def แสดงประวัติ(x):
        x.history_window = tk.Toplevel(x)
        x.history_window.title("ประวัติรายได้และค่าใช้จ่าย")

        income_label = tk.Label(x.history_window, text="ประวัติรายได้", font=("Helvetica", 20,"bold"))
        income_label.pack()
        for income in x.ประวัติรายได้:
            income_item = tk.Label(x.history_window, text=f"รายได้: {income} บาท", font=("Helvetica", 15))
            income_item.pack()

        expenses_label = tk.Label(x.history_window, text="ประวัติค่าใช้จ่าย", font=("Helvetica", 20,"bold"))
        expenses_label.pack()
        for expense, description in x.ประวัติค่าใช้จ่าย:
            expense_item = tk.Label(x.history_window, text=f"ค่าใช้จ่าย: {expense} บาท | รายละเอียด: {description}", font=("Helvetica", 15))
            expense_item.pack()
        
    def หน้าต่าง(x):
        x.รายได้_label = tk.Label(x , text="รายได้ทั้งหมด : 0.0 บาท" , font=20 , width=15 )
        x.รายได้_label.pack(pady=5)
        x.รายได้_entry = tk.Entry(x)
        x.รายได้_entry.pack()
        x.รายได้_button = tk.Button(x, text="เพิ่มรายได้", command=x.เพิ่มรายได้ ,   bg="light pink")
        x.รายได้_button.pack(pady=10)

        x.ค่าใช้จ่าย_label = tk.Label(x, text="ค่าใช้จ่ายทั้งหมด : 0.0 บาท")
        x.ค่าใช้จ่าย_label.pack()
        x.ค่าใช้จ่าย_entry = tk.Entry(x)
        x.ค่าใช้จ่าย_entry.pack()
        x.ค่าใช้จ่าย_รายละเอียด_label = tk.Label(x, text="รายละเอียดค่าใช้จ่าย:")
        x.ค่าใช้จ่าย_รายละเอียด_label.pack()
        x.ค่าใช้จ่าย_รายละเอียด_entry = tk.Entry(x)
        x.ค่าใช้จ่าย_รายละเอียด_entry.pack()
        x.ค่าใช้จ่าย_button = tk.Button(x, text="เพิ่มค่าใช้จ่าย", command=x.เพิ่มค่าใช้จ่าย)
        x.ค่าใช้จ่าย_button.pack()

        x.รายได้สุทธิ_label = tk.Label(x, text="รายได้สุทธิ : 0.0 บาท")
        x.รายได้สุทธิ_label.pack()
        x.แสดงสรุป_button = tk.Button(x, text="แสดงสรุป", command=x.แสดงสรุป)
        x.แสดงสรุป_button.pack()

if __name__ == '__main__':
    app = income_outcome()
    app.mainloop()
