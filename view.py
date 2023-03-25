class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print('>>>...')
            print(note)

    @staticmethod
    def show_note(note):
        print('>>>...')
        print(note)

    @staticmethod
    def show_empty_list_message():
        print('>>Cписок заметок пустой!')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(f'>>>Заметка {note_id} не найдена!')

    @staticmethod
    def display_note_id_exist(note_id):
        print(f'>>>Заметка {note_id} уже есть!')

    @staticmethod
    def display_note_stored():
        print('>>>Заметка успешно добавлена!')

    @staticmethod
    def display_note_updated(note_id):
        print(f'>>>Заметка {note_id} обновлена!')

    @staticmethod
    def display_note_deletion(note_id):
        print(f'>>>Заметка {note_id} удалена!')

    @staticmethod
    def display_all_notes_deletion():
        print('>>>Все заметки удалены!')

    def display_note_id_not_exist(search_id):
        return search_id