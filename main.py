from flask import Flask, jsonify, request
from handler.contacts import ContactsHandler
from handler.login import LoginHandler
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
