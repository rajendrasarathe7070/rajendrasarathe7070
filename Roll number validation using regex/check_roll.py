import re
def validate_roll(roll):
    # Regular expression for roll number pattern
    pattern = r'^(\d{2})(\d{3})([A-Z0-9]{3})(\d{3})$'
    match = re.match(pattern, roll)

    if not match:
        print("Invalid Roll Number Format!")
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

    # College dictionary
    colleges = {
        "233": "RGPV Main Campus",
        "234": "LNCT Bhopal",
        "235": "TIT College",
        "236": "Oriental College"
    }

    # Validate branch and college codes
    branch_name = branches.get(branch_code, None)
    college_name = colleges.get(college_code, None)
    if branch_name and college_name:
        print="Valid Roll Number"
        print=f"Admission Year : 20{year}"
        print=f"Branch         : {branch_name}"
        print=f"College        : {college_name}"
        print=f"Student No.    : {student_no}"
    else: 
        print("Invalid branch or college code!")

# ---- Main Code ----
roll= input("Enter roll number: ").upper()
validate_roll(roll)