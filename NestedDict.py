students = {
    "Student1": {
        "Name": "Alex",
        "Age": 15,
        "Class": "10th Grade",
        "Marks": {
            "Math": 88,
            "Science": 97,
        }
    },
    
    "Student2": {
        "Name": "Bob",
        "Age": 14,
        "Class": "9th Grade",
        "Marks": {
            "Math": 89,
            "Science": 78,
        }
    }
}

for student_id, students_data in students.items():
    print("Student ID:", student_id)
    print("Name:", students_data["Name"])
    print("Age:", students_data["Age"])
    print("Class:", students_data["Class"])
    
    print("Marks:")
    for subject, score in students_data["Marks"].items():
        print(" ",subject,":",score)
    print()

for student_data in students.values():
    student_data["Marks"]["Maths"] += 5

print("/nUpdated Math Marks after bonus")
for student_id, students_data in students.items():
    print(student_id, "->", students_data["Marks"]["Maths"])