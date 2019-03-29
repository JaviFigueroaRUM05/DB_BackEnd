from flask import jsonify
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

    # tested - works
    def getAllGroups(self):
        dao = Chat_GroupsDAO()
        groups_list = dao.getAllGroups()
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result_list.append(result)
        return jsonify(Chat_groups=result_list)

    #tested - working
    # get groups a user belongs to
    def getGroupsUserBelongsTo(self, json):
        if not json.get('uid'):
            return jsonify(Error="No user logged in")
        uid = json.get('uid')
        dao = Chat_GroupsDAO()
        groups_list = dao.getGroupsUserBelongsTo(uid)
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result['isAdmin'] = row[3]
            result_list.append(result)
        return jsonify(Chat_groups=result_list)

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

    def createNewGroup(self, g_info):
        dao = Chat_GroupsDAO()
        gname = g_info['gname']
        gphoto = g_info['gphoto']
        gadmin = g_info['gadmin']

        gid = dao.createNewGroup(gname=gname, gphoto=gphoto, gadmin=gadmin)
        g_info['gid']=gid
        return jsonify(g_info)

    #get users in a specific group
    def getAllUsersByGroup(self, gid):
        # dao = Chat_GroupsDAO()
        # groups_list = dao.getUsersByGroup(gid)
        # result_list = []
        # for row in groups_list:
        #     result = {}
        #     result['uid'] = row[0]
        #     result['uname'] = row[1]
        #     result_list.append(result)
        # return jsonify(Users_in_Chat=result_list)
        result = []
        if gid == 1:
            result.append(self.users[0])
            result.append(self.users[1])
            return jsonify(result)
        elif gid == 2:
            result.append(self.users[2])
            result.append(self.users[3])
            return jsonify(result)
        else:
            return jsonify("Group not found")

    def addUserToGroup(self, new_user):
        # dao = Chat_GroupsDAO()
        # if gid and gname and uid and uname:
        #     if dao.getUserInGroup(gid, uid):
        #         return jsonify(Error="User Already in Group"), 400
        #     else:
        #         g_id = dao.addUserToGroup(gid, gname, uid, uname)
        #         return jsonify(g_id)
        # else:
        #     return jsonify(Error="Unexpected attributes in post request"), 400
        new_user['uid'] = 6
        self.users.append(new_user)
        return jsonify(new_user)

    def removeUserFromGroup(self, gid, uid):
        # dao = Chat_GroupsDAO()
        # if not dao.getUserInGroup(gid, uid):
        #     return jsonify(Error = "User not found."), 404
        # else:
        #     dao.deleteUserFromGroup(gid, uid)
        #     return jsonify(DeleteStatus = "OK"), 200
        return jsonify(self.users[0])


    def deleteGroup(self, gid):
        # dao = Chat_GroupsDAO()
        # if not dao.getGroupById(gid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
        #     dao.deleteGroup(gid)
        #     return jsonify(DeleteStatus = "OK"), 200
    
        return jsonify(self.groups[0])
