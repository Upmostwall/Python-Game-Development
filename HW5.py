def create_report_card(name, marks_dict):
    """
    Create a student report card using a tuple.
    
    Args:
        name: Student's name
        marks_dict: Dictionary with subjects and their marks
    
    Returns:
        Tuple containing student information
    """
    report_card = (name, marks_dict)
    return report_card


def display_report_card(report_card):
    """Display the student report card."""
    name, marks = report_card
    
    print("\n" + "=" * 40)
    print("STUDENT REPORT CARD")
    print("=" * 40)
    print("Name: " + name)
    print("\nMarks:")
    print("-" * 40)
    
    total = 0
    for subject, mark in marks.items():
        print(subject + ": " + str(mark))
        total += mark
    
    average = total / len(marks)
    print("-" * 40)
    print("Total: " + str(total))
    print("Average: " + format(average, ".2f"))
    print("=" * 40 + "\n")


student1 = create_report_card("John Doe", {
    "Math": 85,
    "English": 78,
    "Science": 92,
    "History": 88
})

display_report_card(student1)
