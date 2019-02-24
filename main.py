from flask import Flask, jsonify, request
from handler.contacts import ContactsHandler
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

# Iterator keys for verifying needed keys
CREATENEWUSERKEYS =['uname', 'email', 'password', 'fname', 'lname']
LOGINKEYS = ['email', 'password']
ADDCONTACTNAMEKEYS = ['fname', 'lname']


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App! Sofia is currently trying to make things work in group related routes.'


# Uses json data to login user (email only)
# Tested and Hardcoded
@app.route('/api/login', methods=['POST'])
def attemptLogin():
    if request.method == 'POST':
        for key in LOGINKEYS:
            if key not in request.json:
                return jsonify(Error='Missing credentials from submission: ' + key)
        return LoginHandler().attemptUserLogin(
            email=request.json['email'],
            password=request.json['password'])
    else:
        return jsonify(Error="Method not allowed."), 405


# Registers a new user using json data.
# Tested and hardcoded
@app.route('/api/register-user', methods=['POST'])
def createNewUser():
    if request.method == 'POST':
        credentials = {}
        for key in CREATENEWUSERKEYS:
            if key not in request.json:
                return jsonify(Error='Missing credentials from submission: '+ key)
            else:
                credentials[key] = request.json[key]
        return LoginHandler().createNewUser(credentials=credentials)
    else:
        return jsonify(Error="Method not allowed."), 405


# Gets user contacts, adds or deletes user contacts using json data
# Tested and hardcoded
# TODO Verify user is uid user
@app.route('/api/contacts/<int:uid>', methods=['GET','POST'])
def getAllContacts(uid):
    if request.method == 'GET':
        return ContactsHandler().getAllContacts(uid=uid)
    if request.method == 'POST':
        for key in ADDCONTACTNAMEKEYS:
            if key not in request.json:
                return jsonify(Error='Missing credentials from submission: ' + key)
        if request.json.get('email'):
            return ContactsHandler().addContact(uid=uid,
                                                fname=request.json['fname'],
                                                lname=request.json['lname'],
                                                email=request.json['email'])
        elif request.json.get('phone'):
            return ContactsHandler().addContact(uid=uid,
                                                fname=request.json['fname'],
                                                lname=request.json['lname'],
                                                phone=request.json['phone'])
        else:
            return jsonify(Error='Missing credentials from submission; '
                                 'Please submit either an email or phone number.')
    else:
        return jsonify(Error="Method not allowed."), 405

# TODO Verify user is uid user
@app.route('/api/contacts/<int:uid>/<int:cid>', methods=['GET','DELETE'])
def deleteContact(uid, cid):
    if request.method == 'DELETE':
        return ContactsHandler().removeContact(uid=uid,
                                               cid=cid)
    if request.method == 'GET':
        return ContactsHandler().getSpecificContact(uid=uid,
                                                    cid=cid)
    else:
        return jsonify(Error="Method not allowed."), 405


# ------------------------- Group Routes ----------------------------------------

# tested- see all groups available and add a group
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


# tested - method to get the groups a user belongs to
@app.route('/api/chat-groups/groups/<int:id>', methods=['GET','DELETE'])
def getChatGroupsByUser(id):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllGroupsByUser(id)
    if request.method == 'DELETE':
        return Chat_GroupsHandler().deleteGroup(id)
    else:
        return jsonify(Error="Method not allowed."), 405


# tested - method to get the users of a certain group
@app.route('/api/chat-groups/users/<int:gid>', methods=['GET'])
def getUsersInGroup(gid):
    if request.method == 'GET':
        return Chat_GroupsHandler().getAllUsersByGroup(gid)
    else:
        return jsonify(Error="Method not allowed."), 405


# tested
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

# ---------------------------- Post Routes --------------------------------------------------


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
