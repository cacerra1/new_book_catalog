from datetime import datetime
from app import db, bcrypt  # app/__inti__.py
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now) # this will auto populate and capture when account was created

    def check_password(self, password): # uses self because this is an instance and not a class method and password entered by user
        return bcrypt.check_password_hash(self.user_password, password) # checks the hashed PW in DB and compare enter to the user. if match it truens true

    @classmethod  # created a class method. that's what the decorator signifies. keyworld cls shows its a class method
    # cls instead of self because it belongs to the class and not an instance
    def create_user(cls, user, email, password):
        user = cls(user_name=user,  # define fields for DB here. get these values when user submits form data
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8')) # generates PW hash
        db.session.add(user) # add user to DB session and commit it (saves to DB)
        db.session.commit()
        return user # return the user we created


@login_manager.user_loader  # nothing more than the instance of login_manager
def load_user(id):
    return User.query.get(int(id))
