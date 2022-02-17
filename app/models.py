
from . import db
from werkzeug.security import  generate_password_hash, check_password_hash
from flask_login import  UserMixin
from . import login_manager
from  datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100),unique=True, index=True)
    log_password = db.Column(db.String(255))
    profile_img = db.Column(db.String())
    confirmed = db.Column(db.Boolean, default=False)
    comments = db.relationship('Recipe_comment', backref='user', lazy='dynamic')
    
    
    @property
    def password(self):
        raise AttributeError(' You can not access the password attribute')
    
    @password.setter
    def password(self,password):
        self.log_password = generate_password_hash(password)
        
    def password_verification(self,password):
        return check_password_hash(self.log_password,password)
    
    def generate_confirm_token(self,expire_time=1800):
        serial= Serializer(current_app.config['SECRET_KEY'], expire_time)
        return serial.dumps({'confirm': self.id})
    
    def confirm(self,token):
        serial = Serializer(current_app.config['SECRET_KEY'])
        try:
            data =serial.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    
    def generate_pass_reset_token(self,expire_time=1800):
        serial=Serializer(current_app.config['SECRET_KEY'],expire_time)
        return serial.dumps({'reset' : self.id})
    
    def password_reset(self,reset_token, new_pwd):
        serial = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = serial.loads(reset_token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_pwd
        db.session.add(self)
        return True
    def generate_auth_token(self,expire_time):
        serial = Serializer(current_app.config['SECRET_KEY'],expires_in=expire_time)
        return serial.dumps({'id': self.id}).decode('ascii')
    
    @staticmethod
    def verify_auth_token(auth_token):
        serial = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = serial.loads(auth_token)
        except:
            return None
        return User.query.get(data['id'])
    
    def __repr__(self):
        return f'User {self.name}'
    
    
class Recipe:
    def __init__(self, id,name,image,link,content):
        self.id = id
        self.name = name
        self.image = image
        self.link = link
        self.content = content
        
class Recipe_comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    recipe_id = db.Column(db.Integer)
    recipe_title = db.Column(db.String)
    image_path = db.Column(db.String)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()
     
    @classmethod    
    def fetch_review(cls,id):
        res = cls.query.filter_by(recipe_id=id).all()
        return res
    

# class Likes(db.Model):
#     __tablename__ = 'likes'

#     id = db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
#     recipe_id = db.Column(db.Integer, db.ForeignKey())            
        