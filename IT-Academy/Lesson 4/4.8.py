grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]
sort_grades = sorted(grades, key=lambda x: x[1])
for i, j in enumerate(sort_grades):
    print("Hello {}! Your grade is {}".format(j[0], j[1]))
    i += 1
