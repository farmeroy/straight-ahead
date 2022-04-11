from flask import (
         Blueprint, request, url_for,
        )
from twilio.twiml.voice_response import VoiceResponse, Gather

# all routes in this blueprint are pre-pended with '/press_request'
bp = Blueprint('fundraising', __name__, url_prefix='/press_request')

def menu():
    """Respond to incoming phone calls with a menu of options."""
    resp = VoiceResponse()
    resp.say('Welcome to press request')

    resp.redirect(url_for('welcome.index'))

    return str(resp)