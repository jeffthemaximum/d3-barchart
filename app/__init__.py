from flask import Flask
from app import config
import logging, sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.config.from_object(config)

from app import routes