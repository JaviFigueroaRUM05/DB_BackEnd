from flask import Flask, jsonify, request
from handler.users import UserHandler
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


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App! Sofia is currently trying to make things work in group related routes.'


# Registers a new user using json data.
@app.route('/user/register', methods=['POST'])
def createNewUser():
    if request.method == 'POST': return UserHandler().createNewUser(json=request.json)
    else:                        return jsonify(Error="Method not allowed."), 405


# Uses json data to login user (email only)
@app.route('/user/login', methods=['POST'])
def attemptLogin():
    if request.method == 'POST': return UserHandler().attemptUserLogin(json=request.json)
    else:                        return jsonify(Error="Method not allowed."), 405


# Gets User by uid
@app.route('/user/uid=<int:uid>', methods=['GET'])
def getUserInfoByID(uid):
    if request.method == 'GET': return UserHandler().getUserInfoByID(uid=uid)
    else:                       return jsonify(Error="Method not allowed."), 405


# Gets User by uname
@app.route('/user/uname=<uname>', methods=['GET'])
def getUserInfoByUname(uname):
    if request.method == 'GET': return UserHandler().getUserInfoByUname(uname=uname)
    else:                       return jsonify(Error="Method not allowed."), 405


# Gets User Contacts
@app.route('/user/contacts', methods=['GET'])
def getAllContacts():
    if request.method == 'GET': return UserHandler().getAllContacts(uid=request.headers.get('Authorization'))
    else:                       return jsonify(Error="Method not allowed."), 405


# get a specific contact from a user's contact list.
@app.route('/user/contacts/<int:cid>', methods=['GET'])
def getSpecificContact(cid):
    if request.method == 'GET': return UserHandler().getSpecificContact(uid=request.headers.get('Authorization'),
                                                                        cid=cid)
    else:                       return jsonify(Error="Method not allowed."), 405


# Adds contact to user's contact list.
@app.route('/user/add-contact', methods=['POST'])
def addContact():
    if request.method == 'POST': return UserHandler().addContact(uid=request.headers.get('Authorization'),
                                                                 json=request.json)
    else:                        return jsonify(Error="Method not allowed."), 405


# Delete a contact from a user's contact list.
@app.route('/user/delete-contact/<int:cid>', methods=['DELETE'])
def deleteContact(cid):
    if request.method == 'DELETE': return UserHandler().removeContact(uid=request.headers.get('Authorization'),
                                                                      cid=cid)
    else:                          return jsonify(Error="Method not allowed."), 405


# Get all users in the system.
@app.route('/dashboard/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET': return UserHandler().getAllUsersInfo()
    else:                       return jsonify(Error="Method not allowed."), 405


# Get info on a specific user.
# This route, though seperate, is redundant with /user/uid=<int:uid>
@app.route('/dashboard/users/<int:uid>', methods=['GET'])
def getSpecificUser(uid):
    if request.method == 'GET': return UserHandler().getUserInfoByID(uid=uid)
    else:                       return jsonify(Error="Method not allowed."), 405


# Get the contacts of a specific user.
@app.route('/dashboard/users/<int:uid>/contacts', methods=['GET'])
def getSpecificUserContacts(uid):
    if request.method == 'GET': return UserHandler().getAllContactsDashboard(authUID=request.headers.get('Authorization'),
                                                                             uid=uid)
    else:                       return jsonify(Error="Method not allowed."), 405

# ------------------------- Group Routes ----------------------------------------

#tested - works
# method to get the groups a user belongs to
# Remember uid is passed through json
@app.route('/groups', methods=['GET'])
def getChatGroupsForUser():
    if request.method == 'GET': return Chat_GroupsHandler().getGroupsUserBelongsTo(request.headers.get('Authorization'))
    else:                       return jsonify(Error="Method not allowed."), 405

#tested - works
# method to get metadata of a group a user belongs to
@app.route('/groups/<int:gid>', methods=['GET'])
def getSpecificGroup(gid):
    if request.method == 'GET': return Chat_GroupsHandler().getGroupById(gid=gid)
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

# tested - works
# get all posts of a specified group
@app.route('/groups/<int:gid>/posts', methods=['GET'])
def getAllPostOfAGroup(gid):
    if request.method == 'GET': return PostsHandler().getPostsByGroup(gid)
    else:                       return jsonify(Error="Method not allowed."), 405

# tested - works
# get specific post from group
@app.route('/groups/<int:gid>/posts/<int:pid>', methods=['GET'])
def getSpecificPost(gid, pid):
    if request.method == 'GET': return PostsHandler().getPostsById(gid,pid)
    else:                       return jsonify(Error="Method not allowed."), 405

# reply to a specific group
@app.route('/groups/<int:gid>/reply', methods=['POST'])
def replyToPost(gid):
    if request.method == 'POST': return jsonify(Output="POST request received")
    else:                        return jsonify(Error="Method not allowed."), 405

# tested - works
# see all groups available
@app.route('/dashboard/groups', methods=['GET'])
def dash_GetAllChatGroups():
    if request.method == 'GET': return Chat_GroupsHandler().getAllGroups()
    else:                       return jsonify(Error="Method not allowed."), 405

# get specific group info
@app.route('/dashboard/groups/<int:gid>', methods=['GET'])
def dash_getSpecificGroup(gid):
    if request.method == 'GET':  return Chat_GroupsHandler().getGroupById(gid=gid)
    else:                        return jsonify(Error="Method not allowed."), 405

# get all posts from a specific group
@app.route('/dashboard/groups/<int:gid>/posts', methods=['GET'])
def dash_getPostsFromGroup(gid):
    if request.method == 'GET':  return PostsHandler().getPostsByGroup(gid)
    else:                        return jsonify(Error="Method not allowed."), 405


# TODO: connect to handlers
@app.route('/groups/<int:gid>/posts/<int:pid>/reaction', methods=['POST', 'PUT', 'DELETE'])
def interaction(gid, pid):
    if   request.method == 'POST':   return jsonify(Output="POST request received.")
    elif request.method == 'PUT':    return jsonify(Output="PUT request received.")
    elif request.method == 'DELETE': return jsonify(Output="DELETE request received.")
    else:                            return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/trending', methods=['GET'])
def dash_trending():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts', methods=['GET'])
def dash_posts():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/<int:pid>/replies', methods=['GET'])
def dash_replies(pid):
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/<int:pid>/reactions', methods=['GET'])
def dash_reactions(pid):
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/user/<int:uid>', methods=['GET'])
def dash_user_posts(uid):
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-posts', methods=['GET'])
def dash_daily_posts():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-posts/user/<int:uid>', methods=['GET'])
def dash_user_daily_posts(uid):
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-replies', methods=['GET'])
def dash_daily_replies():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-likes', methods=['GET'])
def dash_daily_likes():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-dislikes', methods=['GET'])
def dash_daily_dislikes():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/active-users', methods=['GET'])
def dash_active_users():
    if request.method == 'GET': return jsonify(Output="GET request received.")
    else:                       return jsonify(Error="Method not allowed."), 405

#------------------------------ Main -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)
