
import uuid
from flask import request, jsonify
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.models import Users

from apps.authentication.util import verify_pass,getJwtBearerToken

# Login & Registration

@blueprint.route('/api/v1/login', methods=['POST'])
def login():
        # read form data
        username = request.form['username']
        password = request.form['password']
        if username is None or len(username) == 0 and verify_pass(password, "Password@1") == False:
            # Something (user or pass) is not ok
            return jsonify({"message": "Wrong user name was provided: '" +username+"'"}),400

        userId = str(uuid.uuid4())
        ip_address = request.remote_addr
        user = Users(userId,ip_address,username)
       
        # Check the password
        if user:

            login_user(user)
            jwtBearerToken = getJwtBearerToken(user.serialize())
            user.accessToken = jwtBearerToken
            db.session.add(user)
            db.session.commit()
            return jsonify({"AccessToken": jwtBearerToken,"UserName":user.name}),200
            

@blueprint.route('/api/v1/logout', methods=['GET', 'POST'])
@login_required
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
