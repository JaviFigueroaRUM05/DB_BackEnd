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



   #Old methods

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




