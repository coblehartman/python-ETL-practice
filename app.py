from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class ShortURL(db.Model):
    __tablename__ = 'short_urls'
    id = db.Column(db.Integer, primary_key=True)
    original_urls = db.Column(db.string(), nullable=False)
    short_urls = db.Column(db.string(), nullable=False)

    def generate_short_url(self, session):
        characters = string.ascii_letters + string.digits
        while True:
            path = ''.join(random.choices(characters, k=6))
            if not session.query(ShortURL).filter_by(short_url=path).first():
                return path
            
with app.app_context():
    db.create_all()
    
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url
        
    shortened_url = ShortURL(original_url=original_url)
    shortened_url.short_url = shortened_url.generate_short_url(db.session)
    db.session.add(shortened_url)
    db.session.commit()
    
    return jsonify({'shortened_url' : request.host_url + shortened_url.short_url})

@app.route('/<shortened_url>')
def redirect_to_original(shortened_url):
    shortened_url = ShortURL.query.filter_by(short_url=shortened_url).first_or_404()\
    return redirect(short_url)