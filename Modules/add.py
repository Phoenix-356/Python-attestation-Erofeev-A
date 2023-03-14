from Modules.save import save_notes


def add_notes(new_notes):
    new_notes.header = input("Укажите заголовок заметки: ")
    new_notes.body = input("Укажите содержание заметки: ")
    save_notes(new_notes)