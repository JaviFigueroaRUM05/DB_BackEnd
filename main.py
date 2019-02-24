from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler
from handler.login import LoginHandler
from handler.chat_groups import Chat_GroupsHandler
from handler.posts import PostsHandler
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


@app.route('/login/submit', methods=['GET'])
def attemptLogin():
    if request.method == 'GET':
        return LoginHandler().attemptUserLogin(
            email='brianrodrig@gail.com',
            password='pasword')
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/NewUser/submit', methods=['GET', 'POST'])
def createNewUser():
    if request.method == 'GET':
        return LoginHandler().confirmNewUser(email='brianrdrg@gmail.com')
    else:
        credentials={}
        credentials['uname']='testname'
        credentials['email']='abc@upr.edu'
        credentials['password']='testpass'
        credentials['fname']='Juan'
        credentials['lname']='Dalmau'

        return LoginHandler().createNewUser(credentials=credentials)

# ------------------------- Group Routes ----------------------------------------

#tested- see all groups available and add a group
@app.route('/api/chat-groups/groups', methods=['POST', 'GET'])
def getAllChatGroups():
    if request.method == 'POST':
        g_info = {}
        g_info['gname']='group1'
        g_info['gphoto']='default'
        return Chat_GroupsHandler().createNewGroup(g_info=g_info)
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllGroups()
    else:
        return jsonify(Error="Method not allowed."), 405

#tested - method to get the groups a user belongs to
@app.route('/api/chat-groups/groups/<int:id>', methods=['GET','DELETE'])
def getChatGroupsByUser(id):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllGroupsByUser(id)
    if request.method == 'DELETE':
        return Chat_GroupsHandler().deleteGroup(id)
    else:
        return jsonify(Error="Method not allowed."), 405

#tested - method to get the users of a certain group
@app.route('/api/chat-groups/users/<int:gid>', methods=['GET'])
def getUsersInGroup(gid):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllUsersByGroup(gid)
    else:
        return jsonify(Error="Method not allowed."), 405

#tested
@app.route('/api/chat-groups/users/<int:gid>/<int:uid>', methods=['POST', 'DELETE'])
def modUsersInGroup(gid, uid):
    if request.method == 'POST':
        credentials={}
        credentials['uname']='testname'
        credentials['email']='abc@upr.edu'
        credentials['password']='testpass'
        credentials['fname']='Juan'
        credentials['lname']='Dalmau'
        return Chat_GroupsHandler().addUserToGroup(credentials)
    elif request.method == 'DELETE':
        return Chat_GroupsHandler().removeUserFromGroup(gid, uid)
    else:
        return jsonify(Error="Method not allowed."), 405

#---------------------------- Post Routes --------------------------------------------------

@app.route('/api/posts/group/<int:id>', methods=['POST', 'GET'])
def getGroupPosts(id):
    if request.method == 'POST':
        p_info={}
        p_info['post_date'] = '2019-06-23'
        p_info['media'] = 'default'
        p_info['message'] = 'I hope everything is going well'
        return PostsHandler().createNewPost(p_info=p_info)
    elif request.method == 'GET':
        return PostsHandler().getPostsByGroup(id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/api/posts/user/<int:id>', methods=['GET'])
def getUserPosts(id):
    if request.method == 'GET':
        return PostsHandler().getPostsByUser(id)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run(debug=True)
