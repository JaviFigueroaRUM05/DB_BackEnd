from flask import Flask, jsonify, request
from handler.users import UserHandler
from handler.chat_groups import Chat_GroupsHandler
from handler.posts import PostsHandler
from handler.interactions import InteractionHandler
from handler.dashboard import DashboardHandler

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

    # tested - works
    # method to get metadata of a group a user belongs to


@app.route('/groups/<int:gid>/admins', methods=['GET'])
def getSpecificGroupAdmins(gid):
    if request.method == 'GET': return Chat_GroupsHandler().getGroupAdmins(gid=gid)
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

# tested - works
# see all groups available
@app.route('/dashboard/groups/admins', methods=['GET'])
def dash_getAllAdmins():
    if request.method == 'GET': return Chat_GroupsHandler().getAllAdmins()
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
@app.route('/groups/<int:gid>/posts/<int:pid>/post-reaction', methods=['POST'])
def post_reaction(gid, pid):
    json = request.get_json()
    handler = InteractionHandler()
    uid = request.headers.get('Authorization')
    if   request.method == 'POST':   return handler.post_reaction(uid, pid, json)
    else:                            return jsonify(Error="Method not allowed."), 405


@app.route('/groups/<int:gid>/posts/<int:pid>/update-reaction', methods=['PUT'])
def update_reaction(gid, pid):
    json = request.get_json()
    handler = InteractionHandler()
    uid = request.headers.get('Authorization')
    if   request.method == 'PUT':    return handler.update_reaction(uid, pid, json)
    else:                            return jsonify(Error="Method not allowed."), 405


@app.route('/groups/<int:gid>/posts/<int:pid>/delete-reaction', methods=['DELETE'])
def delete_reaction(gid, pid):
    handler = InteractionHandler()
    uid = request.headers.get('Authorization')
    if   request.method == 'DELETE': return handler.delete_reaction(uid, pid)
    else:                            return jsonify(Error="Method not allowed."), 405


@app.route('/groups/<int:gid>/posts/<int:pid>/reaction', methods=['GET'])
def get_reaction(gid, pid):
    handler = InteractionHandler()
    uid = request.headers.get('Authorization')
    if   request.method == 'GET':    return handler.get_reaction(uid, pid)
    else:                            return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/trending', methods=['GET'])
def dash_trending():
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_trending_hashtag()
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts', methods=['GET'])
def dash_posts():
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_posts()
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/<int:pid>/replies', methods=['GET'])
def dash_replies(pid):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_replies_to_post(pid)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/<int:pid>/reactions', methods=['GET'])
def dash_reactions(pid):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_reactions_to_post(pid)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/posts/<int:pid>/reactions-count', methods=['GET'])
def dash_reactions_count(pid):
    handler = DashboardHandler()
    if request.method == 'GET' : return handler.get_reactions_count_to_post(pid)
    else                       : return jsonify(Error="Mathod not allowed."), 405

@app.route('/dashboard/posts/user/<int:uid>', methods=['GET'])
def dash_user_posts(uid):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_posts_by_user(uid)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-posts/<date>', methods=['GET'])
def dash_daily_posts(date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_posts_by_date(date)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-posts-count', methods=['GET'])
def dash_daily_posts_count():
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_posts_count_by_date()
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-posts/<date>/user/<int:uid>', methods=['GET'])
def dash_user_daily_posts(uid, date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_posts_by_user_date(uid, date)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-replies/<date>', methods=['GET'])
def dash_daily_replies(date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_all_replies_by_date(date)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-likes/<date>', methods=['GET'])
def dash_daily_likes(date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_likes_by_date(date)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/daily-dislikes/<date>', methods=['GET'])
def dash_daily_dislikes(date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_dislikes_by_date(date)
    else:                       return jsonify(Error="Method not allowed."), 405


@app.route('/dashboard/active-users/<date>', methods=['GET'])
def dash_active_users(date):
    handler = DashboardHandler()
    if request.method == 'GET': return handler.get_active_users_by_date(date)
    else:                       return jsonify(Error="Method not allowed."), 405

#------------------------------ Main -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)
