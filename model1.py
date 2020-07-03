import sqlite3

class Model():
    def __init__(self, db):
        self.db = db

    def select_everything(self):
        conn = sqlite3.connect(self.db)
        result = conn.cursor().execute('select * from article')
        return result
