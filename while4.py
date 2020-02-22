names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

# не поняла, как и зачем использовать while :(


def find_person(name):
    if name in names:
        print("Валера нашелся!")
    else:
        print("Такого имени нет в списке!")


find_person("Валера")
