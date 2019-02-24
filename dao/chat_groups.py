from config.dbconfig import pg_config
import psycopg2

class Chat_GroupsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                                    pg_config['host'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from chat_groups;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, gid):
        cursor = self.conn.cursor()
        query = "select * from chat_groups where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    # get all groups that a user belongs to
    def getGroupsByUser(self, uid):
        cursor = self.conn.cursor()
        query = "select * from participants where participant_id = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get all users on a group
    def getUsersByGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select participant_id, participant_name from participants where group_id = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserInGroup(self, gid, uid):
        cursor = self.conn.cursor()
        query = "select * from participants where group_id = %s AND participant_id = %s;;"
        cursor.execute(query, (gid, uid,))
        result = cursor.fetchone()
        return result

    def getGroupName(self, gname):
        cursor = self.conn.cursor()
        query = "select * from chat_groups where gname = %s;"
        cursor.execute(query, (gname))
        result = cursor.fetchone()
        return result

    def getGroupsByAdmin(self, admin):
        cursor = self.conn.cursor()
        query = "select gid from chat_administration where admin = %s;"
        cursor.execute(query, (admin,))
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def createNewGroup(self, gname, gphoto, gadmin):
        cursor = self.conn.cursor()
        query = "insert into chat_groups(gname, gphoto, gadmin) values (%s, %s, %s) returning gid;"
        cursor.execute(query, (gname, gphoto, gadmin,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def addUserToGroup(self, gid, gname, uid, uname):
        cursor = self.conn.cursor()
        query = "insert into participants(group_id, group_name, participant_id, participant_name) values (%s, %s, %s, %s) returning participant_name;"
        cursor.execute(query, (gid, gname, uid, uname,))
        participant_name = cursor.fetchone()[0]
        self.conn.commit()
        return participant_name

    # users param is an array that will be passed when the admin selects the users to
    # add fro his/her contact list. Particiapnts will be added to table Particiapnts, which
    # will serve as the intermediate between the chat_groups and user tables.
    def addUsersToGroup(self, gid, gname, users):
        cursor = self.conn.cursor()
        added_users=[]
        for user in users:
            user_id = user[0]
            user_name = user[1]
            query = "insert into participants(group_id, group_name, participant_id, participant_name) values (%d, %s, %d, %s) returning uid;"
            cursor.execute(query, (gid, gname, user_id, user_name))
            uid = cursor.fetchone()[3]
            self.conn.commit()
            added_users.append(uid)
        return added_users

    #delete group from own's personal group collection
    def deleteGroupIfUser(self, uid):
        cursor = self.conn.cursor()
        query = "delete from participants where uid = %s; "
        cursor.execute(query, (uid,))
        self.conn.commit()
        return gid

    def deleteGroupIfAdmin(self, uid):
        cursor = self.conn.cursor()
        query = "delete from chat_administration where uid = %s; "
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid

    def setGroupAdmin(self, uid, gid):
        cursor = self.conn.cursor()
        query = "insert into chat_administration(gid, admin) where values(%s, %s) returning uid; "
        cursor.execute(query, (gid, uid,))
        self.conn.commit()
        return uid

    def deleteUserFromGroup(self, gid, uid):
        cursor = self.conn.cursor()
        query = "delete from participants where group_id = %s AND participant_id = %s; "
        cursor.execute(query, (gid, uid))
        self.conn.commit()
        return uid
