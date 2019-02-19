from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler
from handler.login import LoginHandler
from handler.chat_groups import Chat_GroupsHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App! Sofia is currently trying to make things work in group related routes.'

@app.route('/api/login/<email>&<password>', methods=['GET'])
def attemptLogin(email, password):
    if request.method == 'GET':
        return LoginHandler().attemptUserLogin(
            email=email,
            password=password)
    else:
        return jsonify(Error="Method not allowed."), 405



@app.route('/api/register-user', methods=['POST'])
def createNewUser():
    if request.method == 'POST':
        # Hardwired credential object
        credentials={}
        credentials['uname']='testname'
        credentials['email']='abc@upr.edu'
        credentials['password']='testpass'
        credentials['fname']='Juan'
        credentials['lname']='Dalmau'
        return LoginHandler().createNewUser(credentials=credentials)
    else:
        return jsonify(Error="Method not allowed."), 405


#tested
@app.route('/api/create-group', methods=['POST'])
def createNewGroup():
    g_info={}
    g_info['gname']='group1'
    g_info['gphoto']='default'
    g_info['gadmin']=1
    return Chat_GroupsHandler().createNewGroup(g_info=g_info)

#tested - method to get the groups a user belongs to
@app.route('/api/groups/<int:uid>', methods=['GET'])
def groupsByUser(uid):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllGroupsByUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

#tested - method to get the users of a certain group
@app.route('/api/group-users/<int:gid>', methods=['GET'])
def usersInGroup(gid):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllUsersByGroup(gid)
    else:
        return jsonify(Error="Method not allowed."), 405

#tested
@app.route('/api/groups/<int:gid>/<int:uid>', methods=['POST', 'DELETE'])
def UsersInGroup(gid, uid):
    if request.method == 'POST':
        uname = LoginHandler().getUserbyId(uid)
        gname = Chat_GroupsHandler().getGroupById(gid)
        return Chat_GroupsHandler().addUserToGroup(gid, gname, uid, uname)
    elif request.method == 'DELETE':
        return Chat_GroupsHandler().removeUserFromGroup(gid, uid)
    else:
        return jsonify(Error="Method not allowed."), 405

#tested
@app.route('/api/groups/<int:gid>', methods=['DELETE'])
def removeGroup(gid):
    if request.method == 'DELETE':
        return Chat_GroupsHandler().deleteGroup(gid)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run(debug=True)
