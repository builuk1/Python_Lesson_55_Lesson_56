# Записна книжка

class Note:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def edit(self, new_content):
        self.content = new_content

    def __str__(self):
        return self.content


class Notebook:

    # Create notes
    def __init__(self):
        self.notes = []

    # Create note
    def add_note(self, title, author, content):
        note = Note(title, author, content)
        self.notes.append(note)

    # Read
    def __str__(self):
        result = ''
        for note in self.notes:
            result = result + str(note.content) + '\n'
        return result

    # Delete
    def remove_note(self, title):
        for index in range(len(self.notes)):
            if (self.notes[index]).title == title:
                self.notes.pop(index)
                break


flag = True
book = Notebook()

while flag:
    command = str(input('Enter command: [r], [c], [e], [d]: '))
    if command.lower() == 'c':
        title = str(input('Enter title: '))
        author = str(input('Enter author: '))
        content = str(input('Enter content: '))

        book.add_note(title, author, content)
    elif command.lower() == 'r':
        print(book)

    elif command.lower() == 'e':
        flag = str(input("Enter [any key] + [enter] to continue OR enter [enter] to exit: "))

    elif command.lower() == 'd':
        title = str(input('Enter title: '))
        book.remove_note(title)

# age = 12
# if age < 13:
#     print('Child')
