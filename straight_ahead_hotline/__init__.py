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

    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Respond to incoming phone calls with a menu of options."""
        # Start our TwinML response
        resp = VoiceResponse()

        # Start our <gather> verb
        gather = Gather(num_digits=1, action='welcome/gather')
        gather.say('Welcome to Straight Ahead. To contact fundraising, press "1", to contact a regional organizer, press "2".')
        resp.append(gather)

        # If the user doesn't select an option, redirect
        resp.redirect(url_for('welcome.index'))

        return str(resp)

    
    from . import welcome
    app.register_blueprint(welcome.bp)

    from . import regional
    app.register_blueprint(regional.bp)

    from . import fundraising
    app.register_blueprint(fundraising.bp)

    from . import press_request
    app.register_blueprint(press_request.bp)

    from . import spanish
    app.register_blueprint(spanish.bp)

    app.add_url_rule('/', endpoint='index')

    return app

