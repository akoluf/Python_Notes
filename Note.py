import os
import sys


class Note:
    def __init__(self, id, title, text):
        self.id = id
        self.title = title
        self.text = text

    def save(self):
        filename = f"{self.id}_{self.title}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)

    @classmethod
    def load(cls, id, title):
        filename = f"{id}_{title}.txt"
        with open(filename, "r", encoding="utf-8") as file:
            return cls(id, title, file.read())

    def edit(self):
        new_text = input("Введите новый текст заметки: ")
        self.text = new_text
        self.save()

    def delete(self):
        filename = f"{self.id}_{self.title}.txt"
        os.remove(filename)


def create_note():
    title = input("Введите название заметки (максимум 12 символов): ")
    while len(title) > 12:
        print("Название слишком длинное. Пожалуйста, попробуйте еще раз.")
        title = input("Введите название заметки (максимум 12 символов): ")

    text = input("Введите текст заметки (максимум 200 символов): ")
    while len(text) > 200:
        print("Текст слишком длинный. Пожалуйста, попробуйте еще раз.")
        text = input("Введите текст заметки (максимум 200 символов): ")

    # Получаем следующий свободный id
    id = len([f for f in os.listdir() if f.endswith(".txt")]) + 1
    note = Note(id, title, text)
    note.save()
    return note


def view_notes():
    notes = [f for f in os.listdir() if f.endswith(".txt")]
    notes.sort()
    for note in notes:
        note_id, note_title = note.split("_", 1)
        print(f"{note_id}. {note_title.rsplit('.', 1)[0]}")


def edit_note():
    note_id = input("Введите ID заметки: ")
    notes = [f for f in os.listdir() if f.endswith(".txt")]
    note_file = None
    for note in notes:
        if note.startswith(f"{note_id}_"):
            note_file = note
            break
    if note_file:
        title = note_file.split("_", 1)[1].rsplit(".", 1)[0]
        note = Note.load(note_id, title)
        note.edit()
    else:
        print("Заметка не найдена.")


def delete_note():
    note_id = input("Введите ID заметки: ")
    notes = [f for f in os.listdir() if f.endswith(".txt")]
    note_file = None
    for note in notes:
        if note.startswith(f"{note_id}_"):
            note_file = note
            break
    if note_file:
        title = note_file.split("_", 1)[1].rsplit(".", 1)[0]
        note = Note.load(note_id, title)
        note.delete()
    else:
        print("Заметка не найдена.")


def main():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Выход...")
            sys.exit()
        else:
            print("Неверная опция. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
