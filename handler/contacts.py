from flask import jsonify
from dao.contacts import ContactsDAO


class ContactsHandler:

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


    def addContact(self, uid, cid):
        # Verify user/cid
        # create new entry if not existant
        # dao= ContactsDAO()
        # addResult = dao.addContactById(uid=uid, cid=cid)
        # if not addResult:
        #     return jsonify(Error='The contact you are trying to '
        #                          'add does not exist.')

        # Hardcoded response JSON
        addResult = {"contactCreated": True}

        return jsonify(addResult)


    def removeContact(self, uid, cid):
        # Verify user/cid
        # delete entry if existant
        # dao = ContactsDAO()
        # removalResult = dao.removeContactById(uid=uid, cid=cid)

        # Hardcoded REsponse Json
        removalResult = {"entriesDeleted": 1}

        return jsonify(removalResult)
