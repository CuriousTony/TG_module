import sqlite3
from aiogram.fsm.state import StatesGroup, State


class FormDB(StatesGroup):
    name = State()
    age = State()
    grade = State()


def init_db():
    conn = sqlite3.connect('school_data.db')
    curs = conn.cursor()
    curs.execute(
        '''
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()


init_db()
