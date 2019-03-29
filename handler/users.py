from flask import jsonify
from psycopg2 import IntegrityError
from dao.contacts import ContactsDAO
from dao.users import UsersDAO

ADDCONTACTNAMEKEYS = ['first_name', 'last_name']
CREATENEWUSERKEYS = ['uname', 'email', 'password', 'first_name', 'last_name', 'phone']
LOGINKEYS = ['email', 'password']

class UserHandler:

    def _buildUserResponse(self, user_tuple):
        response = {}
        response['uid'] = user_tuple[0]
        response['uname'] = user_tuple[1]
        response['first_name'] = user_tuple[2]
        response['last_name'] = user_tuple[3]
        response['email'] = user_tuple[4]
        response['phone'] = user_tuple[5]
        return response

    # How do I handle duplicates/errors?
    def createNewUser(self, json):
        for key in CREATENEWUSERKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key), 400
        dao = UsersDAO()
        try:
            uid = dao.insertNewUser(uname=json['uname'], email=json['email'],
                                    password=json['password'], first_name=json['first_name'],
                                    last_name=json['last_name'], phone=json['phone'])
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

        return jsonify({'uid': uid}), 201

    def attemptUserLogin(self, json):
        for key in LOGINKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)
        dao = UsersDAO()
        userID = dao.getIdByLogin(email=json['email'], password=json['password'])
        if userID is None:
            return jsonify(Error="Invalid email or password."), 400
        else:
            return jsonify({"uid": userID[0]}), 202


    # Do I need json for dashboard?
    def getAllUsersInfo(self):
        dao = UsersDAO()
        users = dao.getAllUsersInfo()
        UserList = []
        for user in users:
            UserList.append(self._buildUserResponse(user_tuple=user))
        response = {'contacts': UserList}
        return jsonify(response)

    def getUserInfoByID(self, uid):
        dao = UsersDAO()
        user = dao.getUserInfoByID(uid=uid)
        if not user:
            return jsonify(Error='User does not exist: '+ str(uid)), 404
        else:
            response = self._buildUserResponse(user_tuple=user)
        return jsonify(response)

    def getUserInfoByUname(self, uname):
        dao = UsersDAO()
        user = dao.getUserInfoByUname(uname=uname)
        if not user:
            return jsonify(Error='User does not exist: ' + str(uname)), 404
        else:
            response = self._buildUserResponse(user_tuple=user)
        return jsonify(response)

    def getAllContacts(self, uid):
        dao = ContactsDAO()
        contacts = dao.getUserContacts(uid=uid)
        contactList = []
        for contact in contacts:
            contactList.append(self._buildUserResponse(user_tuple=contact))
        response = {'contacts': contactList}
        return jsonify(response)

    def getSpecificContact(self, uid, cid):
        dao = ContactsDAO()
        contact = dao.getContactById(uid=uid, cid=cid)
        if not contact:
            return jsonify(Error='User does not have this contact '
                                 'in their contact list: ' + str(cid)), 404
        else:
            response = self._buildUserResponse(user_tuple=contact)
        return jsonify(response)

# ==========================================================================================

    def addContact(self, uid, json):
        # TODO Verify this is functional with new tables once implemented
        for key in ADDCONTACTNAMEKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)

        dao = ContactsDAO()

        if json.get('email'):
            addResult = dao.addContactByEmail(uid=uid, fname=json['first_name'],
                                              lname=json['lname'], email=json['email'])
        elif json.get('phone'):
            addResult = dao.addContactByPhone(uid=uid, fname=json["fname"],
                                              lname=json["lname"], phone=json["phone"])
        if not addResult:
            return jsonify(Error='The contact you are trying to '
                                 'add does not exist.')

        return jsonify(addResult)


    def removeContact(self, uid, cid):
        # Verify user/cid
        # delete entry if existant
        dao = ContactsDAO()
        removalResult = dao.removeContactById(uid=uid, cid=cid)

        # Hardcoded REsponse Json
        # removalResult = {"entriesDeleted": 1}

        return jsonify(removalResult)
