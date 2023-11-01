#lists

# Create a list of students, where each student is a tuple of (name, age, grade)
students = [('Alice', 12, 7), ('Bob', 13, 8), ('Carol', 14, 9)]

# Create a dictionary to store the average grade for each student
student_grades = {}

# Iterate over the students list and calculate the average grade for each student
for student in students:
    name, age, grade = student
    student_grades[name] = grade

# Calculate the overall average grade for all students
overall_average_grade = sum(student_grades.values()) / len(student_grades)

# Print the average grade for each student and the overall average grade
for name, grade in student_grades.items():
    print(f'{name}: {grade}')
print(f'Overall average grade: {overall_average_grade}')

# Create a dictionary of countries, where each country is a tuple of (name, population, capital)
countries = {
    'Nigeria': (211,400,708, 'Abuja'),
    'United States': (333,282,642, 'Washington, D.C.'),
    'China': (1,453,569,000, 'Beijing'),
}

# Create a list to store the population of each country
country_populations = []

# Iterate over the countries dictionary and add the population of each country to the list
for country, stats in countries.items():
    population = stats[1]
    country_populations.append(population)

# Sort the list of country populations in descending order
country_populations.sort(reverse=True)

# Print the top 10 countries with the largest population
print('Top 10 countries with the largest population:')
for i in range(10):
    print(f'{i + 1}. {country_populations[i]} people')
