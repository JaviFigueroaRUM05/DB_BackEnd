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

    def get_trending_hashtags(self):
        cursor = self.conn.cursor()
        query = "select hName, count(*) " \
                "from Hashtag natural inner join Tagged " \
                "group by hName " \
                "order by hName desc"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts(self):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uid, postid " \
                "from (Post natural inner join Users) natural inner join Cgroup " \
                "order by postID desc"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_replies_to_post(self, pid):
        cursor = self.conn.cursor()
        query = "select p.pDate, p.message, p.mediatype, p.media, p.postid " \
                "from (select * from replies) as r, post as p " \
                "where r.replyid = p.postid and r.opid = %s " \
                "order by p.postID"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_user(self, uid):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname, postid " \
                "from (Post natural inner join Users) natural inner join Cgroup " \
                "where uid = %s " \
                "order by postID"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_date(self, date):
        cursor = self.conn.cursor()
        query = "select pDate, message, mediaType, media, gName, uname, postid " \
                "from (Post natural inner join Users) natural inner join Cgroup " \
                "where pDate between %s and %s"
        start_date = date + " 00:00:00"
        end_date   = date + " 23:59:59"
        cursor.execute(query, (start_date, end_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_count_by_date(self):
        cursor = self.conn.cursor()
        query  = "select date(pdate), count(*) " \
                 "from post " \
                 "group by date(pdate)"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_posts_by_user_date(self, uid):
        cursor = self.conn.cursor()
        query = "select date(pDate), count(*) " \
                "from (Post natural inner join Users) natural inner join Cgroup " \
                "where uid = %s " \
                "group by date(pDate)"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_all_replies_by_date(self):
        cursor = self.conn.cursor()
        query = "select date(pDate), count(*) " \
                "from (Replies inner join Post on Replies.replyid = Post.postid) " \
                "group by date(pdate)"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_reactions_to_post(self, pid):
        cursor = self.conn.cursor()
        query = "select rType, uname, rdate, uid " \
                "from (Reaction natural inner join Users) " \
                "      natural inner join " \
                "      (select postID from Post) as p "\
                "where p.postID = %s"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_reactions_count_to_post(self, pid):
        cursor = self.conn.cursor()
        query = "select rType, postid, count(*) " \
                "from Reaction " \
                "where postid = %s " \
                "group by postid, rtype"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_likes_by_date(self):
        cursor = self.conn.cursor()
        query = "select date(rdate), count(*) " \
                "from Reaction " \
                "where rType = 'L' " \
                "group by date(rdate)"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_dislikes_by_date(self):
        cursor = self.conn.cursor()
        query = "select date(rdate), count(*) " \
                "from Reaction " \
                "where rType = 'D' " \
                "group by date(rdate)"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def get_active_users_by_date(self):
        cursor = self.conn.cursor()
        query = "select date(pdate), uname, count(*) " \
                "from Post natural inner join Users " \
                "group by date(pdate), uname " \
                "order by date(pdate), count(*) desc"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result
