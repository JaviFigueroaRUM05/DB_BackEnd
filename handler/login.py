from flask import jsonify
from dao.login import LoginDAO


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

    def getUserbyId(self, id):
        dao = LoginDAO()
        user = dao.getUserById(id)
        if not user:
            return None
        else:
            return user[1]


    def attemptUserLogin(self, email, password):
        userPassword = self._getUserLoginInfo(email)
        if (userPassword==None):
            return jsonify(Error="User email not found."), 404
        else:
            loginAttempt={}
            loginAttempt['email']=email
            if password==userPassword:
                loginAttempt['login']='Success'
            else:
                loginAttempt['login'] = 'Failure'
            return jsonify(loginAttempt)


    def confirmNewUser(self, email):
        dao = LoginDAO()
        user = dao.getUserByEmail(email)
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet
        else:
            confirmed={}
            confirmed['email']=email
            confirmed['availability']='available'
            return jsonify(confirmed)

    def createNewUser(self, credentials):
        dao = LoginDAO()
        user = dao.getUserByEmail(credentials['email'])
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet
        else:
            uname = credentials['uname']
            email = credentials['email']
            password = credentials['password']
            fname = credentials['fname']
            lname = credentials['lname']
            uid = dao.insertNewUser(uname=uname, email=email,
                                    password=password, fname=fname,
                                    lname=lname)
            credentials['uid']=uid
            return jsonify(credentials)
