import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox

# --- ตั้งค่าไฟล์ข้อมูล ---
DATA_FILE = "student_tasks.csv"

# --- โครงสร้างหน้าต่าง GUIหลัก ---
class TaskCheckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ระบบเช็กการส่งงานนักเรียน (Task Check)")
        self.root.geometry("750x500")

        # --- ส่วนป้อนข้อมูล (Input Frame) ---
        input_frame = ttk.LabelFrame(root, text=" เพิ่ม/เช็กรายการงาน ", padding=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(input_frame, text="ชื่อ-สกุล นักเรียน:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_student = ttk.Entry(input_frame, width=20)
        self.ent_student.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="ชื่อภาระงาน:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_task = ttk.Entry(input_frame, width=20)
        self.ent_task.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="สถานะการส่ง:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_status = ttk.Combobox(input_frame, values=["ส่งแล้ว", "ส่งช้า", "ยังไม่ส่ง"], state="readonly", width=17)
        self.combo_status.current(0)
        self.combo_status.grid(row=1, column=1, padx=5, pady=5)

        btn_add = ttk.Button(input_frame, text="บันทึกข้อมูล", command=self.add_record)
        btn_add.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

        # --- ตารางแสดงรายการ (Table / Treeview) ---
        table_frame = ttk.Frame(root, padding=10)
        table_frame.pack(fill="both", expand=True)

        columns = ("student", "task", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        self.tree.heading("student", text="ชื่อ-สกุล นักเรียน")
        self.tree.heading("task", text="ภาระงาน / ชิ้นงาน")
        self.tree.heading("status", text="สถานะการส่ง")

        self.tree.column("student", width=250)
        self.tree.column("task", width=250)
        self.tree.column("status", width=150, anchor="center")

        # Scrollbar สำหรับตาราง
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- ส่วนจัดการรายการ (Action Bar) ---
        action_frame = ttk.Frame(root, padding=10)
        action_frame.pack(fill="x")

        btn_delete = ttk.Button(action_frame, text="ลบรายการที่เลือก", command=self.delete_record)
        btn_delete.pack(side="right", padx=5)

        # โหลดข้อมูลเก่าถ้ามี
        self.load_data()

    # --- ฟังก์ชันการทำงานต่างๆ ---
    def add_record(self):
        student = self.ent_student.get().strip()
        task = self.ent_task.get().strip()
        status = self.combo_status.get()

        if not student or not task:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณากรอกชื่อนักเรียนและชื่อภาระงานให้ครบถ้วน")
            return

        # บันทึกลงตาราง GUI
        self.tree.insert("", "end", values=(student, task, status))
        self.save_data()

        # ล้างช่องป้อนข้อมูล
        self.ent_student.delete(0, tk.END)
        self.ent_task.delete(0, tk.END)

    def delete_record(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกรายการที่ต้องการลบในตาราง")
            return
        
        for item in selected_item:
            self.tree.delete(item)
        self.save_data()

    def save_data(self):
        # บันทึกข้อมูลทั้งหมดลงไฟล์ CSV
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            for child in self.tree.get_children():
                writer.writerow(self.tree.item(child)["values"])

    def load_data(self):
        # โหลดข้อมูลจากไฟล์ CSV ถ้าไฟล์มีอยู่จริง
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, mode="r", encoding="utf-8-sig") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.tree.insert("", "end", values=row)

# --- เรียกใช้งานโปรแกรม ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskCheckApp(root)
    root.mainloop()