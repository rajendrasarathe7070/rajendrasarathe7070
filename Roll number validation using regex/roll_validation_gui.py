import re
import tkinter as tk
from tkinter import messagebox

def validate_roll():
    roll = entry.get().upper()

    pattern = r'^(\d{2})(\d{3})([A-Z0-9]{3})(\d{3})$'
    match = re.match(pattern, roll)

    if not match:
        messagebox.showerror("Error", "Invalid Roll Number Format!")
        return

    year, college_code, branch_code, student_no = match.groups()

    # Branch dictionary
    branches = {
        "C04": "Computer Science",
        "I03": "Information Technology",
        "E02": "Electronics and Communication",
        "M01": "Mechanical Engineering",
        "C00": "Civil Engineering"
    }
    name={"043":"Rajendra sarathe "}

    # College dictionary
    colleges = {
        "233": "RGPV Main Campus",
        "234": "LNCT Bhopal",
        "235": "TIT College",
        "236": "Oriental College"
    }

    branch_name = branches.get(branch_code)
    college_name = colleges.get(college_code)
    name_st=name.get(student_no)

    if branch_name and college_name:
        result = (
            f"Valid Roll Number\n\n"
            f"Name	 =  	 {name_st}\n"
            f"Admission Year   :	 20{year}\n"
            f"Branch                : 	 {branch_name}\n"
            f"College                 :	 {college_name}\n"
            f"Student No.        : 	{student_no}"
        )
        messagebox.showinfo("Result", result)
    else:
        messagebox.showerror("Error", "Invalid branch or college code!")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Roll Number Validator")
root.geometry("350x200")
root.resizable(False ,False)
#root.colour("green")
label = tk.Label(root, text="Enter Roll Number:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

btn = tk.Button(root, text="Submit", font=("Arial", 10), command=validate_roll)
btn.pack(pady=15)

root.mainloop()