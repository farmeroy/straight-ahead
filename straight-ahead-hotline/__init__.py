from flask import Flask, url_for
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

    
    from . import welcome
    app.register_blueprint(welcome.bp)

    from . import regional
    app.register_blueprint(regional.bp)

    from . import fundraising
    app.register_blueprint(fundraising.bp)

    # This sets our default endpoint
    # Because welcome.py has no url_prefix, it is the root '/'
    app.add_url_rule('/', endpoint='index')

    return app

