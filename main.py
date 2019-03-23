from flask import Flask, jsonify, request
from handler.user import UserHandler
from handler.login import LoginHandler
from handler.chat_groups import Chat_GroupsHandler
from handler.posts import PostsHandler
from handler.interactions import InteractionHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

# Iterator keys for verifying needed keys
CREATENEWUSERKEYS =['uname', 'email', 'password', 'first_name', 'last_name']
LOGINKEYS = ['email', 'password']
ADDCONTACTNAMEKEYS = ['first_name', 'last_name']


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App! Sofia is currently trying to make things work in group related routes.'


# Registers a new user using json data.
@app.route('/user/register', methods=['POST'])
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


# Uses json data to login user (email only)
@app.route('/user/login', methods=['POST'])
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


# Gets User Contacts
@app.route('/user/<int:uid>', methods=['GET'])
def getUserInfo(uid):
    if request.method == 'GET':
        return UserHandler().getUserInfo(uid=uid) #TODO Implement Handler.
    else:
        return jsonify(Error="Method not allowed."), 405


# Gets User Contacts
@app.route('/user/<int:uid>/contacts', methods=['GET'])
def getAllContacts(uid):
    if request.method == 'GET':
        return UserHandler().getAllContacts(uid=uid)
    else:
        return jsonify(Error="Method not allowed."), 405


# get a specific contact from a user's contact list.
@app.route('/user/<int:uid>/contacts/<int:cid>', methods=['GET'])
def getSpecificContact(uid, cid):
    if request.method == 'GET':
        return UserHandler().getSpecificContact(uid=uid,
                                                cid=cid)
    else:
        return jsonify(Error="Method not allowed."), 405


# Adds contact to user's contact list.
@app.route('/user/<int:uid>/add-contact', methods=['POST'])
def addContact(uid):
    if request.method == 'POST':
        for key in ADDCONTACTNAMEKEYS:
            if key not in request.json:
                return jsonify(Error='Missing credentials from submission: ' + key)
        if request.json.get('email'):
            return UserHandler().addContact(uid=uid,
                                            fname=request.json['fname'],
                                            lname=request.json['lname'],
                                            email=request.json['email'])
        elif request.json.get('phone'):
            return UserHandler().addContact(uid=uid,
                                            fname=request.json['fname'],
                                            lname=request.json['lname'],
                                            phone=request.json['phone'])
        else:
            return jsonify(Error='Missing credentials from submission; '
                                 'Please submit either an email or phone number.')
    else:
        return jsonify(Error="Method not allowed."), 405


# Delete a contact from a user's contact list.
@app.route('/user/<int:uid>/delete-contact/<int:cid>', methods=['DELETE'])
def deleteContact(uid, cid):
    if request.method == 'DELETE':
        return UserHandler().removeContact(uid=uid,
                                           cid=cid)
    else:
        return jsonify(Error="Method not allowed."), 405


# Get all users in the system.
@app.route('/dashboard/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        return UserHandler().getAllUsers()  #TODO Implement Handler and verification.
    else:
        return jsonify(Error="Method not allowed."), 405


# Get info on a specific user.
@app.route('/dashboard/users/<int:uid>', methods=['GET'])
def getSpecificUser():
    if request.method == 'GET':
        return UserHandler().getSpecificUser()  #TODO Implement Handler and verification.
    else:
        return jsonify(Error="Method not allowed."), 405

# Get the contacts of a specific user.
@app.route('/dashboard/users/<int:uid>/contacts', methods=['GET'])
def getSpecificUserContacts():
    if request.method == 'GET':
        return UserHandler().getSpecificUserContacts()  #TODO Implement Handler and verification.
    else:
        return jsonify(Error="Method not allowed."), 405

# ------------------------- Group Routes ----------------------------------------

# tested- see all groups available and add a group
@app.route('/api/chat-groups/groups', methods=['POST', 'GET'])
def getAllChatGroups():
    if request.method == 'POST':
        json = request.get_json()
        try:
            g_info           = {}
            g_info['gname']  = json['gname']
            g_info['gphoto'] = json['gphoto']
        except:
            return jsonify(Error="Unexpected attribute in POST request."), 405
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
        json = request.get_json()
        try:
            credentials             = {}
            credentials['uname']    = json['uname']
            credentials['email']    = json['email']
            credentials['password'] = json['password']
            credentials['fname']    = json['fname']
            credentials['lname']    = json['lname']
        except:
            return jsonify(Error="Unexpected attribute in POST request."), 405
        return Chat_GroupsHandler().addUserToGroup(credentials)

    elif request.method == 'DELETE':
        return Chat_GroupsHandler().removeUserFromGroup(gid, uid)
    
    else:
        return jsonify(Error="Method not allowed."), 405

# ---------------------------- Post Routes --------------------------------------------------


@app.route('/api/posts/group/<int:id>', methods=['POST', 'GET'])
def getGroupPosts(id):
    if request.method == 'POST':
        json = request.get_json()
        try:
            p_info              = {}
            p_info['post_date'] = json['post_date']
            p_info['media']     = json['media']
            p_info['message']   = json['message']
        except:
            return jsonify(Error="Unexpected attribute in POST request."), 405
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

#------------------------------ Interactions -----------------------------------

@app.route('/api/posts/<int:pid>', methods=['PUT', 'POST'])
def updateInteraction(pid):
    if request.method == 'PUT':
        #data = request.get_json()
        return InteractionHandler().updateReaction(pid, request.json)
    elif request.method == 'POST':
        return InteractionHandler().postReply(pid, request.json)

if __name__ == '__main__':
    app.run(debug=True)
