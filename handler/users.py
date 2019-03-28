from flask import jsonify
from dao.contacts import ContactsDAO
from dao.users import UsersDAO

ADDCONTACTNAMEKEYS = ['first_name', 'last_name']


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


    def getUserInfoByID(self, uid, json):
        dao = UsersDAO()
        user = dao.getUserInfoByID(uid=uid)
        if not user:
            return jsonify(Error='User does not exist: '+ str(uid)), 404
        else:
            response = self._buildUserResponse(user_tuple=user)
        return jsonify(response)

    def getUserInfoByUname(self, uname, json):
        dao = UsersDAO()
        user = dao.getUserInfoByUname(uname=uname)
        if not user:
            return jsonify(Error='User does not exist: ' + str(uname)), 404
        else:
            response = self._buildUserResponse(user_tuple=user)
        return jsonify(response)



#==========================================================================================
    def getAllContacts(self, uid):
        dao = ContactsDAO()
        contacts = dao.getUserContacts(uid=uid)
        contactList = {}
        for contactID in contacts:
            contactList[str(contactID[0])] = self._getContactByID(contactID[0])

        # Hardcoded response json
        # contactList={
        #               'uid': uid,
        #               "2": {
        #                 "fname": "Manuel",
        #                 "lname": "DB",
        #                 "uname": "manueldb"
        #               },
        #               "3": {
        #                 "fname": "Juan",
        #                 "lname": "Dalmau",
        #                 "uname": "testname"
        #               }
        #             }

        return jsonify(contactList)

    def getSpecificContact(self, uid, cid):
        dao = ContactsDAO()
        contact = dao.verifyContactById(uid=uid, cid=cid)
        if not contact:
            return jsonify(Error='contact not found')
        result = {
            cid: self._getContactByID(cid)
        }

        # Hardcoded result
        # result = {
        #             'uid': uid,
        #             'cid': cid,
        #             "2": {
        #                 "fname": "Manuel",
        #                 "lname": "DB",
        #                 "uname": "manueldb"
        #               }}


        return jsonify(result)

    def _getContactByID(self, uid):
        dao = ContactsDAO()
        contact = dao.getContactById(uid=uid)
        result = {}
        result['uname']=contact[0]
        result['fname']=contact[1]
        result['lname']=contact[2]
        if not contact:
            return 'User Not Found'
        return result

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
