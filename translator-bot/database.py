import sqlite3 as sq


class Database:
    def __init__(self, database):
        self.conn = sq.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS "User" (
                "id"	INTEGER,
                "user_id"	INTEGER NOT NULL,
                "username"	TEXT,
                "created_at"	DATETIME NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
            """
        )

    def create_user(self, user_id, username, time):
        self.cur.execute(
            """INSERT INTO User(user_id,username,created_at) VALUES (?,?,?)""",
            (user_id, username, time)

        )
        self.conn.commit()


    def count_user(self):
        self.cur.execute(
            """SELECT * from User"""
        )
        users = dict_fetchall(self.cur)
        return users



    def get_user_by_chat_id(self, chat_id):
        self.cur.execute(
            """SELECT * FROM User WHERE user_id = ?""",
            (chat_id,)
        )
        user = dict_fetchone(self.cur)
        return user





def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
