# Experiment No. 5
# Calculate average grade of students

n = int(input("Enter the number of students: "))

total_class = 0

for i in range(1, n + 1):
    print("\nEnter marks for Student", i)

    total = 0

    for j in range(1, 6):
        marks = float(input("Enter marks for Test " + str(j) + ": "))
        total = total + marks

    average = total / 5

    print("Average of Student", i, "=", average)

    total_class = total_class + average

overall_average = total_class / n

print("\nOverall Average of the Class =", overall_average)