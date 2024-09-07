
students = [('Alex',10),('Georgie',56),('Maria',18)]
def sort_by_age(students):
    return sorted(students,key=lambda person:person[1])

sorted_students = sort_by_age(students)
print(sorted_students)