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
        query = "select uid, uname, first_name, last_name, email, phone " \
                "from users " \
                "where uid in (select cid from contacts where uid= %s);"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactById(self, uid, cid):
        cursor = self.conn.cursor()
        query = "select uid, uname, first_name, last_name, email, phone " \
                "from users " \
                "where uid =" \
                "(select cid from contacts where uid=%s and cid=%s);"
        cursor.execute(query, (uid,cid,))
        result = cursor.fetchone()
        return result

    def addContactByEmail(self, uid, first_name, last_name, email):
        cursor = self.conn.cursor()
        query = "insert into contacts (uid, cid)"\
                "values (%s, (select uid from users where first_name=%s"\
                "AND last_name=%s AND email=%s)) returning uid,cid;"
        cursor.execute(query, (uid, first_name, last_name, email, ))
        response = cursor.fetchone()
        self.conn.commit()
        return response

    def addContactByPhone(self, uid, first_name, last_name, phone):
        cursor = self.conn.cursor()
        query = "insert into contacts (uid, cid)"\
                "values (%s, (select uid from users where first_name=%s"\
                "AND last_name=%s AND phone=%s)) returning uid,cid;"
        cursor.execute(query, (uid, first_name, last_name, phone,))
        response = cursor.fetchone()
        self.conn.commit()
        return response

    def removeContactById(self, uid, cid):
        cursor = self.conn.cursor()
        query = "DELETE from contacts where uid=%s AND cid=%s returning (cid);"
        cursor.execute(query, (uid, cid,))
        self.conn.commit()
        return {'entriesDeleted': cursor.rowcount}
