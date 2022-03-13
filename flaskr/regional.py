from flask import (
         Blueprint, request,  url_for,
        )
from twilio.twiml.voice_response import VoiceResponse, Gather
import os    
from dotenv import load_dotenv    
load_dotenv()    

EASTERN_ORG_PHONE = os.getenv('EASTERN_ORG_PHONE')
 

# all routes in this blueprint are pre-pended with '/welcome'
bp = Blueprint('regional', __name__, url_prefix='/regional')

@bp.route('/menu', methods=['GET', 'POST'])
def menu():
    # Start our TwinML response
    resp = VoiceResponse()

    # Start our <gather> verb
    gather = Gather(num_digits=1, action=url_for('regional.gather'))
    gather.say('You have reached regional organizers menu,'
            ' press "1" for statewide campaign questions,'
            ' press "2" for western Pennsylvania,'
            ' press 3 for central Pennsylvania, '
            ' press 4 for south easter Pennsylvania'
            ' press 5 to return to the main menu.'
            )
    resp.append(gather)

    # If the user doesn't select an option, redirect
    resp.redirect(url_for('regional.menu'))

    return str(resp)


@bp.route('/gather', methods=['GET', 'POST'])
def gather():
    resp = VoiceResponse()
    selected_option = request.values['Digits']
    # all routes should be made with url_for to ensure correct routing
    option_actions = {'1': url_for('regional.statewide'),
                      '2': url_for('regional.western'),
                      '3': url_for('regional.central'),
                      '4': url_for('regional.south_eastern'),
                      '5': url_for('welcome.index')
                      }

    if selected_option in option_actions:
        response = VoiceResponse()
        choice = option_actions[selected_option]
        response.redirect(choice)
        return str(response)

    resp.redirect(url_for('welcome.index'))

    return str(resp)

@bp.route('/statewide', methods=['GET', 'POST'])
def statewide():
    resp = VoiceResponse()
    resp.say('You have reached statewide PA organizers')
    resp.redirect(url_for('welcome.index'))
    
    return str(resp)

@bp.route('/western', methods=['GET', 'POST'])
def western():
    resp = VoiceResponse()
    resp.say('You have reached western PA organizers')
    resp.redirect(url_for('welcome.index'))
    
    return str(resp)

@bp.route('/central', methods=['GET', 'POST'])
def central():
    resp = VoiceResponse()
    resp.say('You have reached central PA organizers')
    resp.redirect(url_for('welcome.index'))
    
    return str(resp)

@bp.route('/south_eastern', methods=['GET', 'POST'])
def south_eastern():
    resp = VoiceResponse()
    resp.say('Your call is being forwarded to the contact for South Eastern Pennsylvania.')
    resp.dial(EASTERN_ORG_PHONE)
    resp.redirect(url_for('welcome.index'))
    
    return str(resp)


