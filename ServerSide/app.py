from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Accounts(db.Model):
    userId = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    

    def __repr__(self):
        return '<Account %r>' % self.userId

class Cards(db.Model):
    cardId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(30), db.ForeignKey('accounts.userId'))
    vocabNL = db.Column(db.String(100), nullable=False)
    vocabTL = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    
    def __repr__(self):
        return '<Card %r>' % self.cardID
    
with app.app_context():
        db.create_all()



if __name__ == '__main__':
    app.run(debug=True)