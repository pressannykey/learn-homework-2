"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def compare_strings(str1, str2):
        if type(str1) is not str or type(str2) is not str:
            return 0
        if str1 == str2:
            return 1
        else:
            if len(str1) > len(str2):
                return 2
            elif str2 == 'learn':
                return 3
        return 'Не знаю, что с этим делать:('

    print(compare_strings('1', 2))
    print(compare_strings('', ''))
    print(compare_strings('looong', 'learn'))
    print(compare_strings('test', 'learn'))
    print(compare_strings('note', 'tone'))


if __name__ == "__main__":
    main()
