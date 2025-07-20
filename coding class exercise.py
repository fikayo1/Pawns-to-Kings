#Question 1:print each students name and scores
students = [["Alice",85], ["Bob",78], ["Clara",92], ["David",65]]
print("students_scores") 
for student in students:
    name, scores = student
    print(f"{name}:{scores}")
# Question 2:  Print only the names of students who scored above 80
for student in students:
    name, scores = student
    if scores > 80:
        print(name)
# Question 3: Find out the average of their scores
def average(scores):
    return sum(scores) / len(scores)
scores = [85, 78, 92, 65]
avg = average(scores)
print("Average of scores: ", avg)
    