
def get_data(filename):
    '''

    :param filename: имя файла
    :return: вовзращает дату с которой и работают оостальные функции в формате списка списков(матрица)
    '''
    f = open(filename).readlines()
    work_data = list()  # список списков

    for s in f:
        data = s.strip().split("#")
        work_data.append(data)
    return work_data
def delete_dublicates(data):
    '''

    :param data: дата в формате список списков
    :return: возвращается список из ученых которые не воровалои чужие препараты
    '''
    work_data = sort_date(data)
    without_dublicate_data = list() # тут дата без дублей(дуль это ученый который копирует чужой препарат)
    original_names = list()
    for column in work_data:
        if column[1] not in original_names:
            original_names.append(column[1])
            without_dublicate_data.append(column)
    return without_dublicate_data
def get_from_date(data, date):
    '''
    :param data:стандартное для всех функций список списков
    :param date:дата для проверки
    :return:    Эта функция чекает что делали ученые по дате, вовзращает данные в формате
    “Ученый <Фамилия И.О.> создал препарат: <препарат> - <дата>” если ученые работали
    “В этот день ученые отдыхали” если ученые не работали
    '''
    date = date.replace(".", "-")
    temp = date.split("-")
    date = temp[-1] + "-" + temp[1] + "-" + temp[0]
    reses = list() # список найденных данных
    for i in data:
        if i[2] == date:
            reses.append(i)
    if len(i) == 0:
        return "В этот день ученые отдыхали"
    else:
        res = list() #финальные рузельтаты
        for i in reses:
            res.append(f"Ученый {i[0]} создал препарат: {i[1]} - {date}")
        return res


def sort_date(data):
    '''

    :param data: передается список из ученых
    :return: отсортированный по дате список ученых
    на данный момент в разработке
    '''
    return data
def write_to_file(data, type):
    '''

    :param data: список который надо закинуть в файл
    :param type: txt/csv
    :return: creted file
    на данный момент в разработке
    '''
def do_task_1(data) :
    '''
    В задаче 1 нужно выдать полиции всех фейков Аллопуринола и его создателя
    :param data: стандартная дата в формате лист листов
    Принтует “Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):

<ФИО ученого> - <Дата создания>

…

Оригинальный рецепт принадлежит: <ФИО ученого>”
    '''
    data = sort_date(data) # Сортируем по дате
    res = [] # формируем результат
    for i in data:
        if i[1] == "Аллопуринол":
            res.append(i)
    for i in range(1, len(res)):
        print(f"{res[i][0]} - {res[i][2]}")
    print(f"Оригинальный рецепт принадлежит: {res[0][0]}")

#print(delete_dublicates(get_data("scientist.txt")))
#print(get_from_date(get_data("scientist.txt"), "1276-02-24"))

def zad1():
    do_task_1(get_data("scientist.txt"))
def zad3():
    a = input() #юзерввод
    while a != "эксперимент":
        print(get_from_date(get_data("scientist.txt"), a))
        a = input()
