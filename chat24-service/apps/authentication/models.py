from lib2to3.pgen2 import token
import string
from types import ClassMethodDescriptorType
from flask_login import UserMixin
from apps.authentication.crypto_util import getClaimPayload
from apps import db, login_manager
from datetime import datetime

ROLE = {
    'guest': 0,
    'user': 1,
    'admin': 2
}

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.String(64), primary_key=True)
    ipaddress = db.Column(db.String(64))
    name = db.Column(db.String(64))
    password = db.Column(db.String(250))
    email = db.Column(db.String(250))
    accessToken = db.Column(db.String(500))
    role = db.Column(db.Integer)
    authProvider = db.Column(db.String(64))
    loginDateTime = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, userId,ip_address,username, email,authProvider,role=ROLE['guest']):
        self.id = userId
        self.ipaddress = ip_address
        self.name = username
        self.role = role
        self.email = email
        self.authProvider = authProvider

    def is_admin(self):
        return self.role == ROLE['admin']

    def allowed(self, role):
        return self.role >= role

    def __repr__(self):
        return str(self.claimPayload())
        
    def claimPayload(self):
        return {"id": self.id,
                "ipaddress": self.ipaddress,
                "name": self.name,
                "role": "guest" if self.role == ROLE['guest'] else "user" if self.role == ROLE['user'] else 'admin',
                "email": self.email,
                "authProvider": self.authProvider}
    def serialize(self):
        return {"id": self.id,
                "ipaddress": self.ipaddress,
                "name": self.name,
                "role": "guest" if self.role == ROLE['guest'] else "user" if self.role == ROLE['user'] else 'admin',
                "email": self.email,
                "loginDateTime": self.loginDateTime,
                "authProvider": self.authProvider,
                "accessToken": self.accessToken}


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    bearerToken = request.headers.get('Authorization')
    if bearerToken.casefold().startswith("bearer "):
        token = bearerToken[7:]
        claim = getClaimPayload(token) 
        print(claim)   
        user = Users.query.filter_by(id=claim["id"]).first()
        if user is not None:
            return user
        else:
            return None
    else:
        return None
