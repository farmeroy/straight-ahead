from flask import (
         Blueprint, request,  url_for,
        )
from twilio.twiml.voice_response import VoiceResponse, Gather

# all routes in this blueprint are pre-pended with '/welcome'
bp = Blueprint('regional', __name__, url_prefix='/regional')

@bp.route('/', methods=['GET', 'POST'])
def menu():
    pass

@bp.route('/menu', methods=['GET', 'POST'])
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

