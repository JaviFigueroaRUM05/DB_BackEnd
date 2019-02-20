from config.dbconfig import pg_config
import psycopg2

class ContactsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)


    def getUserContacts(self, uid):
        cursor = self.conn.cursor()
        query = "select cid from contacts where uid= %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getContactById(self, uid):
        cursor = self.conn.cursor()
        query = "select uname, fname, lname, photo from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def verifyContactById(self, uid, cid):
        cursor = self.conn.cursor()
        query = "select cid from contacts where uid = %s AND cid = %s;"
        cursor.execute(query, (uid,cid,))
        result = cursor.fetchone()
        return result