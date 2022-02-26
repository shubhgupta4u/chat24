from functools import wraps
from flask import session, jsonify
from apps.authentication.models import Users
from flask_login import (
    current_user
)

def requires_access_level(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = Users.query.filter_by(id=current_user.id).first()  
            if user is None:
                return jsonify({"message": "You are not authorized to access this resource."}), 401
            elif not user.allowed(role):
                return jsonify({"message": "You do not have sufficient permission to access this resource."}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator