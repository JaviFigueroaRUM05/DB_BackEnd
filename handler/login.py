from flask import jsonify
from dao.login import LoginDAO

CREATENEWUSERKEYS = ['uname', 'email', 'password', 'first_name', 'last_name']
LOGINKEYS = ['email', 'password']


class LoginHandler:

    def build_login_dict(self, email, password):
        result = {}
        result['email'] = email
        result['password'] = password
        return result

    def _getUserLoginInfo(self, email):
        dao = LoginDAO()
        userPassword = dao.getUserPassword(email)
        if not userPassword:
            return None
        else:
            return userPassword[0]

        # Currently checks if password is password

    def attemptUserLogin(self, json):
        # When ready to implement, uncomment this line.
        # userPassword = self._getUserLoginInfo(email)

        for key in LOGINKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)

        userPassword = 'password'
        if (userPassword == None):
            return jsonify(Error="User email not found."), 404
        else:
            loginAttempt = {}
            loginAttempt['email'] = json['email']
            if json['password'] == userPassword:
                loginAttempt['login'] = 'Success'
                loginAttempt['uid'] = '5'
            else:
                loginAttempt['login'] = 'Failure'
            return jsonify(loginAttempt)

    # currently returns email as available
    def confirmNewUser(self, email):
        # When ready to implement, uncomment these lines
        # dao = LoginDAO()
        # user = dao.getUserByEmail(email)

        # Defaults user as available
        user = []
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet
        else:
            confirmed = {}
            confirmed['email'] = email
            confirmed['availability'] = 'available'
            return jsonify(confirmed)

    # Todo Move some of this logic into sql in DAO
    def createNewUser(self, json):
        # When ready, ucmooment these lines
        dao = LoginDAO()
        # user = dao.getUserByEmail(credentials['email'])

        for key in CREATENEWUSERKEYS:
            if key not in json:
                return jsonify(Error='Missing credentials from submission: ' + key)

        # TODO remove this, just pass in the json, and handle any errors
        # sent back from the DB.
        # default to valid new user
        user = []
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet

        else:
            # When ready, ucomment this line
            uid = dao.insertNewUser(uname=json['uname'], email=json['email'],
                                    password=json['password'], fname=json['first_name'],
                                    lname=json['last_name'])
            response = {'uid': uid}
            return jsonify(response)
