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

# Old routes
@app.route('/PartApp/parts', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        # cambie a request.json pq el form no estaba bregando
        # parece q estaba poseido por satanas ...
        # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
        print("REQUEST: ", request.json)
        return PartHandler().insertPartJson(request.json)
    else:
        if not request.args:
            return PartHandler().getAllParts()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getPartById(pid):
    if request.method == 'GET':
        return PartHandler().getPartById(pid)
    elif request.method == 'PUT':
        return PartHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return PartHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    return PartHandler().getSuppliersByPartId(pid)

@app.route('/PartApp/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else :
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)

@app.route('/PartApp/suppliers/<int:sid>',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

@app.route('/PartApp/parts/countbypartid')
def getCountByPartId():
    return PartHandler().getCountByPartId()

if __name__ == '__main__':
    app.run(debug=True)
