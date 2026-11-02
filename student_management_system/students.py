class Student:
    all_Students=[]
    
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no =roll_no
        self.marks =marks
        
    @classmethod
    def add_student(cls,student):
        name=input("Enter student name:")
        roll_no=input("Enter student roll number:")
        marks=input("Enter student marks:")
        student=cls(name,roll_no,marks)
        cls.all_Students.append(student)
        return student
    
    @classmethod
    def update_student_marks(cls):
        roll_no=input("Enter student roll number to update marks:")
        new_marks=input("Enter new marks:")
        for student in cls.all_Students:
            if student.roll_no==roll_no:
                student.marks=new_marks
                return f"{student.name}'s marks updated successfully"
        return "student not found"
    
    @classmethod
    def show_all_students(cls):
        if not cls.all_Students:
            return "No student founds"
        for student in cls.all_Students:
            print(f"\nName: {student.name}")
            print(f"Roll Number: {student.roll_no}")
            print(f"Marks: {student.marks}")
            