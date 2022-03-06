from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a menu of options."""
    # Start our TwinML response
    resp = VoiceResponse()
    
    # Read a message aloud to the caller
    # resp.say("Thank you for calling Straight Ahead.", voice='alice')
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

    # Start our <gather> verb
    gather = Gather(num_digits=1)
    gather.say('Welcome to Straight Ahead. To contact fundraising, press "1", to contact a regional organizer, press "2".')
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect('/answer')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


