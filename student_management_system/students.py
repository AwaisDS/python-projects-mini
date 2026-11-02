import pandas as pd
from pathlib import Path

class Student:
    csv_path = Path(__file__).with_name("students.csv")
    columns = ["Name", "Roll Number", "Marks"]
    
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no =roll_no
        self.marks =marks

    @classmethod
    def ensure_csv(cls):
        if not cls.csv_path.exists() or cls.csv_path.stat().st_size == 0:
            pd.DataFrame(columns=cls.columns).to_csv(cls.csv_path, index=False)
        
    @classmethod
    def add_student(cls):
        cls.ensure_csv()
        name=input("Enter student name:")
        roll_no=input("Enter student roll number:")
        marks=input("Enter student marks:")
        df=pd.DataFrame([{
            "Name": name,
            "Roll Number": roll_no,
            "Marks": marks,
        }], columns=cls.columns)
        df.to_csv(cls.csv_path, mode="a", index=False, header=False)

    @classmethod
    def update_student_marks(cls):
        cls.ensure_csv()
        roll_no=input("Enter student roll number to update marks:")
        new_marks=input("Enter new marks:")
        df=pd.read_csv(cls.csv_path, dtype={"Roll Number": str, "Marks": str})
        df.loc[df["Roll Number"] == roll_no, "Marks"] = new_marks
        df.to_csv(cls.csv_path, index=False)

    
    @classmethod
    def show_all_students(cls):
        cls.ensure_csv()
        df=pd.read_csv(cls.csv_path, dtype={"Roll Number": str, "Marks": str})
        print(df)
            