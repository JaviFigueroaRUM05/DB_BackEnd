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
        query = "select * from post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get all posts of a specified group
    def getPostsByGroup(self, gid):
        cursor = self.conn.cursor()
        query = " select postid, pdate, message, mediatype, media, uid as author, gid, op as original_post, likes, dislikes " \
                "from (select * from" \
                "     (select * from post where gid = %s) as all_posts" \
                "           left outer join" \
                "     (select p1.postid as op, p2.postid as reply" \
                "      from post as p1, replies, post as p2" \
                "      where replies.replyID = p2.postID and replies.opID = p1.postID) as replies_table" \
                "      on all_posts.postid = replies_table.reply) as all_and_replies " \
                "           left outer join" \
                "      (select likes, dislikes, pid1 " \
                "       from (select count(rid) as likes, post.postID as pid1" \
                "               from reaction, post" \
                "               where reaction.postid = post.postid and rType='L'" \
                "               group by post.postID) as likes_tables" \
                "                   left outer join" \
                "            (select count(rid) as dislikes, post.postID as pid2" \
                "               from reaction, post" \
                "               where reaction.postid = post.postid and rType='D'" \
                "               group by post.postID) as dislikes_table" \
                "               on pid1 = pid2) as reactions" \
                "               on all_and_replies.postid = reactions.pid1;"

        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get posts by unique post id
    def getPostById(self, pid):
        cursor = self.conn.cursor()
        select_info_post = " select postid, pdate, message, mediatype, media, uid as author, gid, op as original_post, likes, dislikes " \
                "from (select * from" \
                "     (select * from post where postid = %s) as all_posts" \
                "           left outer join" \
                "     (select p1.postid as op, p2.postid as reply" \
                "      from post as p1, replies, post as p2" \
                "      where replies.replyID = p2.postID and replies.opID = p1.postID) as replies_table" \
                "      on all_posts.postid = replies_table.reply) as all_and_replies " \
                "           left outer join" \
                "      (select likes, dislikes, pid1 " \
                "       from (select count(rid) as likes, post.postID as pid1" \
                "               from reaction, post" \
                "               where reaction.postid = post.postid and rType='L'" \
                "               group by post.postID) as likes_tables" \
                "                   left outer join" \
                "            (select count(rid) as dislikes, post.postID as pid2" \
                "               from reaction, post" \
                "               where reaction.postid = post.postid and rType='D'" \
                "               group by post.postID) as dislikes_table" \
                "               on pid1 = pid2) as reactions" \
                "               on all_and_replies.postid = reactions.pid1;"
        cursor.execute(select_info_post, (pid,))
        result = cursor.fetchone()
        return result

    # get all users that have reacted to a specific post
    def getUsers_and_Reactions(self, pid):
        cursor = self.conn.cursor()
        query = "select uid, uname, first_name, last_name, email, phone, rid, rdate, rtype " \
                "from users natural inner join reaction " \
                "where postid = %s;"
        cursor.execute(query, (pid,))
        user_list = []
        for row in cursor:
            user_list.append(row)
        return user_list

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
