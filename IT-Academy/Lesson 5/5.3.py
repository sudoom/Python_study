student_db = [
    {'surname': 'Ivanov', 'name': 'Ivan', 'gender': 'male', 'age': '21'},
    {'surname': 'Petrov', 'name': 'Ivan', 'gender': 'male', 'age': '31'},
    {'surname': 'Sidorov', 'name': 'Pavel', 'gender': 'male', 'age': '25'},
    {'surname': 'Prokova', 'name': 'Alyona', 'gender': 'female', 'age': '21'},
    {'surname': 'Prokova', 'name': 'Karina', 'gender': 'female', 'age': '20'}
    ]

criteria_inp = input(
    'Enter criteria to search:\n'
    '(if not one , enter !): '
    ).split('!')


def search_stu(database, search):
    criteria = set(search)
    l = []

    for i in range(len(database)):
        student = database[i].copy()
        val = set(student.values())
        if criteria.issubset(val):
            student['id'] = i + 1
            l.append(student)
    return l


def print_search(result_list):
    if result_list:
        for i in result_list:
            print(
                '\nStudent № {id}: {surname} {name} {gender} {age}'.format(**i)
                )
    else:
        print('404')


print_search(search_stu(student_db, criteria_inp))
