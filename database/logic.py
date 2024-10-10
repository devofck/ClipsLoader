import os
import sqlite3
import time


class Database:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('database\\database.sqlite3')

    def add_video(self, video_path: str, likes: int):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO videos(video_path, likes_count, loaded_date) VALUES(?,?,?)',
            [
                video_path,
                likes,
                round(time.time())
            ]
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
