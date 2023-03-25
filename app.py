from controller import Controller
from model_json import ModelJSON
from view import View
from note import Note

import os
import datetime



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(
                        '[1] Добавить заметку\n'
                        '[2] Показать заметку\n'
                        '[3] Показать все заметки\n'
                        '[4] Редактировать заметку\n'
                        '[5] Удалить заметку\n'
                        '[6] Удалить все заметки\n'
                        '[7] Выход\n'
                        'Выберите действие: ')

        if command == '1':
            print('\tСоздание заметки.')
            c.create_note(get_note_data())

        elif command == '2':
            print('\tПоказать заметку.')
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif command == '3':
            if c.notes_exist():
                print('\tПоказать все заметки.')
                c.show_notes()

        elif command == '4':
            if c.notes_exist():
                print('\tРедактировать заметку.')
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '5':
            if c.notes_exist():
                print('\tВы удаляете заметку!')
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '6':
            if c.notes_exist():
                print('Удалить все заметки!')
                if input('Уверены!!! (Y/N): ').capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '7':
            break

        else:
            print('\tНеверный ввод!')


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('\t\tДайте имя заметке: ')
    text = input('\t\tЗаполните заметку: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('\t\tВведите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print('\t\t\tВведено неверное id заметки!')