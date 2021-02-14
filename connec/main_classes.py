import datetime

class ObjectPostgres():
    import psycopg2

    # подключение к postgres
    def __init__(self, db_name, db_user, db_password, db_host, db_port=5432):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.connection = self.__connect(self.db_name, self.db_user, self.db_password, self.db_host,
                        self.db_port)
        if self.connection:
            self.cursor = self.connection.cursor()

    def __connect(self, db_name, db_user, db_password, db_host, db_port):
        connection = None
        if not(self.db_port):
            self.db_port = 5432
        try:
            connection = self.psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print('Соединение установлено')
        except:
            print('Соединение не установлено')
        return connection

    def execute_read_query(self, query):
        result_serial = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            result_serial = []
            # сериализация типа данных date из-за JSON
            for object in range(len(result)):
                result_serial.append([])
                for i in range(len(result[object])):
                    if isinstance(result[object][i], datetime.date):
                        i = result[object][i].__str__()
                        result_serial[object].append(i)
                        continue
                    result_serial[object].append(result[object][i])
            print('Запрос выполнен')
        except:
            print("Запрос не выполнен")
        return result_serial

class ObjectMySQL():
    import mysql.connector

    def __init__(self, db_name, db_user, db_password, db_host, db_port=3306):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.connection = self.__connect(self.db_name, self.db_user, self.db_password, self.db_host,
                                         self.db_port)
        if self.connection:
            self.cursor = self.connection.cursor()

    def __connect(self, db_name, db_user, db_password, db_host, db_port):
        connection = None
        if not (self.db_port):
            self.db_port = 3306
        try:
            connection = self.mysql.connector.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print('Соединение установлено')
        except:
            print('Соединение не установлено')
        return connection

    def execute_read_query(self, query):
        result_serial = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            result_serial = []
            # сериализация типа данных date из-за JSON
            for object in range(len(result)):
                result_serial.append([])
                for i in range(len(result[object])):
                    if isinstance(result[object][i], datetime.date):
                        i = result[object][i].__str__()
                        result_serial[object].append(i)
                        continue
                    result_serial[object].append(result[object][i])
            print('Запрос выполнен')
        except:
            print("Запрос не выполнен")
        return result_serial