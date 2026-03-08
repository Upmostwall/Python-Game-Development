import time
student_info = {
    "MATH": "A",
    "SCIENCE": "B",
    "ENGLISH": "A",
    "HISTORY": "C",
    "ART": "B"
}

while True:
  
    print("---Student Profile---")
    print("1. View Student Grades")
    print("2. Update Student Grades")
    print("3. Delete Student Grades")
    print("4. Add New Subject")
    print("5. Exit Profile")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        if student_info:
            for subject, grade in student_info.items():
                print(subject, ":", grade)
        else:
            print("No subjects available.")     
        
    elif choice == 2:
        subject = input("Enter the subject name to update: ").upper()
        if subject in student_info:
            grade = input("Enter the new grade: ").upper()
            student_info[subject] = grade
            print("Grade updated successfully.")
        else:
            print("Subject not found in profile.")

    elif choice == 3:
        subject = input("Enter the subject name to delete: ").upper()
        if subject in student_info:
            del student_info[subject]
            print("Subject deleted successfully.")
        else:
            print("Subject not found in profile.")
    
    elif choice == 4:
        new_subject = input("Enter the new subject name: ").upper()
        grade = input("Enter the grade for the new subject: ").upper()
        student_info[new_subject] = grade
        print("New subject added successfully.")

    elif choice == 5:
        print("Exiting the profile...")
        time.sleep(2)
        print("Profile exited successfully.")
        break

    else:
        print("Invalid choice. Please select a valid option (1-5).")