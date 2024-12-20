students_scores = {
    "Alice": (85, 92, 78),
    "Bob": (90, 88, 84),
    "Charlie": (80, 79, 93)
}

def calculate_average(scores):
    return sum(scores) / len(scores)

def print_averages():
    for student, scores in students_scores.items():
        avg_score = calculate_average(scores)
        print(f"{student}'s average score: {avg_score:.2f}")

def find_highest_avg():
    highest_avg = -1
    top_student = ""
    for student, scores in students_scores.items():
        avg_score = calculate_average(scores)
        if avg_score > highest_avg:
            highest_avg = avg_score
            top_student = student
    return top_student, highest_avg

print_averages()

top_student, highest_avg = find_highest_avg()
print(f"\nStudent with the highest average score is {top_student} with an average of {highest_avg:.2f}.")
