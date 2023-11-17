import tkinter as tk

class income_outcome(tk.Tk):
    def __init__(x):
        super().__init__()
        x.title("ระบบติดตามรายได้และค่าใช้จ่าย")
        
        x.รายได้ = 0.0
        x.ค่าใช้จ่าย = 0.0
        x.ประวัติรายได้ = []
        x.ประวัติค่าใช้จ่าย = []
        x.หน้าต่าง()
    
    def เพิ่มรายได้(x):
        จำนวน = float(x.รายได้_entry.get())
        x.รายได้ += จำนวน
        x.รายได้_label.config(text=f"รายได้ทั้งหมด: {x.รายได้} บาท", font=("Helvetica", 20,"bold"))
        x.รายได้_entry.delete(0, 'end')  

        x.ประวัติรายได้.append(จำนวน)

    def เพิ่มค่าใช้จ่าย(x):
        จำนวน = float(x.ค่าใช้จ่าย_entry.get())
        x.ค่าใช้จ่าย += จำนวน
        x.ค่าใช้จ่าย_label.config(text=f"ค่าใช้จ่ายทั้งหมด: {x.ค่าใช้จ่าย} บาท", font=("Helvetica", 20,"bold"))
        x.ค่าใช้จ่าย_entry.delete(0, 'end')

        x.ประวัติค่าใช้จ่าย.append(จำนวน)

    def แสดงสรุป(x):
        รายได้สุทธิ = x.รายได้ - x.ค่าใช้จ่าย
        x.รายได้สุทธิ_label.config(text=f"รายได้สุทธิ: {รายได้สุทธิ} บาท", font=("Helvetica", 20,"bold"))

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
        for expense in x.ประวัติค่าใช้จ่าย:
            expense_item = tk.Label(x.history_window, text=f"ค่าใช้จ่าย: {expense} บาท", font=("Helvetica", 15))
            expense_item.pack()

    def หน้าต่าง(x):

        x.รายได้_label = tk.Label(x , text="รายได้ทั้งหมด: 0.0 บาท" , font=("Helvetica", 20, "bold"))
        x.รายได้_label.pack(pady=2.5)
        x.รายได้_entry = tk.Entry(x, font=("Helvetica", 13))
        x.รายได้_entry.pack(pady=2.5)
        x.รายได้_button = tk.Button(x, text="เพิ่มรายได้", command=x.เพิ่มรายได้ , bg="light pink", font=("Helvetica", 13))
        x.รายได้_button.pack(pady=2.5)

        x.ค่าใช้จ่าย_label = tk.Label(x, text="ค่าใช้จ่ายทั้งหมด: 0.0 บาท" , font=("Helvetica", 20, "bold"))
        x.ค่าใช้จ่าย_label.pack(pady=2.5)
        x.ค่าใช้จ่าย_entry = tk.Entry(x, font=("Helvetica", 13))
        x.ค่าใช้จ่าย_entry.pack(pady=2.5)
        x.ค่าใช้จ่าย_button = tk.Button(x, text="เพิ่มค่าใช้จ่าย", command=x.เพิ่มค่าใช้จ่าย , bg="light pink", font=("Helvetica", 13))
        x.ค่าใช้จ่าย_button.pack(pady=2.5)

        x.รายได้สุทธิ_label = tk.Label(x, text="รายได้สุทธิ: 0.0 บาท", font=("Helvetica", 20, "bold"))
        x.รายได้สุทธิ_label.pack(pady=2.5)
        x.แสดงสรุป_button = tk.Button(x, text="แสดงสรุป", command=x.แสดงสรุป, bg="light blue" , font=("Helvetica", 13))
        x.แสดงสรุป_button.pack(pady=2.5)

if __name__ == '__main__':
    app = income_outcome()
    app.mainloop()
