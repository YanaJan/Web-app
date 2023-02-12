group = [
    {
        "name": "Мячина",
        "surname": "Лада",
        "exam": ["Алгебра", "ВВИТ", "Философия"],
        "mark": [4, 4, 4]
    },
    {
        "name": "Землякова",
        "surname": "Вероника",
        "exam": ["Алгебра", "ВВИТ", "Философия"],
        "mark": [5, 5, 4]
    },
    {
        "name": "Дедова",
        "surname": "Мария",
        "exam": ["Алгебра", "ВВИТ", "Философия"],
        "mark": [3, 3, 3]
    },
    {
        "name": "Бомко",
        "surname": "Алиса",
        "exam": ["Алгебра", "ВВИТ", "Философия"],
        "mark": [5, 5, 4]
    }
]

score = int(input("Input average score:"))


def filt(score):
    print(u'Name'.ljust(15), u'Surname'.ljust(20), u'Average score')
    for student in group:
        if sum(student['mark'])/len(student['mark']) >= score:
            print(student['name'].ljust(15), student['surname'].ljust(20), int(sum(student['mark'])/len(student['mark'])))


filt(score)