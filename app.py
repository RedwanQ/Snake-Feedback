from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    game = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    commnets = db.Column(db.Text())

    def __init__(self, customer, game, rating, comments):
        self.customer = customer
        self.game = game
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        game = request.form['game']
        rating = request.form['rating']
        commnets = request.form['comments']
        print(customer,game,rating,commnets)
        
        if customer == '' or game == '':
            return render_template('index.html', message='Please enter required Fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, game, rating, commnets)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, game, rating, commnets)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.debug = True
    app.run()