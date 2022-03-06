from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options."""
    # Start our TwinML response
    resp = VoiceResponse()

    # Start our <gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('Welcome to Straight Ahead. To contact fundraising, press "1", to contact a regional organizer, press "2".')
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect('/voice')

    return str(resp)

@app.route("/gather", methods=['GET', 'POST'])
def gather():
    # Start our TwinML response
    resp = VoiceResponse()
    
    # If the request already gathered digits, process them
    if 'Digits' in request.values:
        # get the digit
        choice = request.values['Digits']
        # conditionally <say> messages
        if choice == '1':
            resp.say('You will be redirected to fundraising')
            return str(resp)
        elif choice == '2':
            resp.say('Please choose your region')
            return str(resp)
        else:
            resp.say("I didn't understand your response.")

    # If the user didn't choose 1 or 2 send back to /voice
    resp.redirect('/voice')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)


