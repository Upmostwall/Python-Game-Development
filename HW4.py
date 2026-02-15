import random

marks = [random.randint(0, 100) for _ in range(20)]

low_marks = [m for m in marks if m <= 30]
mid_marks = [m for m in marks if 31 <= m <= 69]
high_marks = [m for m in marks if m >= 70]

print("All Marks:", marks)
print("Marks <= 30:", low_marks)
print("Marks 31 to 69:", mid_marks)
print("Marks >= 70:", high_marks)
