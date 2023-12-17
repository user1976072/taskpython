import json
import os
import datetime

class Note:
    def __init__(self, id, title, content, timestamp):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self, id, title, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(id, title, content, timestamp)
        self.notes.append(new_note)

    def save_notes_to_json(self):
        data = []
        for note in self.notes:
            data.append({
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "timestamp": note.timestamp
            })
        with open('notes.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_notes_from_json(self):
        if os.path.exists('notes.json'):
            with open('notes.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    new_note = Note(item['id'], item['title'], item['content'], item['timestamp'])
                    self.notes.append(new_note)

    def display_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}\nTitle: {note.title}\nContent: {note.content}\nTimestamp: {note.timestamp}\n")

    def edit_note(self, id, new_content):
        for note in self.notes:
            if note.id == id:
                note.content = new_content
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)