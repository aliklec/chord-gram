
from db.repository import *
import mysql.connector

# this code will connect us to the database

#note - the class below inherits from Repository abstract class
class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost', # to run LOCALLY, this should be localhost (then back to 'host': 'db')
            'port': '32000', # to run LOCALLY, this should be 32000 (then back to 'port': '3306')
            'database': 'songs'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    # destructor
    # when I'm done this will get called and close the DB connection
    # def __del__(self):
    #     self.cursor.close()
    #     self.connection.close()


    def load_chord(self):
        sql = 'SELECT * FROM song_data'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'url': url,
                    'chords': chords,
                    } for (id, url, chords) in self.cursor]
        return entries

if __name__ == '__main__':
    repo = MysqlRepository()
    mysongs = repo.load_chord()
    # print(len(mysongs))
    # print(type(mysongs))
    # for item in mysongs:
    #     print(item)
    #     print(item['chords'])
    #     print(type(item))
    #
    # print()
    # print(len(mysongs))
    # print(type(mysongs))
    print(mysongs[1]['id'])
    print(type(mysongs[0]['chords']))