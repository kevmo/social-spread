import os

from flask import Flask

from config import DevConfig


# Set up a singe app instance.
app = Flask(__name__)

# Load this from an environment variable you can
# set in the env, e.g. on a server vs locally vs AWS...
app.config.from_object(os.environ.get('APP_SETTINGS', DevConfig))


@app.route('/')
def hello():
    return "HELLOOO"


@app.route('/check-config')
def check_config():
    print "CHECK IT: ", app.config['CONFIG']
    return app.config['CONFIG']


# TODO: This isn't how you should run a production server.
if __name__ == "__main__":
  app.run(debug=True)