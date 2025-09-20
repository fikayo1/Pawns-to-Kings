def get_grade(score):
    """Return letter grade based on score."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 46:
        return "D"
            return "C"
    elif score >= 40:
        return "E"
    else:
        return "F"


def main():
    students = []
    
    # Ask number of students
    while True:
        try:
            n = int(input("How many students do you want to enter? "))
            if n > 0:
                break
            else:
                print("Number of students must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Collect student data
    for i in range(n):
        while True:
            name = input(f"Enter name for student {i+1}: ").strip()
            if name != "":
                break
            else:
                print("Name cannot be empty.")
        
        while True:
            try:
                score = float(input(f"Enter score for {name} (0 - 100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        students.append({"name": name, "score": score})
    
    # Calculate highest, lowest, and average scores
    scores = [s["score"] for s in students]
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    print("\n--- Results ---")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Average Score: {average:.2f}\n")
    
    # Print each student's grade
    for s in students:
        print(f"{s['name']} - Score: {s['score']} - Grade: {get_grade(s['score'])}")


if _name_ == "_main_":
    main()