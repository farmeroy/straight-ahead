from flask import (
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
from twilio.twiml.voice_response import VoiceResponse
from flask import Flask
from view_helpers import twiml

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# This part is working you can do "http//......../welcome"

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu'), method="POST"
    ) as g:
        g.say(message="For Press Request please press 1. " +
                      "For Fundraising please press 2. " +
                      "For Organizing please press 3. " +
                      "For Spanish please press 4. ", loop=3)
    return twiml(response)


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = {'1': press_request,
                      '2': fundrasing,
                      '3': organizing_menu,
                      '4': spanish}

    if option_actions in selected_option:
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()


# This bit cant figure it yet it gives an error.
# werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a
# request that this server could not understand.
# KeyError: 'Digits'

@app.route('/organizing', methods=['GET', 'POST'])
def organizing():
    selected_option = request.form['Digits']
    option_actions = {'2': "+12024173312",
                      '3': "+12024173378",
                      '4': "+12027336386",
                      "5": "+12027336637"}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.dial(option_actions[selected_option])
        return twiml(response)

    return _redirect_welcome()


# private methods

def press_request(response):
    response.dial("+12027336646")
    return response


def fundrasing(response):
    response.dial("+12027336646")
    return response


def spanish(response):
    response.dial("+12027336646")
    return response


def organizing_menu(response):
    with response.gather(
            numDigits=1, action=url_for('organizing'), method="POST"
    ) as g:
        g.say("To call the Western press 1. To call the " +
              "Central press 2. To call the  South Eastern press 3 " +
              "To call the Statewide General Campaign Questions press 4.",
              voice="alice", language="en-GB", loop=3)

    return response


# This code returns all the way to welcome message
def _redirect_welcome():
    response = VoiceResponse()
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect(url_for('welcome'))

    return twiml(response)


if __name__ == "__main__":
    app.run(debug=True)
