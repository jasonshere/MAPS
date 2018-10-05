import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from init import db, ma, PREFIX
import hashlib

# model for clerk
class Clerk(db.Model):
    """
    Clerk Model
    """
    
    __tablename__ = '{}clerk'. format(PREFIX)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    # initialise model
    def __init__(self, data):
        """
        constructor
        :param data: init data
        """
        for field in data:
            setattr(self, field, data[field])
        db.create_all()

    # add a clerk
    def addClerk(self):
        """
        add a new clerk
        :return: Boolean
        """
        self.password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        db.session.add(self)
        return db.session.commit()

    # login a clerk
    def login(self):
        """
        sign in clerk
        :return: Boolean, Object
        """
        result = self.query.filter(\
                                Clerk.username == self.username,\
                                Clerk.password == hashlib.sha224(self.password.encode('utf-8')).hexdigest()\
                            ).first()
        result = clerk_schema.dump(result)
        if result.data :
            return True, result.data
        else:
            return False, {}

class ClerkSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'name', 'phone', 'age', 'sex', 'password', 'created_at')

clerk_schema = ClerkSchema()
clerks_schema = ClerkSchema(many=True)