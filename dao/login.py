from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

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
        query = "insert into users(uname, email, password, fname, lname) values (%s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (uname, email, password, fname, lname))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid





#Old methods

    def getPartsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from supplier where scity = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sname, scity, sphone):
        cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sname, scity, sphone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid