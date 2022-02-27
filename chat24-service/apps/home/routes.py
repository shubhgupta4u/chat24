from apps.authentication import blueprint
from flask import request,jsonify
from apps.authentication.crypto_util import hash_pass

class HomeController:
    @blueprint.route('/', methods=['GET'])
    def home():    
        return jsonify("Welcome to chat24 Api Service..."),200  

    @blueprint.route('/api/v1/hashPwd', methods=['GET'])
    def hashPwd():    
        password = request.form['password']
        pwdhash = hash_pass(password)
        return jsonify(pwdhash.decode('ascii')),200  