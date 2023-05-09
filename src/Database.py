import unittest
import sqlite3


class Database:

    def __init__(self, path: str = ':memory:'):
        self.con = sqlite3.connect(
            database=path
        )

    def create_table(self):
        cur = self.con.cursor()
        query = """
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        """
        cur.execute(query)

    def select_all(self):
        cur = self.con.cursor()
        query = """
        SELECT * FROM user;
        """
        res = cur.execute(query)
        print(res.fetchall())

    def add_user(self, username: str, password: str):
        cur = self.con.cursor()
        query = """
        INSERT INTO user VALUES (?, ?, ?);
        """
        cur.execute(query, (None, username, password))
    
    def password_is_valid(self, username: str, password: str) -> bool:
        cur = self.con.cursor()
        query = """
        SELECT password FROM user WHERE username = ?;
        """
        cur.execute(query, (username,))
        res = cur.fetchone()
        return res[0] == password


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.con.close()
    
    def test_create_table(self):
        self.db.create_table()

    def test_add_user(self):
        cur = self.db.con.cursor()
        self.db.add_user(username='Kamet0', password='K@rmineC0rp')
        query = """
        SELECT username, password FROM user WHERE username = 'Kamet0';
        """
        cur.execute(query)
        res = cur.fetchone()
        self.assertEqual(res[0], 'nelo')
        self.assertEqual(res[1], 'karmine')


if __name__ == '__main__':
    unittest.main()
