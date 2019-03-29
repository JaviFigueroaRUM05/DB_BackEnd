from flask import jsonify
from dao.login import LoginDAO

CREATENEWUSERKEYS = ['uname', 'email', 'password', 'first_name', 'last_name']
LOGINKEYS = ['email', 'password']


class LoginHandler:



    def attemptUserLogin(self, json):
        for key in LOGINKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)
        dao = LoginDAO()
        userID = dao.getIdByLogin(email=json['email'], password=json['password'])
        if (userID == None):
            return jsonify(Error="Invalid email or password."), 400
        else:
            return jsonify({"uid":userID}), 202
