from flask import Flask
from os.path import isfile, join, abspath, dirname
from flask import render_template
from yaml import load as yaml_load
from flask import url_for, send_from_directory, abort as abort_flask
import random


# PATH RELATIVITY #############################################################

ROOT_DIRECTORY = dirname(dirname(abspath(__file__)))


def get_path(relative_path):
    """Get an absolute path from the relative path to this project directory."""
    return abspath(join(ROOT_DIRECTORY, relative_path))

# CONFIG ######################################################################
with open(get_path('config.yml'),'r') as config_file:
    config = yaml_load(config_file.read())

# LOGGING #####################################################################

# CREATE FLASK APP ############################################################
app = Flask(__name__)


def static_global(filename):
    return url_for('static', filename=filename)

# SET CONFIG GLOBAL VARIABLE ##################################################

@app.context_processor
def inject_new_conf():
    return dict(config=config,static=static_global)

# SETUP JINJA2 TEMPLATES ######################################################
@app.template_filter('shuffle')
def shuffle_filter(seq):
    """
    This shuffles the sequence it is applied to.
    Jinja2 _should_ provide this.
    """
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq
# ROUTING  ####################################################################

@app.route('/')
def hello_world():
    return render_template('home.html.jinja2')


if __name__ == "__main__":
    app.run(debug=True)