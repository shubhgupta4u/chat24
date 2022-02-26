from flask_login import (
    login_required,current_user
)

from apps import db
from apps.authentication import blueprint
from apps.authentication.auth_util import requires_access_level
from apps.authentication.models import ROLE, Users
from datetime import datetime,timedelta
from flask import request, jsonify

@blueprint.route('/api/v1/user', methods=['GET'])
@requires_access_level(ROLE['guest'])
@login_required
def user():
    user = Users.query.filter_by(id=current_user.id).first()
    
    if user is not None:
        return jsonify(user.serialize()),200  
    else:
        return jsonify("User is not found"),404  

@blueprint.route('/api/v1/users', methods=['GET'])
@requires_access_level(ROLE['admin'])
@login_required
def users():
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
@requires_access_level(ROLE['admin'])
def getAll():
    activeInLastNDay=None
    if request.args.get("ActiveInLastNDay"):
        activeInLastNDay = int(request.args.get("ActiveInLastNDay"))
    roleName = request.args.get("Role")
    users = [] 
    if roleName is not None:
        users =Users.query.filter_by(role = ROLE[roleName])
    else:    
        users = Users.query.all() 

    if activeInLastNDay is not None and activeInLastNDay >= 0:
        current_time = datetime.now()
        nDayAgo = current_time - timedelta(days =activeInLastNDay)
        users = filter(lambda x: x.loginDateTime > datetime(nDayAgo.year,nDayAgo.month,nDayAgo.day), users)

    return jsonify([user.serialize() for user in users]),200    

@blueprint.route('/api/v1/users', methods=['DELETE'])
@login_required
@requires_access_level(ROLE['admin'])
def delete():
    id = request.args.get("id")
    if id is not None:
        user = Users.query.filter_by(id=id).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User is removed successfully"}),200
        
    return jsonify({"message": "user is not available"}),404

@blueprint.route('/api/v1/users/purge', methods=['DELETE'])
@login_required
@requires_access_level(ROLE['admin'])
def purgeGuestUser():
    inActiveInLastNDay=None
    if request.args.get("InActiveInLastNDay"):
        inActiveInLastNDay = int(request.args.get("InActiveInLastNDay"))
    roleName = request.args.get("Role")
    if inActiveInLastNDay is not None and roleName is not None and inActiveInLastNDay > 0 and roleName != 'admin':
        users =Users.query.filter_by(role = ROLE[roleName])
        current_time = datetime.now()
        nDayAgo = current_time - timedelta(days =inActiveInLastNDay)
        print(datetime(nDayAgo.year,nDayAgo.month,nDayAgo.day))
        users = filter(lambda x: x.loginDateTime < datetime(nDayAgo.year,nDayAgo.month,nDayAgo.day), users)
        [db.session.delete(user) for user in users]
        db.session.commit()
        return jsonify({"message": "Users are purged successfully"}),200
    else:        
        return jsonify({"message": "Invalid query parameters"}),400
