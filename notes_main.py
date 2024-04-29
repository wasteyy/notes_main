from PyQt5.QtCore import Qt
import json
from PyQt5.QtWidgets import QInputDialog, QApplication, QVBoxLayout,  QHBoxLayout, QWidget, QListWidget, QLabel, QPushButton, QTextEdit, QLineEdit


notesies = {
    "Welcome note":{
        "text": "In this application you can create notes with tags and many more things",
        "tags": ["smart notes", "tips"]
    }
}

def add_notesie():
    note_name, ok = QInputDialog.getText(prozor, "Add note", "Note name:")
    if ok and note_name != " ":
        notesies[note_name] = {"text": " ", "tags": []}
        title_list.addItem(note_name)

def delete_notesie():
    if note_name.selectedItems():
        key = title_list.selectedItems()[0].text()
        del notesies[key]
        title_list.clear()
        text_field.clear()
        with open("smart_notes.json", "w", sort_keys = True, ensure_ascii = True) as file:
            json.dump(notesies, file)
    else:
        print("You haven't typed anything in")

def save_notesie():
    if title_list.selectedItems():
        key = title_list.selectedItems()[0]
        notesies[key]["text"] = text_field.toPlainText()
        with open("smart_notes.json", "w") as file:
            json.dump(notesies, file)
    else:
        print("You haven't typed anything in")

with open("smart_notes.json", "w") as file:
    json.dump(notesies, file)

app = QApplication([])
prozor = QWidget()
prozor.setWindowTitle("Smart Notes")
prozor.resize(900, 600)

title_list = QListWidget()
tag_list = QListWidget()

title_title = QLabel("Title list")
tag_title = QLabel("Tag list")

create_note = QPushButton("Create note")
delete_note = QPushButton("Delete note")
save_note = QPushButton("Save note")
add_note = QPushButton("Add to note")
untag_note = QPushButton("Untag from note")
search_note = QPushButton("Search notes by tag")

tag_line = QLineEdit()
tag_line.setPlaceholderText("Enter tag...")

text_field = QTextEdit()

v_line = QVBoxLayout()
v_line.addWidget(title_title)
v_line.addWidget(title_list)
h_line = QHBoxLayout()
h_line.addWidget(create_note)
h_line.addWidget(delete_note)
v_line.addLayout(h_line)
v_line.addWidget(save_note)
v_line.addWidget(tag_title)
v_line.addWidget(tag_list)
v_line.addWidget(tag_line)
h_line2 = QHBoxLayout()
h_line2.addWidget(add_note)
h_line2.addWidget(untag_note)
v_line.addLayout(h_line2)
v_line.addWidget(search_note)
v_line2 =QVBoxLayout()
v_line2.addWidget(text_field)
main_h_line = QHBoxLayout()
main_h_line.addLayout(v_line2, stretch=2)
main_h_line.addLayout(v_line, stretch=1)

prozor.setLayout(main_h_line)

def show_note():
    name = title_list.selectedItems()[0].text()
    text_field.setText(notesies[name]["text"])
    tag_list.clear()
    tag_list.addItems(notesies[name]["tags"])

title_list.itemClicked.connect(show_note)
create_note.clicked.connect(add_notesie)
delete_note.clicked.connect(delete_notesie)
save_note.clicked.connect(save_notesie)

with open("smart_notes.json", "r") as file:
    notesies = json.load(file)

title_list.addItems(notesies)

prozor.show()
app.exec()
