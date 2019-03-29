from config.dbconfig import pg_config
import psycopg2


class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsersInfo(self):
        cursor = self.conn.cursor()
        query = "select uid, uname, first_name, last_name, email, phone " \
                "from Users;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserInfoByID(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, uname, first_name, last_name, email, phone " \
                "from Users where uid= %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserInfoByUname(self, uname):
        cursor = self.conn.cursor()
        query = "select uid, uname, first_name, last_name, email, phone " \
                "from Users where uname= %s;"
        cursor.execute(query, (uname,))
        result = cursor.fetchone()
        return result

    def getIdByLogin(self, email, password):
        cursor = self.conn.cursor()
        query = "select uid from users where email = %s AND password = %s;"
        cursor.execute(query, (email,password))
        result = cursor.fetchone()
        return result

    def insertNewUser(self, uname, email, password, first_name, last_name, phone):
        cursor = self.conn.cursor()
        query = "insert into users(uname, email, password, first_name," \
                " last_name, phone) values (%s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (uname, email, password, first_name, last_name, phone,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid
