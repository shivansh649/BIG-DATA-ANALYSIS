# Simulated CSV content (no need to read a file)
csv_data = """id,name,age,department,salary
1,John,34,Engineering,75000
2,Sara,29,Marketing,62000
3,Tom,41,Engineering,80000
4,Anna,25,Marketing,60000
5,James,31,HR,50000
6,Laura,30,Engineering,72000"""

# Step 1: Convert CSV string into list of dictionaries
lines = csv_data.strip().split("\n")
headers = lines[0].strip().split(",")

data = []
for line in lines[1:]:
    values = line.strip().split(",")
    row = dict(zip(headers, values))
    row["age"] = int(row["age"])
    row["salary"] = int(row["salary"])
    data.append(row)

# Step 2: Show full dataset
print("Original Dataset:")
for row in data:
    print(row)

# Step 3: Filter Engineering Department
engineering = [row for row in data if row["department"] == "Engineering"]
print("\nEngineering Department:")
for row in engineering:
    print(row)

# Step 4: Average Salary by Department
department_salaries = {}
department_counts = {}

for row in data:
    dept = row["department"]
    salary = row["salary"]
    if dept not in department_salaries:
        department_salaries[dept] = 0
        department_counts[dept] = 0
    department_salaries[dept] += salary
    department_counts[dept] += 1

print("\nAverage Salary by Department:")
for dept in department_salaries:
    avg = department_salaries[dept] / department_counts[dept]
    print(f"{dept}: {avg:.2f}")

# Step 5: Employee count per department
print("\nEmployee Count by Department:")
for dept in department_counts:
    print(f"{dept}: {department_counts[dept]}")
