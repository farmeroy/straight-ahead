from flask import (
         Blueprint, request, url_for,
        )
from twilio.twiml.voice_response import VoiceResponse, Gather

# all routes in this blueprint are pre-pended with '/welcome'
bp = Blueprint('welcome', __name__, url_prefix='/welcome')

@bp.route('/', methods=['GET', 'POST'])
def index():
    """Respond to incoming phone calls with a menu of options."""
    # Start our TwinML response
    resp = VoiceResponse()

    # Start our <gather> verb
    gather = Gather(num_digits=1, action=url_for('welcome.gather'))
    gather.say('Welcome to Straight Ahead. To contact fundraising, press "1", to contact a regional organizer, press "2".')
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect(url_for('welcome.index'))

    return str(resp)

@bp.route("/gather", methods=['GET', 'POST'])
def gather():
    # Start our TwinML response
    resp = VoiceResponse()
    selected_option = request.values['Digits']
    # define routes with url_for to ensure correct routing
    option_actions = {'1': url_for('fundraising.menu'),
                      '2': url_for('regional.menu'),
                      }

    if selected_option in option_actions:
        response = VoiceResponse()
        choice = option_actions[selected_option]
        response.redirect(choice)
        return str(response)

    resp.redirect(url_for('welcome.index'))

    return str(resp)
