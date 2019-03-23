from flask import jsonify
from dao.contacts import ContactsDAO

ADDCONTACTNAMEKEYS = ['first_name', 'last_name']
class UserHandler:

    # Iterator keys for verifying needed keys




    def getAllContacts(self, uid):
        # dao = ContactsDAO()
        # contacts = dao.getUserContacts(uid=uid)
        # contactList = {}
        # for contactID in contacts:
        #     contactList[str(contactID[0])] = self._getContactByID(contactID[0])

        # Hardcoded response json
        contactList={
                      'uid': uid,
                      "2": {
                        "fname": "Manuel",
                        "lname": "DB",
                        "uname": "manueldb"
                      },
                      "3": {
                        "fname": "Juan",
                        "lname": "Dalmau",
                        "uname": "testname"
                      }
                    }

        return jsonify(contactList)

    def getSpecificContact(self, uid, cid):
        # dao = ContactsDAO()
        # contact = dao.verifyContactById(uid=uid, cid=cid)
        # if not contact:
        #     return jsonify(Error='contact not found')
        # result = {
        #     cid: self._getContactByID(cid)
        # }

        # Hardcoded result
        result = {
                    'uid': uid,
                    'cid': cid,
                    "2": {
                        "fname": "Manuel",
                        "lname": "DB",
                        "uname": "manueldb"
                      }}
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
        # dao = ContactsDAO()
        # if email:
        #  addResult = dao.addContactByEmail(uid=uid, fname=fname,
        #                                    lname=lname, email=email)
        # elif phone > 0:
        #  addResult = dao.addContactByPhone(uid=uid, fname=fname,
        #                                    lname=lname, phone=phone)
        # if not addResult:
        #     return jsonify(Error='The contact you are trying to '
        #                          'add does not exist.')

        # Hardcoded response JSON
        addResult = {"contactCreated": True}

        for key in ADDCONTACTNAMEKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)

        if json.get('email'):
            addContactByEmail() #TODO implement
        if json.get('phone'):
            addContactByEmail() # TODO implement.
        else:
            return jsonify(Error="Neither email nor phone submitted.")

        return jsonify(addResult)


    def removeContact(self, uid, cid):
        # Verify user/cid
        # delete entry if existant
        # dao = ContactsDAO()
        # removalResult = dao.removeContactById(uid=uid, cid=cid)

        # Hardcoded REsponse Json
        removalResult = {"entriesDeleted": 1}

        return jsonify(removalResult)
