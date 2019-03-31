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
        query = "insert into reaction (rdate, rtype, postID, uid) " \
                "VALUES (%s, 'L', %s, %s)"
        cursor.execute(query, (date, pid, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def dislike_post(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "insert into reaction (rdate, rtype, postID, uid) " \
                "VALUES (%s, 'D', %s, %s)"
        cursor.execute(query, (date, pid, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update_to_like(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "update reaction " \
                "set rtype = 'L', rdate = $s " \
                "where uid = %s and postID = %s"
        cursor.execute(query, (date, uid, pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def update_to_dislike(self, pid, uid, date):
        cursor = self.conn.cursor()
        query = "update reaction " \
                "set rtype = 'D', rdate = $s " \
                "where uid = %s and postID = %s"
        cursor.execute(query, (date, uid, pid,))
        cursor.execute()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete_reaction(self, pid, uid):
        cursor = self.conn.cursor()
        query = "delete from reaction " \
                "where uid = %s and postID = %s"
        cursor.execute(query, (uid, pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_reaction(self, pid, uid):
        cursor = self.conn.cursor()
        query = "select rtype " \
                "from reaction " \
                "where uid = %s and postID = %s"
        cursor.execute(query, (uid, pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
