from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/menu')
    gather.say('For YES, press 1. For No, press 2.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/welcome')

    return str(resp)


@app.route('/menu', methods=['GET', 'POST'])
def first_menu():
    """Processes results from the <Gather> prompt in /welcome"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('You selected YES. Good for you!')
            return str(resp)
        elif choice == '2':
            resp.say('You selected NO. Good for you!!')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /answer
    resp.redirect('/welcome')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
