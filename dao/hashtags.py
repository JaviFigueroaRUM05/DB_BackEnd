from config.dbconfig import pg_config
import psycopg2

class HashtagsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getHashtagID(self, hname):
        cursor = self.conn.cursor()
        query = "select hid from hashtag where hname=%s;"
        cursor.execute(query, (hname,))
        result = cursor.fetchone()
        return result

    def createHashtag(self, hname):
        cursor = self.conn.cursor()
        query = "insert into hashtag(hname) values (%s) returning hid;"
        cursor.execute(query, (hname,))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def addTaggedPost(self, hid, postid):
        cursor = self.conn.cursor()
        query = "insert into tagged(postid, hid) values (%s, %s) returning postid;"
        cursor.execute(query, (postid, hid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result
