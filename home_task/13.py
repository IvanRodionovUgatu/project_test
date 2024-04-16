students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

# Способ 1
all_people = students.union(employees)
print("Все люди:", all_people)

# Способ 2
all_people = students | employees
print("Все люди:", all_people)


# Способ 1
both = students.intersection(employees)
print("Учатся и работают:", both)

# Способ 2
both = students & employees
print("Учатся и работают:", both)

# Способ 1
only_employees = employees - students
print("Только работают:", only_employees)

# Способ 2
only_employees = employees.difference(students)
print("Только работают:", only_employees)


# Способ 1
either_or = students.symmetric_difference(employees)
print("Учится или работает (но не оба):", either_or)

# Способ 2
either_or = students ^ employees
print("Учится или работает (но не оба):", either_or)

