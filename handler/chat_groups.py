from flask import jsonify
from dao.chat_groups import Chat_GroupsDAO

class Chat_GroupsHandler:

    def build_chat_groups_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gphoto'] = row[2]
        result['gadmin'] = row[3]
        return result

    def build_chat_group_attributes(self, gid, gname, gphoto, gadmin):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gphoto'] = gphoto
        result['gadmin'] = gadmin
        return result

    def getAllGroups(self):
        dao = Chat_GroupsDAO()
        groups_list = dao.getAllGroups()
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result_list.append(result)
        return jsonify(Chat_groups=result_list)

    def createNewGroup(self, g_info):
        dao = Chat_GroupsDAO()
        gname = g_info['gname']
        gphoto = g_info['gphoto']
        gadmin = g_info['gadmin']

        gid = dao.createNewGroup(gname=gname, gphoto=gphoto, gadmin=gadmin)
        g_info['gid']=gid
        return jsonify(g_info)

    def getGroupById(self, gid):
        dao = Chat_GroupsDAO()
        row = dao.getGroupById(gid)
        if not row:
            return jsonify(Error = "Group Not Found"), 404
        else:
            return row[1]

    #get groups a user belongs to
    def getAllGroupsByUser(self, uid):
        dao = Chat_GroupsDAO()
        groups_list = dao.getGroupsByUser(uid)
        result_list = []
        for row in groups_list:
            result = self.build_chat_groups_dict(row)
            result_list.append(result)
        return jsonify(Chat_groups=result_list)

    #get users in a specific group
    def getAllUsersByGroup(self, gid):
        dao = Chat_GroupsDAO()
        groups_list = dao.getUsersByGroup(gid)
        result_list = []
        for row in groups_list:
            result = {}
            result['uid'] = row[0]
            result['uname'] = row[1]
            result_list.append(result)
        return jsonify(Users_in_Chat=result_list)

    def addUserToGroup(self, gid, gname, uid, uname):
        dao = Chat_GroupsDAO()
        if gid and gname and uid and uname:
            if dao.getUserInGroup(gid, uid):
                return jsonify(Error="User Already in Group"), 400
            else:
                g_id = dao.addUserToGroup(gid, gname, uid, uname)
                return jsonify(g_id)
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def removeUserFromGroup(self, gid, uid):
        dao = Chat_GroupsDAO()
        if not dao.getUserInGroup(gid, uid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.deleteUserFromGroup(gid, uid)
            return jsonify(DeleteStatus = "OK"), 200

    def deleteGroup(self, gid):
        dao = Chat_GroupsDAO()
        if not dao.getGroupById(gid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.deleteGroup(gid)
            return jsonify(DeleteStatus = "OK"), 200
