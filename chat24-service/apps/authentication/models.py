from types import ClassMethodDescriptorType
from flask_login import UserMixin
from apps.authentication.util import getClaimPayload
from apps import db, login_manager

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.String(64), primary_key=True)
    ipaddress = db.Column(db.String(64))
    name = db.Column(db.String(64))
    accessToken = db.Column(db.String(255))

    def __init__(self, userId,ip_address,username):
        self.id = userId
        self.ipaddress = ip_address
        self.name = username

    def __repr__(self):
        return str(self.username)
    
    def serialize(self):
        return {"id": self.id,
                "ipaddress": self.ipaddress,
                "name": self.name,
                "accessToken": self.accessToken}


@login_manager.user_loader
def user_loader(id):
    print('user_loader')
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    bearerToken = request.headers.get('Authorization')
    claim = getClaimPayload(bearerToken)    
    user = Users.query.filter_by(id=claim["id"]).first()
    if user is not None:
        return user
    else:
        return None
