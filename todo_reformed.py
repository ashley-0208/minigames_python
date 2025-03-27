import tkinter as tk
from tkinter import messagebox, ttk


class ModernTODO(tk.Tk):
    def __init__(self):
        super().__init__()

        # تنظیمات پنجره
        self.title("To-Do List پیشرفته")
        self.geometry("500x600")
        self.configure(bg="#f0f0f0")

        # استایل کلی
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50")
        style.configure("TEntry", padding=8)

        # فریم اصلی
        main_frame = tk.Frame(self, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # عنوان
        tk.Label(main_frame, text="لیست کارهای من", font=("Arial", 16),
                 bg="#f0f0f0", fg="#333").pack(pady=10)

        # کادر ورود کار جدید
        entry_frame = tk.Frame(main_frame, bg="#f0f0f0")
        entry_frame.pack(fill=tk.X, pady=10)

        self.task_entry = ttk.Entry(entry_frame, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        add_btn = ttk.Button(entry_frame, text="➕ اضافه کن", command=self.add_task)
        add_btn.pack(side=tk.RIGHT)

        # لیست کارها
        self.list_frame = tk.Frame(main_frame, bg="#f0f0f0")
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        # نمونه اولیه
        self.tasks = []

        # رویدادها
        self.task_entry.bind("<Return>", lambda e: self.add_task())

    def add_task(self):
        task_text = self.task_entry.get().strip()

        if task_text:
            task_frame = tk.Frame(self.list_frame, bg="white", bd=1, relief=tk.RIDGE, padx=10, pady=5)
            task_frame.pack(fill=tk.X, pady=5)

            tk.Label(task_frame, text=task_text, font=("Arial", 12),
                     bg="white", anchor="w").pack(side=tk.LEFT, fill=tk.X, expand=True)

            del_btn = tk.Button(task_frame, text="❌", font=("Arial", 10),
                                bg="#ff4444", fg="white", bd=0,
                                command=lambda f=task_frame: self.remove_task(f))
            del_btn.pack(side=tk.RIGHT)

            self.tasks.append(task_frame)
            self.task_entry.delete(0, tk.END)

    def remove_task(self, task_frame):
        if messagebox.askyesno("حذف کار", "آیا مطمئنید می‌خواهید این کار را حذف کنید؟"):
            task_frame.destroy()
            self.tasks.remove(task_frame)


if __name__ == "__main__":
    app = ModernTODO()
    app.mainloop()