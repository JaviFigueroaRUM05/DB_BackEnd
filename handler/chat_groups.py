from flask import jsonify
from psycopg2 import IntegrityError
from dao.chat_groups import Chat_GroupsDAO

class Chat_GroupsHandler:

    def build_chat_groups_dict(self, row):
        result = {}
        result['GID'] = row[0]
        result['gName'] = row[1]
        result['gPhoto'] = row[2]
        return result

    def build_chat_groups_participants_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['isadmin'] = row[1]
        result['uname'] = row[2]
        result['first_name'] = row[3]
        result['last_name'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        return result

    def build_all_admins_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gName'] = row[1]
        result['gPhoto'] = row[2]
        result['uid'] = row[3]
        result['uname'] = row[4]
        result['first_name'] = row[5]
        result['last_name'] = row[6]
        result['email'] = row[7]
        result['phone'] = row[8]
        result['isAdmin'] = row[9]
        return result


    # tested - works
    def getAllGroups(self):
        dao = Chat_GroupsDAO()
        groups_list = dao.getAllGroups()
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result_list.append(result)
        return jsonify(Chat_groups=result_list)


    # tested - works
    def getAllAdmins(self):
        dao = Chat_GroupsDAO()
        adminsList = dao.getAllAdmins()
        result_list = []
        for row in adminsList:
            result = self.build_all_admins_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    #tested - working
    # get groups a user belongs to
    def getGroupsUserBelongsTo(self, uid):
        if not uid:
          return jsonify(Error="No user logged in")
        dao = Chat_GroupsDAO()
        groups_list = dao.getGroupsUserBelongsTo(uid)
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result['isAdmin'] = row[3]
            result_list.append(result)
        return jsonify(result_list)

    #get specific chat group
    def getGroupById(self, gid):
        dao = Chat_GroupsDAO()
        row = dao.getGroupById(gid)
        if not row:
            return jsonify(Error = "Group Not Found"), 404
        else:
            chat_info = self.build_chat_groups_dict(row)
            participants_list = dao.getUsersInAGroup(gid)
            result_list = []
            for p in participants_list:
                result = self.build_chat_groups_participants_dict(p)
                result_list.append(result)
            chat_info['participants'] = result_list
            return jsonify(chat_info)


    def getGroupAdmins(self, gid):
        dao = Chat_GroupsDAO()
        admin_list = dao.getAdminsInAGroup(gid=gid)
        if not admin_list:
            return jsonify(Error= "Group with gid=" +gid+ " does not have any Admins."),404
        else:
            admins=[]
            for admin in admin_list:
                admins.append(self.build_chat_groups_participants_dict(admin))
            return jsonify({"admins": admins}), 200

    def editGroupAdmins(self, gid, json):
        dao = Chat_GroupsDAO()
        uid = json['uid']
        isadmin = json['isAdmin']
        result = dao.editGroupAdmins(uid, gid, isadmin)
        return jsonify({'reply_id': result})


    def createNewGroup(self, json):
        dao = Chat_GroupsDAO()
        try:
            if json.get('gname') :
                gid = dao.createNewGroup(gname=json['gname'], gphoto=['gphoto'])
            else:
                return jsonify(Error='Group name not provided.'), 400
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))
        json['gid']=gid
        return jsonify({"group": json})

    def addParticipant(self, gid, json):
        dao = Chat_GroupsDAO()
        uid_participant = dao.addParticipant(uid=json['uid'], gid=gid, isAdmin=['isadmin'])  #uid comes from json
        return jsonify({"added_participant": uid_participant})

    def removeParticipant(self, gid, json):
        dao = Chat_GroupsDAO()
        result = dao.removeParticipants(uid=json['uid'], gid=gid)  # uid comes from json
        return jsonify({"removed_participant": result})

    def deleteGroup(self, gid):
        dao = Chat_GroupsDAO()
        result = dao.deleteGroup(gid=gid)
        return jsonify({"deleted_group": result})
