from flask import jsonify
from config.dbconfig import pg_config
import psycopg2

class DashboardDao:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def get_trending_hashtag(self):
        cursor = self.conn.cursor()
        query = "select hName, count(*) " \
                "from Hashtag natural inner join Tagged " \
                "group by hName" \
                "order by hName desc"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts(self):
        cursor = self.conn.cursor()
        query = """select pDate, message, mediaType, media, gName, uname
                   from (Post natural inner join Users) natural inner join Cgroup
                   order by postID desc"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_replies_to_post(self, pid):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname" \
                "from (select replyID " \
                "      from Replies " \
                "      where opID = %s) " \
                "      natural inner join " \
                "      ((Post natural inner join Users) natural inner join Cgroup)" \
                "order by postID"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_user(self, uid):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname" \
                "from (Post natural inner join Users) natural inner join Cgroup" \
                "where uid = %s" \
                "order by postID"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname" \
                "from (Post natural inner join Users) natural inner join Cgroup" \
                "where pDate = %s" \
                "order by postID"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_user_date(self, uid, date):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname" \
                "from (Post natural inner join Users) natural inner join Cgroup" \
                "where uid = %s and pDate = %s" \
                "order by postID"
        cursor.execute(query, (uid, date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_replies_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname" \
                "from (select replyID " \
                "      from Replies) " \
                "      natural inner join " \
                "      ((Post natural inner join Users) natural inner join Cgroup)" \
                "where pDate = %s" \
                "order by postID"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_reactions_to_post(self, pid):
        cursor = self.conn.cursor()
        query = "select rType, uname " \
                "from (Reaction natural inner join Users) " \
                "      natural inner join " \
                "      (select postID from Post)"\
                "where postID = %s"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_likes_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from Reaction " \
                "where rDate = %s and rType = 'L' "
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_dislikes_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select count(*) " \
                "from Reaction " \
                "where rDate = %s and rType = 'D' "
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_active_users_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select uname, count(*) " \
                "from Post natural inner join Users " \
                "where rDate = %s " \
                "group by uname desc"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
