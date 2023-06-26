from flask import Flask
from .views import getmail
from .views import account

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')
app.register_blueprint(getmail.gm)
app.register_blueprint(account.ac)


