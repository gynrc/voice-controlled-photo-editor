from . import db
from werkzeug.security import generate_password_hash

# User model to store login credentials
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    profile_photo = db.Column(db.String(255))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  
        except NameError:
            return str(self.id)
    
    def __init__(self, username, password, firstname, lastname, profile_photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.profile_photo = profile_photo

    def __repr__(self):
        return f'<User %r {self.id}>'

# Photo model to store uploaded photos
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

    def __init__(self, user_id, file_path):
        self.user_id = user_id
        self.file_path = file_path
    
    def __repr__(self):
        return f'<Photo %r {self.id}>'

# Voice command model
class VoiceCommand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    command_path = db.Column(db.String(200), nullable=False)
    command_prompt = db.Column(db.String(200), nullable=False)


    def __init__(self, user_id,command_path, command_prompt):
        self.user_id = user_id
        self.command_path = command_path
        self.command_prompt = command_prompt
    
    def __repr__(self):
        return f'<VoiceCommand %r {self.id}>'

# Edited design model
class Designs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    design_file_path = db.Column(db.String(200), nullable=False)
    design_filename = db.Column(db.String(200), nullable=False)

    @staticmethod
    def get_all_designs():
        return Designs.query.all()
    
    def __init__(self, user_id, design_filename, design_file_path):
        self.user_id = user_id
        self.design_filename = design_filename
        self.design_file_path = design_file_path
    
    def __repr__(self):
        return f'<Designs %r {self.id}>'

# ExtendScript files model
class ExtendScripts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    script_file_path = db.Column(db.String(255), nullable=False) 
    script_filename = db.Column(db.String(200), nullable=False)  # Store the generated filename

    @staticmethod
    def get_all_scripts():
        return ExtendScripts.query.all()

    def __init__(self, user_id, script_file_path, script_filename):
        self.user_id = user_id
        self.script_file_path = script_file_path
        self.script_filename = script_filename

    def __repr__(self):
        return f'<ExtendScripts %r {self.id}>'
