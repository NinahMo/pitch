from flask import render_template
from app import app

# Views
@app.route('/', methods = ['GET,'POST])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = pitch
    pickuplines = Pitch.query.filter_by(category="pickuplines")
    interviewpitch = Pitch.query.filter_by(category ="interviewpitch")
    promotionpitch = Pitch.query.filter_by(category ="promotionpitch")
    productpitch =  Pitch.query.filter_by(category ="productpitch")

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)

    return render_template('index.html', title = title, pitch = pitch, pickuplines = pickuplines, interviewpitch = interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)