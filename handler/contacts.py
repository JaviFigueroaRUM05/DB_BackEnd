from flask import jsonify
from dao.contacts import ContactsDAO


class ContactsHandler:

    def getAllContacts(self, uid):
        # dao = ContactsDAO()
        # contacts = dao.getUserContacts(uid=uid)
        # contactList = {}
        # for contactID in contacts:
        #     print(contactID)
        #     contactList[str(contactID[0])]=self._getContactByID(contactID[0])
        # print (contactList)

        # Hardcoded response json
        contactList={
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
        result = {"2": {
                        "fname": "Manuel",
                        "lname": "DB",
                        "uname": "manueldb"
                      }}
        return jsonify(result)

    def _getContactByID(self, uid):
        dao = ContactsDAO()
        contact = dao.getContactById(uid=uid)
        result = {}
        result['uname']=contact[0][0]
        result['fname']=contact[0][1]
        result['lname']=contact[0][2]
        if not contact:
            return 'User Not Found'
        return result
