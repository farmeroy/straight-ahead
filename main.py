from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    """Respond to incoming phone calls with a menu of options."""
    # Start our TwinML response
    resp = VoiceResponse()

    # Start our <gather> verb
    gather = Gather(num_digits=1, action='/menu')
    gather.say("For Press Request please press 1. " +
               "For Fundraising please press 2. " +
               "For Organizing please press 3. " +
               "For Spanish please press 4. ", loop=3)
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect('/welcome')

    return str(resp)


@app.route("/menu", methods=['GET', 'POST'])
def menu():
    resp = VoiceResponse()
    selected_option = request.values['Digits']
    option_actions = {'1': '/press_request',
                      '2': '/fundrasing',
                      '3': '/organizing',
                      '4': '/spanish'}

    if selected_option in option_actions:
        response = VoiceResponse()
        choice = option_actions[selected_option]
        response.redirect(choice)
        return str(response)

    resp.redirect('/welcome')

    return str(resp)


@app.route('/press_request', methods=['GET', 'POST'])
def press_request():
    resp = VoiceResponse()
    resp.say('You have reached press_request')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/fundrasing', methods=['GET', 'POST'])
def fundraising():
    resp = VoiceResponse()
    resp.say('You have reached fundraising')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/organizing', methods=['GET', 'POST'])
def organizing():
    """Respond to incoming phone calls with a menu of options."""
    # Start our TwinML response
    resp = VoiceResponse()

    # Start our <gather> verb
    gather = Gather(num_digits=1, action='/organizing_menu')
    gather.say("For Western Press please press 1. " +
               "For Central Press please press 2. " +
               "For South Eastern Press please press 3. " +
               "For Statewide General Campaign Questions please press 4. ", loop=3)
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect('/welcome')

    return str(resp)


@app.route("/organizing_menu", methods=['GET', 'POST'])
def organizing_menu():
    resp = VoiceResponse()
    selected_option = request.values['Digits']
    option_actions = {'1': '/western_press',
                      '2': '/central_press',
                      '3': '/south_eastern_press',
                      '4': '/statewide_general_campaign_questions'}

    if selected_option in option_actions:
        response = VoiceResponse()
        choice = option_actions[selected_option]
        response.redirect(choice)
        return str(response)

    resp.redirect('/welcome')

    return str(resp)


@app.route('/spanish', methods=['GET', 'POST'])
def spanish():
    resp = VoiceResponse()
    resp.say('You have reached spanish')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/western_press', methods=['GET', 'POST'])
def western_press():
    resp = VoiceResponse()
    resp.say('You have reached western press')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/central_press', methods=['GET', 'POST'])
def central_press():
    resp = VoiceResponse()
    resp.say('You have reached central press')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/south_eastern_press', methods=['GET', 'POST'])
def south_eastern_press():
    resp = VoiceResponse()
    resp.say('You have reached south eastern press')

    resp.redirect('/welcome')
    return str(resp)


@app.route('/statewide_general_campaign_questions', methods=['GET', 'POST'])
def statewide_general_campaign_questions():
    resp = VoiceResponse()
    resp.say('You have reached statewide general campaign questions')

    resp.redirect('/welcome')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
