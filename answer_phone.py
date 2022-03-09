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
    selected_option = request.values['Digits']
    option_actions = {'1': '/fundraising',
                      '2': '/organizing_menu',
                      }

    if selected_option in option_actions:
        response = VoiceResponse()
        choice = option_actions[selected_option]
        response.redirect(choice)
        return str(response)

    resp.redirect('/voice')

    return str(resp)
   
@app.route('/organizing_menu', methods=['GET', 'POST'])
def organizing_menu():
    resp = VoiceResponse()
    resp.say('You have reached regional organizers menu.')
    # selected_option = request.form['Digits']
    # option_actions = {'1': western_press,
    #                   '2': central_press,
    #                   '3': south_eastern_press,
    #                   '4': statewide_general_campaign_questions}

    # if option_actions in selected_option:
    #     response = VoiceResponse()
    #     option_actions[selected_option](response)
    #     return twiml(response)

    resp.redirect('/voice')
    return str(resp)

@app.route('/fundraising', methods=['GET', 'POST'])
def fundraising():
    resp = VoiceResponse()
    resp.say('You have reached fundraising')
    
    resp.redirect('/voice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)


