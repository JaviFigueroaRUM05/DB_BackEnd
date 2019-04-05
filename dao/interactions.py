from flask import jsonify
from config.dbconfig import pg_config
import psycopg2

class InteractionsDao:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def like_post(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "insert into Reaction (rdate, rtype, postID, uid) " \
                "VALUES (%s, 'L', %s, %s)" \
                "returning *"
        cursor.execute(query, (date, pid, uid,))
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def dislike_post(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "insert into Reaction (rdate, rtype, postID, uid) " \
                "VALUES (%s, 'D', %s, %s) " \
                "returning *"
        cursor.execute(query, (date, pid, uid,))
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update_to_like(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "update Reaction " \
                "set rtype = 'L', rdate = $s " \
                "where uid = %s and postID = %s " \
                "returning *"
        cursor.execute(query, (date, uid, pid,))
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update_to_dislike(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "update Reaction " \
                "set rtype = 'D', rdate = $s " \
                "where uid = %s and postID = %s " \
                "returning *"
        cursor.execute(query, (date, uid, pid,))
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete_reaction(self, pid, uid):
        cursor = self.conn.cursor()
        query = "delete from Reaction " \
                "where uid = %s and postID = %s " \
                "returning *"
        cursor.execute(query, (uid, pid,))
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_reaction(self, pid, uid):
        cursor = self.conn.cursor()
        query = "select rtype from Reaction where uid = %s and postID = %s"
        cursor.execute(query, (uid, pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
