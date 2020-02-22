"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    class_scores = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '4b', 'scores': [5, 4, 5, 5, 4, 4]},
        {'school_class': '5a', 'scores': [3, 5, 4, 4, 3]},
        {'school_class': '5b', 'scores': [2, 4, 3, 5, 2]},
        {'school_class': '6a', 'scores': [5, 3, 4, 3, 2, 4]},
        {'school_class': '6b', 'scores': [2, 3, 4, 5, 4]}
    ]

    school_scores_sum = 0
    len_scores = 0

    for cl in class_scores:
        class_scores_sum = 0
        for score in cl['scores']:
            class_scores_sum += score
        len_scores += len(cl['scores'])
        print(
            f"Средняя оценка {cl['school_class']} класса: {class_scores_sum/len(cl['scores'])}")
        school_scores_sum += class_scores_sum

    print(f'Средняя оценка школы: {school_scores_sum/len_scores}')


if __name__ == "__main__":
    main()
