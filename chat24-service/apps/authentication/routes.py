
from datetime import datetime
import uuid
from flask import request, jsonify
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)
from sqlalchemy import null

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.auth_util import requires_access_level
from apps.authentication.models import ROLE, Users
from datetime import datetime
from apps.authentication.crypto_util import verify_pass,getJwtBearerToken

# Login & Registration
class AuthController:

    @blueprint.route('/api/v1/login', methods=['POST'])
    def login():
            # read form data
            username = null
            password = null
            authProvider = ""
            email =""
            role=ROLE['guest']
            loginMode = request.form['mode']
            ip_address = request.remote_addr
            user = null
            isNewUser= False
            if loginMode == 'admin':
                username = request.form['username']
                password = request.form['password']   
                user = Users.query.filter_by(email=username).first() 
                role=ROLE['admin']
                if user is None or user.role != ROLE['admin'] or verify_pass(password, user.password) == False:
                    return jsonify({"message": "Wrong user name or password was provided: '" +username+"'"}),400
                user.loginDateTime = datetime.utcnow()
            elif loginMode == 'user':
                username = request.form['username']
                email = request.form['email']
                authProvider = request.form['authProvider']
                role = ROLE['user']
                if ((username is None or len(username) == 0) or (email is None or len(email) == 0) or (authProvider is None or len(authProvider) == 0)):
                    return jsonify({"message": "Invalid user authentication details were provided: '" +username+"'"}),400
                user = Users.query.filter_by(email=email).first()
                if user is None:
                    user = Users(userId,ip_address,username,email,authProvider,role)                
                    isNewUser = True
                else:
                    user.loginDateTime = datetime.utcnow()
            else:
                username = request.form['username']     
                if username is None or len(username) == 0:
                    return jsonify({"message": "Invalid user name was provided: '" +username+"'"}),400
                userId = str(uuid.uuid4())
                isNewUser = True
                user = Users(userId,ip_address,username,email,authProvider,role)
    
            # Check the password
            if user:
                login_user(user)
                jwtBearerToken = getJwtBearerToken(user.claimPayload())
                user.accessToken = jwtBearerToken
                if isNewUser == True:
                    db.session.add(user)
                db.session.commit()
                return jsonify({"AccessToken": jwtBearerToken,"UserName":user.name}),200
                

    @blueprint.route('/api/v1/logout', methods=['GET', 'POST'])
    @login_required
    @requires_access_level(ROLE['guest'])
    def logout():
        username=''
        if current_user.is_authenticated:  
            username = current_user.name    
            user = Users.query.filter_by(id=current_user.id).first()
            if user is not None:
                db.session.delete(user)
                db.session.commit() 

            logout_user()       

        return jsonify({"message": "Hello " +username + ", you have logout successfully."}),200


    # Errors

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return jsonify({"message": "You are not authorized to access this resource."}), 401


    @blueprint.errorhandler(403)
    def access_forbidden(error):
        return jsonify({"message": "You do not have sufficient permission to access this resource."}), 403


    @blueprint.errorhandler(404)
    def not_found_error(error):
        return jsonify({"message": "Requested resource is not available."}), 404


    @blueprint.errorhandler(500)
    def internal_error(error):
        return jsonify({"message": "We are unable to process your request at the moment. Kindly retry after some time."}), 500
