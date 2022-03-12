from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev'
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


       

    @app.route('/fundraising', methods=['GET', 'POST'])
    def fundraising():
        resp = VoiceResponse()
        resp.say('You have reached fundraising')
        
        resp.redirect('/voice')
        return str(resp)
    
    from . import welcome
    app.register_blueprint(welcome.bp)

    from . import regional
    app.register_blueprint(regional.bp)

    app.add_url_rule('/', endpoint='index')

    return app

