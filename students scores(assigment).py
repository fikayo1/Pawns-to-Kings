def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_student_data():
    students = []
    num_students = int(input("How many students do you want to enter? "))
    
    for i in range(num_students):
        print(f"\nStudent {i + 1}:")
        while True:
            name = input("Enter name: ").strip()
            if name:
                break
            else:
                print("Name cannot be empty.")
        
        score = get_valid_score()
        students.append({"name": name, "score": score})
    
    return students

def calculate_stats(students):
    scores = [student["score"] for student in students]
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def display_results(students):
    # Sort students by score descending
    students_sorted = sorted(students, key=lambda x: x["score"], reverse=True)
    
    print("\nStudent Grades:")
    for student in students_sorted:
        grade = assign_grade(student["score"])
        print(f"{student['name']}: Score = {student['score']}, Grade = {grade}")
    
    highest, lowest, average = calculate_stats(students)
    print(f"\nHighest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Average Score: {average:.2f}")

# Main program execution
students = get_student_data()
display_results(students)
