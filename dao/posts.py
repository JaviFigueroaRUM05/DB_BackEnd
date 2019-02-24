from config.dbconfig import pg_config
import psycopg2

class PostsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from Post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPostsByGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select * from Post where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get posts by unique post id
    def getPostById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from Post where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    # get posts by date posted
    def getPostsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from Post where post_date = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get all Replies for a single post; returns array of post ids, which are the post id for those replies
    def getRepliesByPost(self, pid):
        cursor = self.conn.cursor()
        query = "select * from post where reply_to_post = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get all photos of specific group :: needs to be worked on
    # either use join with pid as common attribute or put al info in new table
    def getMediaInGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select * from group_posts where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # see posts by user
    def getPostsByUser(self, uid):
        cursor = self.conn.cursor()
        query = "select pid from user_post where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def createNewPost(self, post_date, media, message, gid, reply_to_post, uid):
        cursor = self.conn.cursor()
        query = "insert into Post(post_date, media, message, gid, reply_to_post) values (%s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (post_date, media, message, gid, reply_to_post,))
        pid = cursor.fetchone()[0]
        query1 = "insert into user_post(uid, pid) values (%s, %s);"
        cursor.execute(query1, (uid, pid,))
        self.conn.commit()
        return pid
