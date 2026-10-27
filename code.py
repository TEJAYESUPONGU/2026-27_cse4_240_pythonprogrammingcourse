
n = int(input("Enter number of students: "))
eligible = []
ineligible = []

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Name: ")
    aggregate = float(input("Aggregate percentage: "))

    subjects = list(map(float, input(
        "Enter marks in 3 subjects: "
    ).split()))

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    if (aggregate >= 75 and len(subjects) == 3
            and min(subjects) >= 50
            and attendance >= 75 and income <= 250000):

        eligible.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "min_subject": min(subjects),
            "income": income
        })
    else:
        ineligible.append(name)

# Sort by aggregate, attendance, subject marks, then income
eligible.sort(key=lambda s: (
    -s["aggregate"],
    -s["attendance"],
    -s["min_subject"],
    s["income"]
))

print("\n--- Scholarship Ranking ---")
if eligible:
    for rank, s in enumerate(eligible, 1):
        print(rank, s["name"],
              "- Aggregate:", s["aggregate"],
              "Attendance:", s["attendance"])
else:
    print("No eligible students.")

print("\nIneligible students:", ineligible)

