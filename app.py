import sqlite3
from tkinter import Tk, ttk, messagebox, StringVar, Entry, Label, Button, Canvas

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        self.create_header()

        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.roll_number_var = StringVar()
        self.exam_roll_var = StringVar()
        self.registration_number_var = StringVar()
        self.batch_var = StringVar()
        self.session_var = StringVar()
        self.blood_group_var = StringVar()

        Label(root, text="First Name:", font=("Arial", 12)).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.first_name_var, font=("Arial", 12)).grid(row=1, column=1, padx=20, pady=10)

        Label(root, text="Last Name:", font=("Arial", 12)).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.last_name_var, font=("Arial", 12)).grid(row=2, column=1, padx=20, pady=10)

        Label(root, text="Email:", font=("Arial", 12)).grid(row=3, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.email_var, font=("Arial", 12)).grid(row=3, column=1, padx=20, pady=10)

        Label(root, text="Phone Number:", font=("Arial", 12)).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.phone_var, font=("Arial", 12)).grid(row=4, column=1, padx=20, pady=10)

        Label(root, text="Roll Number:", font=("Arial", 12)).grid(row=5, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.roll_number_var, font=("Arial", 12)).grid(row=5, column=1, padx=20, pady=10)

        Label(root, text="Exam Roll:", font=("Arial", 12)).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.exam_roll_var, font=("Arial", 12)).grid(row=6, column=1, padx=20, pady=10)

        Label(root, text="Registration Number:", font=("Arial", 12)).grid(row=7, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.registration_number_var, font=("Arial", 12)).grid(row=7, column=1, padx=20, pady=10)

        Label(root, text="Batch:", font=("Arial", 12)).grid(row=8, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.batch_var, font=("Arial", 12)).grid(row=8, column=1, padx=20, pady=10)

        Label(root, text="Session:", font=("Arial", 12)).grid(row=9, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.session_var, font=("Arial", 12)).grid(row=9, column=1, padx=20, pady=10)

        Label(root, text="Blood Group:", font=("Arial", 12)).grid(row=10, column=0, padx=20, pady=10, sticky="w")
        Entry(root, textvariable=self.blood_group_var, font=("Arial", 12)).grid(row=10, column=1, padx=20, pady=10)

        Button(root, text="Add Student", command=self.add_student, font=("Arial", 12), relief="raised", padx=10, pady=5).grid(row=11, column=0, padx=20, pady=20)
        Button(root, text="View Students", command=self.view_students, font=("Arial", 12), relief="raised", padx=10, pady=5).grid(row=11, column=1, padx=20, pady=20)

        self.student_tree = ttk.Treeview(root, columns=("ID", "First Name", "Last Name", "Email", "Phone", "Roll Number", "Exam Roll", "Registration Number", "Batch", "Session", "Blood Group"), show="headings", height=6)
        self.student_tree.grid(row=12, column=0, columnspan=2, padx=20, pady=10)

        for col in ("ID", "First Name", "Last Name", "Email", "Phone", "Roll Number", "Exam Roll", "Registration Number", "Batch", "Session", "Blood Group"):
            self.student_tree.heading(col, text=col, anchor="w")
            self.student_tree.column(col, width=120, anchor="w")

        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        style.map("Treeview", background=[('selected', '#C8E6C9')])

    def create_header(self):
        header_frame = Canvas(self.root, bg="#2196F3", height=50)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        header_frame.create_text(400, 25, text="Student Management System", font=("Arial", 18, "bold"), fill="white")

    def add_student(self):
        first_name = self.first_name_var.get()
        last_name = self.last_name_var.get()
        email = self.email_var.get()
        phone = self.phone_var.get()
        roll_number = self.roll_number_var.get()
        exam_roll = self.exam_roll_var.get()
        registration_number = self.registration_number_var.get()
        batch = self.batch_var.get()
        session = self.session_var.get()
        blood_group = self.blood_group_var.get()

        if not all([first_name, last_name, email, phone, roll_number, exam_roll, registration_number, batch, session, blood_group]):
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        try:
            c.execute('''
                INSERT INTO students (first_name, last_name, email, phone_number, roll_number, exam_roll, registration_number, batch, session, blood_group)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, last_name, email, phone, roll_number, exam_roll, registration_number, batch, session, blood_group))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email must be unique!")
        finally:
            conn.close()

    def view_students(self):
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students")
        for row in c.fetchall():
            self.student_tree.insert("", "end", values=row)
        conn.close()

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementApp(root)
    root.mainloop()
