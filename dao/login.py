from config.dbconfig import pg_config
import psycopg2


class LoginDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getIdByLogin(self, email, password):
        cursor = self.conn.cursor()
        query = "select uid from users where email = %s AND password = %s;"
        cursor.execute(query, (email,password))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "select * from users where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserPassword(self, email):
        cursor = self.conn.cursor()
        query = "select password from users where email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def insertNewUser(self, uname, email, password, fname, lname):
        cursor = self.conn.cursor()
        query = "insert into users(uname, email, password, fname," \
                " lname) values (%s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (uname, email, password, fname, lname))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid
