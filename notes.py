import os
import time

def create_note():
    filename = input("Введите заголовок заметки: ") + ".txt"
    with open(filename, "w") as file:
        content = input("Введите тело заметки: ")
        file.write(content)
        file.close

def show_notes():
    files = os.listdir()
    txt_files = [file for file in files if file.endswith(".txt")]

    print("Открыть список заметок:")
    for file in txt_files:
        print(f"- {file}")

    filename = input("Введите заголовок заметки для просмотра: ") + ".txt"
    if filename in txt_files:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
            file.close
    else:
        print("Заметка не найдена!")

def del_note():
    filename = input("Введите заголовок заметки, которую вы хотите удалить: ") + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f'Заметка "{filename}" удалена.')
    else:
        print("Заметка не найдена.")
        
def edit_note():
    filename = input("Введите заголовок заметки, которую вы хотите редактировать: ") + ".txt"
    with open(filename, "r") as file:
        content = file.read()
        print(f'Текущее содержимое заметки "{filename}":')
        print(content)
        file.close

    edit_mode = input("Хотите перезаписать всю заметку (введите 'всю')\n отредактировать заметку частично (введите 'частично')\n или продолжить запись (введите 'продолжить')? ")
    if edit_mode == "всю":
        new_content = input("Введите новый текст: ")
        with open(filename, "w") as file:
            file.write(new_content)
            print(f'Заметка "{filename}" обновлена.')
            file.close
    elif edit_mode == "частично":
        lines = content.split("\n")
        for i, line in enumerate(lines):
            print(f"{i + 1}: {line}")

        line_num = int(input("Введите номер строки, которую вы хотите изменить: "))
        new_line = input("Введите новый текст для этой строки: ")
        lines[line_num - 1] = new_line

        with open(filename, "w") as file:
            file.write("\n".join(lines))
            print(f'Заметка "{filename}" обновлена.')
            file.close
    elif edit_mode == "продолжить":
        new_content = input("Введите текст, который вы хотите добавить: ")
        with open(filename, "a") as file:
            file.write("\n" + new_content)
            print(f'Заметка "{filename}" обновлена.')
            file.close
    else:
        print("Неверный режим редактирования.")

def find_note_for_date():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    date = time.strptime(date_str, "%Y-%m-%d")

    files = os.listdir()
    txt_files = [file for file in files if file.endswith(".txt")]

    print(f"Заметки созданные {date_str}:")
    for file in txt_files:
        file_date = time.localtime(os.path.getctime(file))
        if file_date.tm_year == date.tm_year and file_date.tm_mon == date.tm_mon and file_date.tm_mday == date.tm_mday:
            print(f"- {file}")

flag = True
while flag:
    print('\nДобро пожаловать в приложение "Заметки"!\n')
    ask = int(input(
        '1 - создать новую заметку\n' +  
        '2 - вывести список заметок\n' + 
        '3 - для поиска по дате\n' + 
        '4 - для редактирования\n' +
        '5 - для удаления\n' + 
        '6 - для выхода\n'))
    if ask == 1:
        create_note()
        answ = str.lower(input('Продолжаем? 1-да/0-нет -> '))
        if answ == '0': flag = False
        else: continue
    elif ask == 2:
        show_notes()
        answ = str.lower(input('Продолжаем? 1-да/0-нет -> '))
        if answ == '0': flag = False
        else: continue
    elif ask == 3:
        find_note_for_date()
        answ = str.lower(input('Продолжаем? 1-да/0-нет -> '))
        if answ == '0': flag = False
        else: continue
    elif ask == 4:
        edit_note()
        answ = str.lower(input('Продолжаем? 1-да/0-нет -> '))
        if answ == '0': flag = False
        else: continue
    elif ask == 5:
        del_note()
        answ = str.lower(input('Продолжаем? 1-да/0-нет -> '))
        if answ == '0': flag = False
        else: continue
    elif ask == 6:
        flag = False
    else:
        print('Операция не найдена!')