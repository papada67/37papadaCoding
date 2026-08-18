import json
import os

FILE_NAME = "student_tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_task(tasks):
    title = input("ระบุชื่องาน/วิชา: ")
    due_date = input("กำหนดส่ง (เช่น YYYY-MM-DD): ")
    priority = input("ระดับความสำคัญ (ต่ำ/กลาง/สูง): ")
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "status": "ยังไม่เสร็จ"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ บันทึกงาน '{title}' เรียบร้อยแล้ว!\n")

def list_tasks(tasks):
    if not tasks:
        print("\n📭 ยังไม่มีงานในระบบ\n")
        return
    
    print("\n📋 รายการงานทั้งหมด:")
    print("-" * 50)
    for task in tasks:
        icon = "✅" if task["status"] == "เสร็จแล้ว" else "⏳"
        print(f"[{task['id']}] {icon} {task['title']} | ส่ง: {task['due_date']} | ความสำคัญ: {task['priority']} | สถานะ: {task['status']}")
    print("-" * 50 + "\n")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("ระบุหมายเลขงานที่ทำเสร็จแล้ว (ID): "))
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "เสร็จแล้ว"
                save_tasks(tasks)
                print(f"🎉 อัปเดตงาน '{task['title']}' เป็นเสร็จเรียบร้อย!\n")
                return
        print("❌ ไม่พบหมายเลขอุปกรณ์นี้\n")
    except ValueError:
        print("❌ กรุณากรอกหมายเลขให้ถูกต้อง\n")

def main():
    tasks = load_tasks()
    while True:
        print("=== 📚 ระบบติดตามงานนักเรียน (Python CLI) ===")
        print("1. ดูรายการงานทั้งหมด")
        print("2. เพิ่มงานใหม่")
        print("3. ทำเลื่อนสถานะเป็นเสร็จแล้ว")
        print("4. ออกจากโปรแกรม")
        
        choice = input("เลือกรายการ (1-4): ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("ปิดโปรแกรม สวัสดีครับ 👋")
            break
        else:
            print("❌ ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่\n")

if __name__ == "__main__":
    main()