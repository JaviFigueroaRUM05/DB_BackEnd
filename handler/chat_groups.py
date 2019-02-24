from flask import jsonify
from dao.chat_groups import Chat_GroupsDAO

class Chat_GroupsHandler:

    groups = [{
        'gid' : 1,
        'gname': 'los de la esquina',
        'gphoto' : 'default'
    },
    {
        'gid' : 2,
        'gname': 'el gara',
        'gphoto' : 'default',
    },
    {
        'gid' : 3,
        'gname': 'the cuchifrits',
        'gphoto' : 'default',
    },
    {
        'gid' : 4,
        'gname': 'DATA',
        'gphoto' : 'default',
    }
    ]

    users = [{
        'uid' : 1,
        'uname' : 'Pedr',
        'email' : 'p@upr.edu',
        'password' : 'pop',
        'fname' : 'pedro',
        'lname' : 'rodriguez'
    },
    {
        'uid' : 2,
        'uname' : 'user2',
        'email' : 'u2@upr.edu',
        'password' : 'user',
        'fname' : 'Juan',
        'lname' : 'rodriguez'
    },
    {
        'uid' : 3,
        'uname' : 'user3',
        'email' : 'u3@upr.edu',
        'password' : 'user',
        'fname' : 'Sancho',
        'lname' : 'Panza'
    },
    {
        'uid' : 4,
        'uname' : 'user4',
        'email' : 'u4@upr.edu',
        'password' : 'user',
        'fname' : 'Flora',
        'lname' : 'Morales'
    }]

    def build_chat_groups_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gphoto'] = row[2]
        return result

    def build_chat_group_attributes(self, gid, gname, gphoto):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gphoto'] = gphoto
        return result

    def getAllGroups(self):
        # dao = Chat_GroupsDAO()
        # groups_list = dao.getAllGroups()
        # result_list = []
        # for row in groups_list:
        #     result = self.build_chat_groups_dict(row)
        #     result_list.append(result)
        # return jsonify(Chat_groups=result_list)
        return jsonify(self.groups)

    def createNewGroup(self, g_info):
        # dao = Chat_GroupsDAO()
        # gname = g_info['gname']
        # gphoto = g_info['gphoto']
        # gadmin = g_info['gadmin']
        #
        # gid = dao.createNewGroup(gname=gname, gphoto=gphoto, gadmin=gadmin)
        # g_info['gid']=gid
        # return jsonify(g_info)
        g_info['gid']=5
        self.groups.append(g_info)
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
        # dao = Chat_GroupsDAO()
        # groups_list = dao.getGroupsByUser(uid)
        # result_list = []
        # for row in groups_list:
        #     result = self.build_chat_groups_dict(row)
        #     result_list.append(result)
        # return jsonify(Chat_groups=result_list)
        result = []
        if uid == 1:
            result.append(self.groups[0])
            result.append(self.groups[1])
            return jsonify(result)
        elif uid==2:
            result.append(self.groups[2])
            result.append(self.groups[3])
            return jsonify(result)
        else:
            return jsonify("User not found")


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
        return jsonify(self.user[0])


    def deleteGroup(self, gid):
        # dao = Chat_GroupsDAO()
        # if not dao.getGroupById(gid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
        #     dao.deleteGroup(gid)
        #     return jsonify(DeleteStatus = "OK"), 200
    
        return jsonify(self.groups[0])
