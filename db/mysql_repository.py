from db.repository import *
import mysql.connector

# this code connects to the database
# class below inherits from Repository abstract class
class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db', # locally: localhost / default: 'db'
            'port': '3306', # locally: 32000 / default: '3306'
            'database': 'songs',
            'allow_local_infile': True
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    # destructor
    # when done this gets called and close the DB connection
    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def load_songs(self):
        sql = 'SELECT * FROM song_data'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'url': url,
                    'chords': chords,
                    } for (id, url, chords) in self.cursor]
        return entries

    def load_chords(self):
        sql = 'SELECT chords FROM song_data'
        self.cursor.execute(sql)
        chords_list = []
        for row in self.cursor:
            chords_list.append(row[0])
        return chords_list

