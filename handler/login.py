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


        # Currently checks if password is password
    def attemptUserLogin(self, email, password):
        # When ready to implement, uncomment this line.
        # userPassword = self._getUserLoginInfo(email)

        userPassword = 'password'
        if (userPassword==None):
            return jsonify(Error="User email not found."), 404
        else:
            loginAttempt={}
            loginAttempt['email']=email
            if password==userPassword:
                loginAttempt['login']='Success'
                loginAttempt['uid']='5'
            else:
                loginAttempt['login'] = 'Failure'
            return jsonify(loginAttempt)



    # currently returns email as available
    def confirmNewUser(self, email):
        # When ready to implement, uncomment these lines
        #dao = LoginDAO()
        #user = dao.getUserByEmail(email)

       # Defaults user as available
        user=[]
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet
        else:
            confirmed={}
            confirmed['email']=email
            confirmed['availability']='available'
            return jsonify(confirmed)



# Todo Move some of this logic into sql in DAO
    def createNewUser(self, credentials):
        # When ready, ucmooment these lines
        #dao = LoginDAO()
        #user = dao.getUserByEmail(credentials['email'])


        #default to valid new user
        user = []
        if user:
            return jsonify(Error="User email already exists"), 300  # Don't know codes yet
        else:
            uname = credentials['uname']
            email = credentials['email']
            password = credentials['password']
            fname = credentials['fname']
            lname = credentials['lname']

           #Default value for testing
            response={}
            response['uid']=69
           # When ready, ucomment this line
           # uid = dao.insertNewUser(uname=uname, email=email,
           #                          password=password, fname=fname,
           #                          lname=lname)
            return jsonify(response)


   # Old methods

    def insertPart(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:
            pname = form['pname']
            pprice = form['pprice']
            pmaterial = form['pmaterial']
            pcolor = form['pcolor']
            if pcolor and pprice and pmaterial and pname:
                dao = PartsDAO()
                pid = dao.insert(pname, pcolor, pmaterial, pprice)
                result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertPartJson(self, json):
        pname = json['pname']
        pprice = json['pprice']
        pmaterial = json['pmaterial']
        pcolor = json['pcolor']
        if pcolor and pprice and pmaterial and pname:
            dao = PartsDAO()
            pid = dao.insert(pname, pcolor, pmaterial, pprice)
            result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePart(self, pid):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePart(self, pid, form):
        dao = PartsDAO()
        if not dao.getPartById(pid):
            return jsonify(Error = "Part not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                pname = form['pname']
                pprice = form['pprice']
                pmaterial = form['pmaterial']
                pcolor = form['pcolor']
                if pcolor and pprice and pmaterial and pname:
                    dao.update(pid, pname, pcolor, pmaterial, pprice)
                    result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400