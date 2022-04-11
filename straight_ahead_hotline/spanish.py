from flask import (
         Blueprint, request, url_for,
        )
from twilio.twiml.voice_response import VoiceResponse, Gather

# all routes in this blueprint are pre-pended with '/spanish'
bp = Blueprint('fundraising', __name__, url_prefix='/spanish')

def menu():
    """Respond to incoming phone calls with a menu of options."""
    resp = VoiceResponse()
    resp.say('Welcome to press spanish')

    resp.redirect(url_for('welcome.index'))

    return str(resp)