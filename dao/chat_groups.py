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
        query = "select * from cgroup;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select gid, gname, gphoto, uid, uname, " \
                "first_name, last_name, email, phone, isAdmin " \
                "from users natural inner join participants " \
                "natural inner join cgroup " \
                "where isAdmin='t';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get all groups that a user belongs to
    def getGroupsUserBelongsTo(self, uid):
        cursor = self.conn.cursor()
        query = "select gid, gName, gPhoto, isadmin " \
                "from participants natural inner join cgroup " \
                "where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #get metadata of a group
    def getGroupById(self, gid):
        cursor = self.conn.cursor()
        query = "select * " \
                "from cgroup " \
                "where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    # get all users on a group
    def getUsersInAGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, isadmin, uname, first_name, last_name, email, phone " \
                "from participants natural inner join users " \
                "where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

     # get admins on a group
    def getAdminsInAGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, isAdmin, uname, first_name, last_name, email, phone " \
                "from participants natural inner join users " \
                "where gid = %s AND isAdmin='t';"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # get a specific user in a group
    def getParticipantInGroup(self, gid, uid):
        cursor = self.conn.cursor()
        query = "select * from participants where gid = %s AND uid = %s;"
        cursor.execute(query, (gid, uid,))
        result = cursor.fetchone()
        return result

    # creates a new group
    def createNewGroup(self, gname, gphoto):
        cursor = self.conn.cursor()
        query = "insert into cgroup(gname, gphoto) values (%s, %s) returning gid;"
        cursor.execute(query, (gname, gphoto, ))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    # adds a participant in a group
    def addParticipant(self, uid, gid, isAdmin):
        cursor = self.conn.cursor()
        getuser = self.getParticipantInGroup(gid,uid)
        if(self.getParticipantInGroup(gid,uid) is not None):
            return "user already in group"
        else:
            admin = False
            if(isAdmin == 'true'):
                admin = True
            else:
                admin = False
            query = "insert into participants(uid, gid, isAdmin) values (%s, %s, %s) returning uid;"
            cursor.execute(query, (uid, gid, admin, ))
            result = cursor.fetchone()[0]
            self.conn.commit()
            return result

    #removes a participant from a group
    def removeParticipants(self, uid, gid):
        cursor = self.conn.cursor()
        getuser = self.getParticipantInGroup(gid, uid)
        if (getuser is None):
            return "user not in group"
        else:
            query = "delete from participants where uid = %s AND gid = %s returning uid;"
            cursor.execute(query, (uid, gid,))
            result = cursor.fetchone()
            self.conn.commit()
            return result

    def deleteGroup(self, gid):
        cursor = self.conn.cursor()
        query = "select uid from participants where gid = %s; "
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(self.removeParticipants(row, gid))
        self.conn.commit()
        return result

    # ---------------------- yet to implement through handlers --------

    def setGroupAdmin(self, uid, gid):
        cursor = self.conn.cursor()
        query = "insert into chat_administration(gid, admin) where values(%s, %s) returning uid; "
        cursor.execute(query, (gid, uid,))
        self.conn.commit()
        return uid
