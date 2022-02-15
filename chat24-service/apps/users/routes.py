
from flask_login import (
    login_required,current_user
)

from apps import db
from apps.authentication import blueprint
from apps.authentication.models import Users

from flask import request, jsonify

@blueprint.route('/api/v1/users', methods=['GET'])
@login_required
def get():
    user ={}
    id = request.args.get("id")
    if id is not None:
        user =Users.query.filter_by(id=id).first()
    else:
        user = Users.query.filter_by(id=current_user.id).first()
    
    if user is not None:
        return jsonify(user.serialize()),200  
    else:
        return jsonify("User is not found"),404    

@blueprint.route('/api/v1/users/all', methods=['GET'])
@login_required
def getAll():
    users = Users.query.all() 
    return jsonify([user.serialize() for user in users]),200    

@blueprint.route('/api/v1/users', methods=['DELETE'])
@login_required
def delete():
    id = request.args.get("id")
    if id is not None:
        user = Users.query.filter_by(id=id).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User is removed successfully"}),200
        
    return jsonify({"message": "user is not available"}),404
