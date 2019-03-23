from flask import Flask, jsonify, request
from handler.contacts import ContactsHandler
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

# method to get the groups a user belongs to
@app.route('/groups', methods=['GET'])
def getChatGroupsForUser(id):
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                       return jsonify(Error="Method not allowed."), 405

# method to get specific chat group a user belongs to
@app.route('/groups/<int:gid>', methods=['GET'])
def getSpecificGroup(gid):
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                       return jsonify(Error="Method not allowed."), 405

# create new chat group
@app.route('/group/create', methods=['POST'])
def createGroup():
    if request.method == 'POST': return jsonify(Output="POST request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# add participant to specific chat group
@app.route('/groups/<int:gid>/add-participant', methods=['POST'])
def addParticipantsToGroup(gid):
    if request.method == 'POST': return jsonify(Output="POST request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# delete participants from a specific group
@app.route('/groups/<int:gid>/delete-participants', methods=['DELETE'])
def deleteparticipantsFromGroup(gid):
    if request.method == 'DELETE': return jsonify(Output="DELETE request received")
    else:                          return jsonify(Error="Method not allowed."), 405

# delete group (only for admins)
@app.route('/groups/<int:gid>/delete-group', methods=['DELETE'])
def deleteGroup(gid):
    if request.method == 'DELETE': return jsonify(Output="DELETE request received")
    else:                          return jsonify(Error="Method not allowed."), 405

# authors a post to the specified group
@app.route('/groups/<int:gid>/create-post', methods=['POST'])
def createPost(gid):
    if request.method == 'POST': return jsonify(Output="POST request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# get all posts of a specified group
@app.route('/groups/<int:gid>/posts', methods=['GET'])
def getAllPostOfAGroup(gid):
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                       return jsonify(Error="Method not allowed."), 405

# get specific post from group
@app.route('/groups/<int:gid>/posts/<int:pid>', methods=['GET'])
def getSpecificPost(gid, pid):
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                       return jsonify(Error="Method not allowed."), 405

# reply to a specific group
@app.route('/groups/<int:gid>/reply', methods=['POST'])
def replyToPost(gid):
    if request.method == 'POST': return jsonify(Output="POST request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# see all groups available
@app.route('/dashboard/groups', methods=['GET'])
def dash_GetAllChatGroups():
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                       return jsonify(Error="Method not allowed."), 405

# get specific group info
@app.route('/dashboard/groups/<int:gid>', methods=['GET'])
def dash_getSpecificGroup():
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# get all posts from a specific group
@app.route('/dashboard/groups/<int:gid>/posts', methods=['GET'])
def dash_getPostsFromGroup():
    if request.method == 'GET': return jsonify(Output="GET request received")
    else:                        return jsonify(Error="Method not allowed."), 405

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
