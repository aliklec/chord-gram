from db.repository import *
import mysql.connector

class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db', # to run LOCALLY, this should be localhost (then back to 'host': 'db')
            'port': '3306', # to run LOCALLY, this should be 32000 (then back to 'port': '3306')
            'database': 'songs'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()


